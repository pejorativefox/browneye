# browneye — LFS r13.1 base rewrite and build container

Status: planning. Created 2026-10-30.
Branch of record: `gcc-13-update` (`origin/gcc-13-update`).
Work root: `~/browneye`.

Two work items:

1. **Item 1 — Version parity.** Bring the base-system RPM specs in line with the
   **LFS r13.1 release tag**, including the book's extra commands and patches.
2. **Item 2 — Base build container.** Turn the resulting base RPM set into a
   container image that can compile the *remaining* specs, so the rest of the
   distro can be upgraded from inside the target environment rather than on the host.

The container depends on Item 1, but Item 1's early waves only need the host.

---

## 0. Ground truth and decisions

### 0.1 Source of truth

- LFS tree: `/home/daspork/repos/lfs`.
- Target: **tag `r13.1`** = commit `71ef60ba3cf255023d1919135c9ce1e1a426f2d8`.
  The working tree is trunk (`581459fa3`, r13.1+16); **do not** take package
  versions from the working tree. Differences to watch:
  xz 5.8.3 (tag) vs 5.8.4, openssl 4.0.1 vs 4.0.2, pcre2 10.47 vs 10.48,
  iproute2 7.1.0 vs 7.2.0, man-pages 6.18 vs 6.19, iana-etc 20260805 vs 20260911,
  expat 2.8.3 vs 2.8.4, automake 1.18.1 vs 1.19, vim 9.2.1025 vs 9.2.1099,
  pkgconf 3.0.5 vs 3.0.7, elfutils 0.195 vs 0.196, systemd 261.2 vs 261.3.
- Base scope: `r13.1:chapter08/chapter08.xml` — 80 packages (systemd variant),
  79 (sysvinit variant), plus chapter 7 layout and chapter 9 config.
- r13.1 still ships `intltool` and `xml-parser`; trunk has them commented out.
  They stay in scope for r13.1.
- Current specs were written against roughly LFS 12.0 (glibc 2.38 / gcc 13.2 / linux 6.4).

### 0.2 Decisions (confirmed)

| # | Decision | Value |
|---|---|---|
| D1 | Init system | **systemd 261.2** (the book's systemd variant) |
| D2 | Library layout | **`/usr/lib64`** (Fedora-style, keep current layout) |
| D3 | Kernel | **deferred to phase 2**; boot tests use host kernel |
| D4 | Bootstrap scope | **chapter 8 built with host toolchain**; chapters 5–7 deferred |
| D5 | Version pin | **r13.1 tag** (`71ef60ba`) |

### 0.3 Divergences from the LFS book

These are deliberate and must be documented in each affected spec:

1. **`/usr/lib64` instead of `/usr/lib`.** Every LFS `--libdir=/usr/lib`,
   `libc_cv_slibdir=/usr/lib`, and `--with-pkg-config-libdir=/usr/lib/pkgconfig`
   becomes `%{_libdir}`. `/lib64` is a symlink to `usr/lib64` so the dynamic loader
   path `/lib64/ld-linux-x86-64.so.2` resolves.
2. **No kernel** in phase 1.
3. **Chapter 8 only**, built by the host compiler (gcc 16.2.1 vs LFS 16.2.0).
4. **r13.1**, not trunk.

Init is *not* a divergence: the base follows the book's systemd variant
(systemd 261.2 + dbus 1.16.2 + markupsafe/jinja2), and udev comes from systemd.

### 0.4 Definitions of done

- **Item 1 done** when every base package builds from its spec, the RPM set is
  dependency-closed, installs into a clean rootfs, and boots to
  `multi-user.target` under systemd in QEMU (host kernel).
- **Item 2 done** when `podman run browneye/base:<tag> ./bbuild build <spec>`
  succeeds for a package that is *not* in the base set.

---

## 1. Item 1 — Version parity with LFS r13.1

### 1.1 Work root and branch

- [ ] 1.1.1 Create `~/browneye` as a git worktree so the `master` checkout stays
      untouched:
      ```bash
      git -C ~/repos/browneye worktree add -b lfs-r13.1 ~/browneye origin/gcc-13-update
      ```
      Fallback: `git clone ~/repos/browneye ~/browneye && git -C ~/browneye switch gcc-13-update`.
- [ ] 1.1.2 Copy/commit this `plan.md` into `~/browneye`.
- [ ] 1.1.3 Add `lfs.lock` (`LFS_TAG=r13.1`, `LFS_COMMIT=71ef60ba…`).

### 1.2 Pin the LFS snapshot and generate the inventory

- [ ] 1.2.1 Generate `lfs.lock` from **`git show r13.1:packages.ent`** and
      `r13.1:patches.ent` (expand compound entities: `perl 5.44.0`, `linux`,
      `sqlite 3.53.4`). Include md5 + URL for every source and patch.
- [ ] 1.2.2 Build the LFS ↔ spec mapping table (`lfs_name -> package_specs/dir`):
      `procps -> procps-ng`, `sqlite -> sqlite3`, `libelf -> elfutils`,
      `flit-core -> python-flit-core`, `packaging -> python-packaging`,
      `wheel -> python-wheel`, `setuptools -> python-setuptools`,
      `jinja2 -> python-jinja`, `markupsafe -> python-markupsafe`.
- [ ] 1.2.3 Flag packages outside base scope: pcre1, python2-*, yum, eudev,
      systemd-sysvinit variant packages, and the repo's non-LFS init stack
      (`finit`, `libite`, `libuev`, `sysklogd`) which is retired from the base.
- **Done when:** `lfs.lock` regenerates deterministically from the tag.

### 1.3 Host seed environment

- [ ] 1.3.1 Install on Fedora 44: `rpm-build rpmdevtools createrepo_c
      squashfs-tools syslinux genisoimage dracut gperf texinfo python3-devel
      perl bison flex gawk gettext-devel`.
- [ ] 1.3.2 Create `~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}`.
- [ ] 1.3.3 Install `rpmsupport/rpmmacros` (patched per 1.4) to `~/.rpmmacros` and
      put `rpmsupport/strip_debug.sh` on `PATH`.
- [ ] 1.3.4 Record host `gcc`/`binutils`/`rpm` versions in `lfs.lock`.
- **Done when:** `bbuild build zlib` produces an RPM from the old spec, proving the
  harness works before content changes.

### 1.4 RPM layout (`/usr/lib64`, D2)

- [ ] 1.4.1 `rpmsupport/rpmmacros`: keep `%_libdir /usr/lib64`, set
      `%_lib /usr/lib64`, `%_prefix /usr`, `%_unitdir /usr/lib/systemd/system`,
      `%_udevrulesdir /usr/lib/udev/rules.d`,
      `%_build_id_links none`, and a minimal `%__spec_install_post` that does not
      depend on Fedora's `brp-*` scripts (needed again for Item 2).
- [ ] 1.4.2 Audit for LFS hardcoded `/usr/lib` and replace with `%{_libdir}`:
      `util-linux --libdir=/usr/lib`, `ncurses --with-pkg-config-libdir=/usr/lib/pkgconfig`,
      `pkgconf`, `zlib`, `libelf` `.pc` install path.
- [ ] 1.4.3 Confirm no `/usr/lib` library installs remain in the base set
      (`grep -n '/usr/lib/' package_specs/*/*.spec`).
- [ ] 1.4.4 Replace the `create_root_filesystem.sh` `/usr -> .` and
      `/lib64 -> lib` hack with a real layout package (1.10.5).
- **Done when:** a test RPM installs `libfoo.so.1` under `/usr/lib64` and
  `/lib64/ld-linux-x86-64.so.2` resolves after installing the layout package.

### 1.5 Build-system fixes (`bbuild` / `builder/`)

- [ ] 1.5.1 `builder/build.py`: create `~/rpmbuild/{SOURCES,BUILD,...}` before
      `fetch_sources()`.
- [ ] 1.5.2 `builder/package.py`: skip dirs without a `.spec` or without
      `sources`/`nosources` instead of hard-`exit()`.
- [ ] 1.5.3 `builder/sources.py`: tolerate comment lines; keep md5 verification;
      support `file://` and local `files/` entries.
- [ ] 1.5.4 Add `package_specs/ORDER` (book order) and make `build_all()` follow it.
- [ ] 1.5.5 Resolve spec names via `lfs.lock` aliases.
- [ ] 1.5.6 Add `bbuild build <spec-path>` for out-of-tree specs (used by Item 2).
- **Done when:** `bbuild build all` walks book order and `.package.sqlite` reports
  failures accurately.

### 1.6 Wave A — simple version bumps (~47 packages)

Source URL + md5 + `Version:` + filelist path updates only.

| Package | repo | r13.1 | Notes |
|---|---|---|---|
| acl | 2.3.1 | 2.4.0 | |
| attr | 2.5.1 | 2.6.0 | |
| autoconf | 2.71 | 2.73 | |
| automake | 1.16.5 | 1.18.1 | needs perl |
| bash | 5.2.15 | 5.3 | enumerated `%files` → globs |
| bzip2 | 1.0.8 | 1.0.8 | docs patch unchanged |
| dejagnu | 1.6.3 | 1.6.3 | |
| diffutils | 3.10 | 3.12 | |
| e2fsprogs | 1.47.0 | 1.47.4 | |
| expat | 2.5.0 | 2.8.3 | |
| expect | 5.45.4 | 5.45.4 | gcc15 patch |
| file | 5.45 | 5.48 | |
| findutils | 4.9.0 | 4.11.0 | |
| flex | 2.6.4 | 2.6.4 | |
| gawk | 5.2.2 | 5.4.1 | |
| gdbm | 1.23 | 1.26 | |
| gmp | 6.3.0 | 6.3.0 | |
| gperf | 3.1 | 3.3 | |
| grep | 3.11 | 3.12 | |
| gzip | 1.12 | 1.14 | |
| iana-etc | 20230810 | 20260805 | data only |
| inetutils | 2.4 | 2.8 | |
| intltool | 0.51.0 | 0.51.0 | r13.1 still includes it |
| iproute2 | 6.4.0 | 7.1.0 | |
| kmod | 30 | 34.2 | systemd dep |
| less | 643 | 704 | |
| libcap | 2.69 | 2.78 | systemd dep |
| libffi | 3.4.4 | 3.8.0 | |
| libpipeline | 1.5.7 | 1.5.8 | |
| libtool | 2.4.7 | 2.6.2 | |
| libxcrypt | 4.4.36 | 4.5.2 | |
| m4 | 1.4.19 | 1.4.21 | |
| make | 4.4.1 | 4.4.1 | |
| man-pages | 6.05.01 | 6.18 | data only |
| mpc | 1.3.1 | 1.4.1 | |
| mpfr | 4.2.1 | 4.2.2 | |
| ninja | 1.11.1 | 1.13.2 | |
| patch | 2.7.6 | 2.8 | |
| pkgconf | 2.0.1 | 3.0.5 | |
| psmisc | 23.6 | 23.7 | |
| sed | 4.9 | 4.10 | |
| tar | 1.35 | 1.35 | acl patch |
| texinfo | 7.0.3 | 7.3 | |
| xml-parser | 2.46 | 2.57 | r13.1 still includes it |
| xz | 5.4.4 | 5.8.3 | |
| zlib | 1.2.13 | 1.3.2 | |
| zstd | 1.5.5 | 1.5.7 | |

- [ ] 1.6.1 Bump in batches of ~10, building each batch.
- [ ] 1.6.2 Convert enumerated `%files` to globs while touching each spec.
- **Done when:** all Wave A packages build and pass `rpm -qpl` path checks.

### 1.7 Wave B — version bump plus build/command changes

| Package | repo → r13.1 | Required change |
|---|---|---|
| coreutils | 9.3 → 9.11 | `coreutils-9.11-i18n-1.patch`, `autoreconf -fv`, `automake -af`, `FORCE_UNSAFE_CONFIGURE=1`, post-install `chroot.8` sed |
| ncurses | 6.4 → 6.6 | `--without-normal --with-cxx-shared --enable-pc-files --with-pkg-config-libdir=%{_libdir}/pkgconfig`; two-pass install; `tic` XOPEN sed; `.so`/`.pc` wide-char shims under `/usr/lib64` |
| readline | 8.2 → 8.3 | `--docdir` currently hardcodes `8.2`; keep `--with-curses` |
| shadow | 4.13 → 4.20.2 | `--without-libbsd --disable-logind`; re-check passwd.5/getspnam.3/groups.1 seds; `touch /usr/bin/passwd` precondition |
| util-linux | 2.39.1 → 2.42.2 | `--libdir=%{_libdir}`, `--runstatedir=/run`, `--disable-liblastlog2` |
| kbd | 2.6.1 → 2.10.0 | `kbd-2.10.0-backspace-1.patch`; sed becomes `/RESIZECONS_PROGS=/s/yes/no/`; `make check` |
| groff | 1.23.0 → 1.24.1 | regenerate `groff.filelist`; verify `/usr/lib` references |
| vim | 9.0.1677 → 9.2.1025 | `vim90` runtime path → new dir; `vi` symlink |
| man-db | 2.11.2 → 2.13.1 | verify setuid/docdir flags |
| grub | 2.06 → 2.14 | build deps and configure flags |
| bc | 1.07.1 → 7.0.3 | upstream rewrite: replace autotools build with `configure.sh`/make |
| gettext | 0.22 → 1.0 | build system changes; keep `msgfmt/msgmerge/xgettext` |
| tcl | 8.6.13 → 8.6.18 | regenerate `autopath`/`conf` patches; filelist |
| libelf | elfutils 0.189 → 0.195 | build only `make -C lib`, `make -C libelf`; `--disable-debuginfod --enable-libdebuginfod=dummy`; install `.pc` to `%{_libdir}/pkgconfig` |
| sqlite | 3.24.0 (`sqlite3`) → 3.53.4 | rename dir to `sqlite`; `sqlite-autoconf-3530400`; update CPPFLAGS |
| procps | 4.0.3 (`procps-ng`) → 4.0.7 | version + `%files` |
| lz4 | missing | new spec: `make BUILD_STATIC=no PREFIX=/usr`, `make install` |
| mpdecimal | missing | new spec: `--disable-static --docdir=...` |

- [ ] 1.7.1 Port each change from `r13.1:chapter08/<pkg>.xml` and verify against the
      actual source tarball.
- [ ] 1.7.2 Vendor every patch under `package_specs/<pkg>/files/` with md5 in
      `sources`; do not depend on versioned linuxfromscratch.org URLs.
- **Done when:** all Wave B packages build and `rpm -qpR` shows expected libs only.

### 1.8 Wave C — toolchain (book order)

- [ ] 1.8.1 gmp → mpfr → mpc (Wave A versions, build-order pinned).
- [ ] 1.8.2 binutils 2.47: `--enable-ld=default --enable-plugins --enable-shared
      --enable-64-bit-bfd --enable-new-dtags --with-system-zlib
      --with-lib-path=/usr/lib64 --enable-default-hash-style=gnu`;
      `make tooldir=/usr`; drop `binutils-libtool-lib64.patch` if unneeded;
      regenerate `binutils.filelist`. (The r13.1 upstream-fix patch is applied in
      ch5, not ch8 — do not apply it here.)
- [ ] 1.8.3 glibc 2.44: patches `glibc-fhs-1.patch` +
      `glibc-2.44-upstream_fixes-1.patch` (r13.1 uses `-1`, not `-2`);
      `--disable-nscd`, **`libc_cv_slibdir=/usr/lib64`**,
      `--enable-kernel=5.10`, keep `--disable-werror
      --enable-stack-protector=strong`; drop `--with-headers`/`--libdir`;
      `make localedata/install-locales` into `glibc-locales`; nscd tmpfiles instead
      of service; regenerate `glibc.filelist`.
- [ ] 1.8.4 gcc 16.2.0: add `--enable-host-pie --enable-targets=all`; keep pie/ssp,
      `LD=ld`, `--with-system-zlib`; regenerate `gcc.filelist` and the
      `libstdc++.so.6.0.*` / python printer paths.
- [ ] 1.8.5 `/etc/ld.so.conf`, `ld.so.conf.d`, `nsswitch.conf` from glibc as
      `%config(noreplace)`; confirm `ldconfig` writes `/etc/ld.so.cache`.
- [ ] 1.8.6 Audit `%post` scriptlets; only ldconfig-style allowed.
- **Done when:** a program compiled against the new glibc/gcc RPMs in a `--root`
  chroot runs, and glibc's provides cover the symbol versions other RPMs require.

### 1.9 Wave D — languages, crypto, Python stack

- [ ] 1.9.1 openssl 3.1.2 → 4.0.1: re-derive configure flags, engine/provider dirs,
      `%files`.
- [ ] 1.9.2 pcre2 10.34 → 10.47 (retire pcre1).
- [ ] 1.9.3 perl 5.38.0 → 5.44.0: port `sh Configure -D ...` set incl.
      `useshrplib`, `usethreads`, privlib/archlib/site/vendor paths; regenerate
      `perl.filelist`.
- [ ] 1.9.4 python 3.11.4 → 3.14.7: `--enable-shared --with-system-expat
      --enable-optimizations --without-static-libpython`; ensurepip;
      `python3`/`python` symlinks; regenerate `python.filelist` for 3.14.
- [ ] 1.9.5 python modules used by systemd's build:
      markupsafe 2.1.3 → 3.0.3, jinja2 3.1.2 → 3.1.6. Also bump the rest of the
      r13.1 set for the afternoon build tooling: flit-core 3.9.0→4.0.2,
      packaging 19.2→26.3, wheel 0.41.1→0.48.0, setuptools 68.1.2→84.0.0.
      `pip install --root=%{buildroot}`.
- [ ] 1.9.6 meson 1.2.1 → 1.12.0, ninja (Wave A).
- **Done when:** `python3 -c "import jinja2, markupsafe"`, `perl -V`, and
  `openssl version` work inside the chroot built from RPMs.

### 1.10 Wave E — init (systemd) and configuration

- [ ] 1.10.1 **systemd 245 (disabled) → 261.2**: enable and rewrite the spec from
      `r13.1:chapter08/systemd.xml`.
      - meson options: `--prefix=/usr --buildtype=release -D default-dnssec=no
        -D firstboot=false -D install-tests=false -D ldconfig=false
        -D sysusers=false -D rpmmacrosdir=no -D homed=disabled -D man=disabled
        -D mode=release -D pamconfdir=no -D dev-kvm-mode=0660
        -D nobody-group=nogroup -D sysupdate=disabled -D ukify=disabled
        -D docdir=/usr/share/doc/systemd-%{version}`
      - **no patch**: the OpenSSL-4 buildfix patch is commented out at r13.1.
      - install pre-generated man pages from `systemd-man-pages-261.2.tar.xz`.
      - udev/udevadm/systemd-hwdb are produced by this package; **do not** build
        the standalone `udev` spec for the base (retire it).
      - ship default unit preset/enablement so the rootfs boots to
        `multi-user.target`.
- [ ] 1.10.2 **dbus 1.14.8 → 1.16.2**: r13.1 builds dbus with **meson**
      (`meson setup --prefix=/usr --buildtype=release --wrap-mode=nofallback ..`),
      not autotools — rewrite the spec's `%build`/`%install` accordingly.
- [ ] 1.10.3 **`browneye-basefs`** (replaces `create_root_filesystem.sh`):
      owns the chapter 7 layout and the Fedora-style merge symlinks
      `/bin→usr/bin`, `/lib→usr/lib`, `/lib64→usr/lib64`, `/sbin→usr/sbin`,
      plus `/usr/local/*`, `/var/{cache,log,spool,tmp}`, `/tmp` 1777, `/root` 0750.
- [ ] 1.10.4 **Chapter 9 config** into `browneye-sysconfig`: `/etc/os-release`,
      `/etc/hosts`, `/etc/shells`, `/etc/inputrc`, `/etc/vimrc`, `/etc/profile`,
      locale, `/etc/systemd/*` (journald, networkd, logind defaults),
      `/etc/udev/*`, network defaults, and systemd unit enablement/presets.
- [ ] 1.10.5 Credential baseline: `/etc/passwd`, `/etc/group`, `/etc/shadow`,
      `/etc/gshadow` (shadow spec; scriptlets guarded).
- [ ] 1.10.6 `browneye-release` 0.33rc2 → new version; parametrise `iso/core.repo`
      to a local URL instead of `192.168.31.94`.
- [ ] 1.10.7 Retire from the base (keep specs in-tree, unused):
      `finit`, `libite`, `libuev`, `sysklogd`, `sysvinit`, `eudev`, standalone
      `udev` (systemd now provides udev). Mark them `.disabled` or move to
      `package_specs/attic/`.
- **Done when:** a rootfs built from the RPMs boots under systemd in QEMU:
  `systemd-udevd` populates `/dev`, `systemd-journald` logs, and the console login
  works.

### 1.11 Filelists and `%files` normalisation

- [ ] 1.11.1 Regenerate base filelists at r13.1 versions: `binutils`, `gcc`,
      `glibc`, `groff`, `kbd`, `perl`, `python`, `tcl`.
- [ ] 1.11.2 Convert version-pinned enumerations to directory globs where safe
      (`bash`, `ncurses`, `readline`, `openssl`, `zlib`, `libffi`, `util-linux`,
      `systemd`).
- [ ] 1.11.3 Lint: no stale `/usr/lib` lib paths, no `%{buildroot}` in `%files`,
      no host-only paths, no missing filelist.
- **Done when:** `rpmbuild` emits no "File not found" / "unpackaged file" warnings.

### 1.12 Assemble the base repository

- [ ] 1.12.1 Add `browneye-base` meta spec = the r13.1 chapter 8 **systemd
      variant** (80 packages) **plus** `browneye-basefs`, `browneye-sysconfig`,
      `browneye-release`.
- [ ] 1.12.2 `createrepo_c ~/browneye/build/repo` (needs the `createrepo_c` spec,
      see 2.1.2).
- [ ] 1.12.3 Dependency closure: `rpm -qpR` over all base RPMs; every require must
      resolve inside the set (or be documented as host/glibc-symbol exceptions).
- [ ] 1.12.4 Checksum/sign artifacts for reproducibility.

### 1.13 Item 1 acceptance

- [ ] 1.13.1 Install the base set into a clean rootfs (see 2.3).
- [ ] 1.13.2 Boot in QEMU with the host kernel; verify systemd reaches
      `multi-user.target`, udev creates device nodes, journald logs, login shell works.
- [ ] 1.13.3 Record the package set + versions as `build/base-manifest.json`.

---

## 2. Item 2 — Base build container

Purpose: once the base RPMs exist, build a container **from those RPMs** and use it
to upgrade the remaining (non-base) specs with the target toolchain.

### 2.1 Missing bootstrap specs

- [ ] 2.1.1 `rpm-build` — split from `rpm.spec` (4.18.1) or new spec: `rpmbuild`,
      `/usr/lib/rpm/{brp-*,macros,...}`, platform macros.
- [ ] 2.1.2 `createrepo_c` — new spec (needed for the local repo).
- [ ] 2.1.3 `python3` alias — current spec is named `python`; add
      `Provides: python3` and `%{_bindir}/python3`.
- [ ] 2.1.4 `browneye-rpm-config` — package `rpmsupport/rpmmacros`,
      `strip_debug.sh`, and the minimal `%__spec_install_post` (no Fedora `brp-*`
      paths), so `rpmbuild` works inside the container.
- [ ] 2.1.5 Verify `rpm` 4.18.1 and `dnf` 4.16.2 still work with the r13.1-era
      toolchain inside the target.

### 2.2 Build the local repo

- [ ] 2.2.1 `createrepo_c --database ~/browneye/build/repo` after 1.12.
- [ ] 2.2.2 Write `build/repo/browneye.repo` with `baseurl=file:///repo`.
- [ ] 2.2.3 Snapshot per build (`repo-r13.1-<date>`).

### 2.3 Assemble the rootfs

- [ ] 2.3.1
      ```bash
      dnf -y --installroot ~/browneye/build/rootfs --releasever=13.1 \
          --disablerepo='*' --repofrompath=browneye,file://$HOME/browneye/build/repo \
          --setopt=install_weak_deps=False install browneye-base
      ```
- [ ] 2.3.2 Post-install bits that cannot live in RPMs: `machine-id`,
      `resolv.conf`, and `systemctl preset-all`/unit enablement if not handled by
      the sysconfig package.
- [ ] 2.3.3 Clean dnf caches and logs; strip debug if needed.
- [ ] 2.3.4 `tar -C build/rootfs -czf build/browneye-rootfs.tar.gz .`
      (Containerfile input).

### 2.4 Container image

- [ ] 2.4.1 Rewrite `Containerfile` (podman-compatible):
      ```dockerfile
      FROM scratch
      ADD build/browneye-rootfs.tar.gz /
      ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
      ENV container=podman
      ENV LANG=C.UTF-8
      WORKDIR /build
      CMD ["/bin/bash"]
      ```
- [ ] 2.4.2 `podman build -t browneye/base:r13.1-<date> -f Containerfile .`
- [ ] 2.4.3 Labels: `org.browneye.lfs-tag=r13.1`,
      `org.browneye.lfs-commit=71ef60ba…`, `org.browneye.base-manifest`.
- [ ] 2.4.4 Document Docker consumption (`podman save | docker load`, or build with
      `docker build`).

### 2.5 In-container build tooling

- [ ] 2.5.1 Include in `browneye-base` (or a `browneye-build` meta):
      `gcc g++ make binutils patch diffutils tar gzip bzip2 xz zstd findutils grep
      sed gawk m4 bison flex perl python3 pkgconf ncurses readline zlib openssl
      rpm rpm-build dnf createrepo_c git curl wget`.
- [ ] 2.5.2 `/etc/dnf/dnf.conf` with `install_weak_deps=False`.
- [ ] 2.5.3 Point dnf at the mounted host repo (or bake a copy at `/repo`).
- [ ] 2.5.4 Ship `bbuild` + `builder/` at `/build` (bind mount in dev).
- [ ] 2.5.5 Set `container=podman` so systemd's container detection and
      `systemd-firstboot` stay out of the way in the image.

### 2.6 Build wrapper

- [ ] 2.6.1 `scripts/container_build.sh`:
      ```bash
      podman run --rm -it \
        -v "$HOME/browneye":/build -w /build \
        browneye/base:r13.1-<date> \
        ./bbuild build "$1"
      ```
- [ ] 2.6.2 `scripts/container_shell.sh` for interactive iteration.
- [ ] 2.6.3 Per-build logs in `build/logs/<pkg>.log`.

### 2.7 Smoke test

- [ ] 2.7.1 Build a non-base package inside the container (e.g. `glib`).
- [ ] 2.7.2 `rpm -Uvh --test` and link check inside the container.
- [ ] 2.7.3 `podman run … rpm --eval '%_libdir'` returns `/usr/lib64`.

### 2.8 Workflow for the remaining specs

- [ ] 2.8.1 Define the outer upgrade order from the repo dependency graph.
- [ ] 2.8.2 Per package: edit spec on host → `container_build.sh <pkg>` →
      install result in a scratch container → commit.
- [ ] 2.8.3 Keep `build/status.tsv` (`pkg`, `old`, `new`, `built`, `installed`,
      `blocked-by`).
- [ ] 2.8.4 Periodically re-run `createrepo_c` and refresh the base image.

### 2.9 Reproducibility and versioning

- [ ] 2.9.1 Tag every image `r13.1-<date>` (plus commit short hash).
- [ ] 2.9.2 Bake `base-manifest.json` + `status.tsv` into
      `/usr/share/browneye/`.
- [ ] 2.9.3 Document rebuild steps in `docs/BUILDING.md`.

---

## 3. Cross-cutting

### 3.1 Validation matrix

| Gate | Check |
|---|---|
| Spec builds | `rpmbuild -bb` exit 0, no unpackaged files |
| Contents | `rpm -qpl`: no stray `/usr/lib`, no host paths, no `%{buildroot}` |
| Deps | every `rpm -qpR` require resolves in the base repo |
| Install | install into `--installroot`, `chroot` smoke commands |
| Boot | QEMU boot; systemd reaches `multi-user.target`, udev + journald active |
| Container | non-base spec builds inside `browneye/base` |

### 3.2 Risks

- **systemd 261.2 is a large build** — meson + dbus (meson) + markupsafe/jinja2
  must all be in place first; it is the single most dependency-heavy step in Wave E.
- **dbus moved to meson** in r13.1 — the old autotools spec cannot be reused;
  rewrite `%build`, `%install`, and `%files`.
- **`/usr/lib64` divergence** — every LFS `--libdir=/usr/lib` must be adapted,
  and glibc's `libc_cv_slibdir` must be `/usr/lib64`; a missed one installs into
  the wrong tree and breaks the loader.
- **RPM scriptlets** — 16 `%post` blocks; audit before installing into a rootfs
  (systemd packages want `systemctl`/`journalctl` calls that must be guarded in a
  build root).
- **Host toolchain mismatch** — gcc 16.2.1 host vs 16.2.0 target is close;
  binutils 2.46 host vs 2.47 target may surface link issues. The container removes
  this variable for the outer upgrades.
- **Item 2 chicken-and-egg** — the container needs `rpmbuild`/`dnf` to build more
  packages; solved by 2.1 and proven by 2.7.
- **Long builds** — gcc (`--enable-targets=all`), Python (`--enable-optimizations`),
  LLVM; schedule separately.
- **Patch hosting** — vendor patches; r13.1 patch URLs are version-scoped.
- **Tests as root** — coreutils/gcc suites need an unprivileged user; keep `%check`
  optional in rpmbuild.
- **Stale init specs** — retiring finit/libite/libuev/sysklogd/udev must not break
  `discover_packages()` or dependencies of later desktop packages.

### 3.3 Resolved decisions

| Question | Answer |
|---|---|
| Init system | systemd 261.2 (book's systemd variant) |
| Library layout | `/usr/lib64` |
| Kernel in phase 1 | No — phase 2 |
| Build scope | Chapter 8 on the host toolchain |
| LFS pin | r13.1 tag (`71ef60ba`) |

### 3.4 Still open

1. Container contents: include `dnf`/`rpm` for in-container builds (planned), or
   keep a pure runtime image and build on the host?
2. Retire vs keep the old init specs (`finit`, `libite`, `libuev`, `sysklogd`,
   `eudev`, `udev`): mark `.disabled` in place or move to `package_specs/attic/`?
3. `glibc-locales`: separate subpackage (planned) or bundled with glibc?

---

## 4. Directory layout (after Item 2)

```
~/browneye/
├── bbuild
├── builder/
├── package_specs/
├── rpmsupport/
├── scripts/
│   ├── container_build.sh
│   ├── container_shell.sh
│   └── build_rootfs.sh
├── iso/
├── docs/BUILDING.md
├── lfs.lock
├── plan.md
└── build/
    ├── repo/                  # createrepo_c output
    ├── rootfs/                # assembled base rootfs
    ├── browneye-rootfs.tar.gz
    ├── logs/
    ├── status.tsv
    └── base-manifest.json
```
