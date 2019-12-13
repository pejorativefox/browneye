Name:       e2fsprogs
Version:    1.44.5
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
mkdir -pv build
pushd build
../configure --prefix=/usr           \
             --bindir=/bin           \
             --with-root-prefix=""   \
             --enable-elf-shlibs     \
             --disable-libblkid      \
             --disable-libuuid       \
             --disable-uuidd         \
             --disable-fsck
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
make install-libs DESTDIR=$RPM_BUILD_ROOT
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/bin/chattr
/bin/compile_et
/bin/lsattr
/bin/mk_cmds
/etc/mke2fs.conf
/lib/libcom_err.so.2
/lib/libcom_err.so.2.1
/lib/libe2p.so.2
/lib/libe2p.so.2.3
/lib/libext2fs.so.2
/lib/libext2fs.so.2.4
/lib/libss.so.2
/lib/libss.so.2.0
/sbin/badblocks
/sbin/debugfs
/sbin/dumpe2fs
/sbin/e2fsck
/sbin/e2image
/sbin/e2label
/sbin/e2mmpstatus
/sbin/e2undo
/sbin/fsck.ext2
/sbin/fsck.ext3
/sbin/fsck.ext4
/sbin/logsave
/sbin/mke2fs
/sbin/mkfs.ext2
/sbin/mkfs.ext3
/sbin/mkfs.ext4
/sbin/resize2fs
/sbin/tune2fs
/usr/include/com_err.h
/usr/include/e2p/e2p.h
/usr/include/et/com_err.h
/usr/include/ext2fs/bitops.h
/usr/include/ext2fs/ext2_err.h
/usr/include/ext2fs/ext2_ext_attr.h
/usr/include/ext2fs/ext2_fs.h
/usr/include/ext2fs/ext2_io.h
/usr/include/ext2fs/ext2_types.h
/usr/include/ext2fs/ext2fs.h
/usr/include/ext2fs/ext3_extents.h
/usr/include/ext2fs/hashmap.h
/usr/include/ext2fs/qcow2.h
/usr/include/ext2fs/tdb.h
/usr/include/ss/ss.h
/usr/include/ss/ss_err.h
/usr/lib/e2initrd_helper
/usr/lib/libcom_err.a
/usr/lib/libcom_err.so
/usr/lib/libe2p.a
/usr/lib/libe2p.so
/usr/lib/libext2fs.a
/usr/lib/libext2fs.so
/usr/lib/libss.a
/usr/lib/libss.so
/usr/lib/pkgconfig/com_err.pc
/usr/lib/pkgconfig/e2p.pc
/usr/lib/pkgconfig/ext2fs.pc
/usr/lib/pkgconfig/ss.pc
/usr/sbin/e2freefrag
/usr/sbin/e4crypt
/usr/sbin/e4defrag
/usr/sbin/filefrag
/usr/sbin/mklost+found
/usr/share/et/et_c.awk
/usr/share/et/et_h.awk
/usr/share/info/libext2fs.info.gz
/usr/share/locale/ca/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/cs/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/da/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/de/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/eo/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/es/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/fi/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/fr/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/hu/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/id/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/it/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/ms/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/nl/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/pl/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/sr/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/sv/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/tr/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/uk/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/vi/LC_MESSAGES/e2fsprogs.mo
/usr/share/locale/zh_CN/LC_MESSAGES/e2fsprogs.mo
/usr/share/man/man1/chattr.1.gz
/usr/share/man/man1/compile_et.1.gz
/usr/share/man/man1/lsattr.1.gz
/usr/share/man/man1/mk_cmds.1.gz
/usr/share/man/man3/com_err.3.gz
/usr/share/man/man5/e2fsck.conf.5.gz
/usr/share/man/man5/ext2.5.gz
/usr/share/man/man5/ext3.5.gz
/usr/share/man/man5/ext4.5.gz
/usr/share/man/man5/mke2fs.conf.5.gz
/usr/share/man/man8/badblocks.8.gz
/usr/share/man/man8/debugfs.8.gz
/usr/share/man/man8/dumpe2fs.8.gz
/usr/share/man/man8/e2freefrag.8.gz
/usr/share/man/man8/e2fsck.8.gz
/usr/share/man/man8/e2image.8.gz
/usr/share/man/man8/e2label.8.gz
/usr/share/man/man8/e2mmpstatus.8.gz
/usr/share/man/man8/e2undo.8.gz
/usr/share/man/man8/e4crypt.8.gz
/usr/share/man/man8/e4defrag.8.gz
/usr/share/man/man8/filefrag.8.gz
/usr/share/man/man8/fsck.ext2.8.gz
/usr/share/man/man8/fsck.ext3.8.gz
/usr/share/man/man8/fsck.ext4.8.gz
/usr/share/man/man8/logsave.8.gz
/usr/share/man/man8/mke2fs.8.gz
/usr/share/man/man8/mkfs.ext2.8.gz
/usr/share/man/man8/mkfs.ext3.8.gz
/usr/share/man/man8/mkfs.ext4.8.gz
/usr/share/man/man8/mklost+found.8.gz
/usr/share/man/man8/resize2fs.8.gz
/usr/share/man/man8/tune2fs.8.gz
/usr/share/ss/ct_c.awk
/usr/share/ss/ct_c.sed
/usr/sbin/fuse2fs
/usr/share/man/man1/fuse2fs.1.gz

%changelog
# let's skip this for now
