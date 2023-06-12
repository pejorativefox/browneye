Name:       fuse
Version:    3.2.5
Release:    1
Summary:    FUSE (Filesystem in Userspace)
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
FUSE (Filesystem in Userspace)

%prep
%setup

%build
mkdir build
pushd build
meson --prefix=/usr ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/etc/fuse.conf
/etc/init.d/fuse3
/lib/udev/rules.d/99-fuse3.rules
/usr/bin/fusermount3
/usr/include/fuse3/
/usr/lib/libfuse3.so
/usr/lib/libfuse3.so.3
/usr/lib/libfuse3.so.3.2.5
/usr/lib/pkgconfig/fuse3.pc
/usr/sbin/mount.fuse3
/usr/share/man/man1/fusermount3.1.gz
/usr/share/man/man8/mount.fuse3.8.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM

