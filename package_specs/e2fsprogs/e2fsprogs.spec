Name:       e2fsprogs
Version:    1.47.0
Release:    1
Summary:    ext filesystem utilities
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The E2fsprogs package contains the utilities for handling the ext2 file system. It also supports the ext3 and ext4 journaling file systems. 

%prep
%setup -q

%build
mkdir -pv build
pushd build
../configure --prefix=/usr           \
             --libdir=%{_libdir}     \
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
rm -fv %{buildroot}/usr/lib/{libcom_err,libe2p,libext2fs,libss}.a
popd

rm -vf %{buildroot}%{_infodir}/dir*
chmod +w %{buildroot}/usr/lib64/*.a

%files
/usr/bin/chattr
/usr/bin/compile_et
/usr/bin/lsattr
/usr/bin/mk_cmds
/usr/etc/e2scrub.conf
/usr/etc/mke2fs.conf
/usr/lib/udev/rules.d/96-e2scrub.rules
/usr/lib64/e2initrd_helper
/usr/lib64/libcom_err.a
/usr/lib64/libcom_err.so
/usr/lib64/libcom_err.so.2
/usr/lib64/libcom_err.so.2.1
/usr/lib64/libe2p.a
/usr/lib64/libe2p.so
/usr/lib64/libe2p.so.2
/usr/lib64/libe2p.so.2.3
/usr/lib64/libext2fs.a
/usr/lib64/libext2fs.so
/usr/lib64/libext2fs.so.2
/usr/lib64/libext2fs.so.2.4
/usr/lib64/libss.a
/usr/lib64/libss.so
/usr/lib64/libss.so.2
/usr/lib64/libss.so.2.0
/usr/lib64/pkgconfig/com_err.pc
/usr/lib64/pkgconfig/e2p.pc
/usr/lib64/pkgconfig/ext2fs.pc
/usr/lib64/pkgconfig/ss.pc
/usr/sbin/badblocks
/usr/sbin/debugfs
/usr/sbin/dumpe2fs
/usr/sbin/e2fsck
/usr/sbin/e2image
/usr/sbin/e2label
/usr/sbin/e2mmpstatus
/usr/sbin/e2scrub
/usr/sbin/e2scrub_all
/usr/sbin/e2undo
/usr/sbin/fsck.ext2
/usr/sbin/fsck.ext3
/usr/sbin/fsck.ext4
/usr/sbin/logsave
/usr/sbin/mke2fs
/usr/sbin/mkfs.ext2
/usr/sbin/mkfs.ext3
/usr/sbin/mkfs.ext4
/usr/sbin/resize2fs
/usr/sbin/tune2fs
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
/usr/sbin/e2freefrag
/usr/sbin/e4crypt
/usr/sbin/e4defrag
/usr/sbin/filefrag
/usr/sbin/mklost+found
/usr/share/et/et_c.awk
/usr/share/et/et_h.awk
/usr/share/info/libext2fs.info.gz
/usr/share/locale/
/usr/share/man/
/usr/share/ss/ct_c.awk
/usr/share/ss/ct_c.sed

%changelog
# let's skip this for now
