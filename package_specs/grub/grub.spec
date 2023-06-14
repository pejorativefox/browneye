Name:       grub
Version:    2.06
Release:    1
Summary:    GNU GRUB is a Multiboot boot loader.
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

Patch: grub-2.06-upstream_fixes-1.patch

%description
GNU GRUB is a Multiboot boot loader. It was derived from GRUB, the GRand Unified Bootloader, which was originally designed and implemented by Erich Stefan Boleyn.

%prep
%setup -q -a0
%patch -p1

%build

%configure  --prefix=/usr        \
            --sysconfdir=/etc    \
            --disable-efiemu     \
            --enable-grub-mkfont \
            --with-platform=efi  \
            --target=x86_64      \
            --disable-werror

%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/usr/share/bash-completion/completions
mv -v %{buildroot}/etc/bash_completion.d/grub %{buildroot}/usr/share/bash-completion/completions

%files
/etc/grub.d/
/usr/bin/grub-*
/usr/lib64/grub/x86_64-efi/
/usr/sbin/grub-bios-setup
/usr/sbin/grub-install
/usr/sbin/grub-macbless
/usr/sbin/grub-mkconfig
/usr/sbin/grub-ofpathname
/usr/sbin/grub-probe
/usr/sbin/grub-reboot
/usr/sbin/grub-set-default
/usr/sbin/grub-sparc64-setup
/usr/share/bash-completion/completions/grub
/usr/share/grub/grub-mkconfig_lib
/usr/share/info/
/usr/share/locale/ 
/usr/share/man/

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 2.06-1
- Updating grub to allow a clean patch to fix a bug: https://wiki.linuxfromscratch.org/lfs/ticket/4354

* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 2.02-2
- Added UEFI support to build
