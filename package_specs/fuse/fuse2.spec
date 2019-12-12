Name:       fuse2
Version:    2.9.7
Release:    1
Summary:    FUSE (Filesystem in Userspace)
License:    GPL
Source0:    fuse-%{version}.tar.gz
Prefix:     /usr

%description
FUSE (Filesystem in Userspace)

%prep
%setup -n fuse-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/etc/init.d/fuse
/etc/udev/rules.d/99-fuse.rules
/sbin/mount.fuse
/usr/bin/fusermount
/usr/bin/ulockmgr_server
/usr/include/fuse.h
/usr/include/fuse/cuse_lowlevel.h
/usr/include/fuse/fuse.h
/usr/include/fuse/fuse_common.h
/usr/include/fuse/fuse_common_compat.h
/usr/include/fuse/fuse_compat.h
/usr/include/fuse/fuse_lowlevel.h
/usr/include/fuse/fuse_lowlevel_compat.h
/usr/include/fuse/fuse_opt.h
/usr/include/ulockmgr.h
/usr/lib64/libfuse.a
/usr/lib64/libfuse.la
/usr/lib64/libfuse.so
/usr/lib64/libfuse.so.2
/usr/lib64/libfuse.so.2.9.7
/usr/lib64/libulockmgr.a
/usr/lib64/libulockmgr.la
/usr/lib64/libulockmgr.so
/usr/lib64/libulockmgr.so.1
/usr/lib64/libulockmgr.so.1.0.1
/usr/lib64/pkgconfig/fuse.pc
/usr/share/man/man1/fusermount.1.gz
/usr/share/man/man1/ulockmgr_server.1.gz
/usr/share/man/man8/mount.fuse.8.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.9.7
- Initial RPM

