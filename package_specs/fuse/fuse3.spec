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
#pushd build
#DESTDIR=%{buildroot} ninja install
#popd
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
ls -lash
install -m 0755 build/lib/libfuse3.so.%{version} %{buildroot}/%{_libdir}
#install -m 0755 build/lib/libulockmgr.so.1.0.1 %{buildroot}/%{_libdir}
install -p ./build/meson-private/fuse3.pc %{buildroot}/%{_libdir}/pkgconfig/
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 ./build/util/fusermount3 %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 ./build/util/mount.fuse3 %{buildroot}/%{_sbindir}
#install -m 0755 ./build/util/ulockmgr_server %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_includedir}/fuse
install -p ./include/fuse.h %{buildroot}/%{_includedir}/
#install -p ./build/include/ulockmgr.h %{buildroot}/%{_includedir}/
	
for i in cuse_lowlevel.h fuse_common.h  fuse_kernel.h  fuse_lowlevel.h  fuse_opt.h; do
	install -p include/$i %{buildroot}/%{_includedir}/fuse/
done
#mkdir -p %{buildroot}/%{_mandir}/man1/
#cp -a doc/fusermount.1 doc/ulockmgr_server.1 %{buildroot}/%{_mandir}/man1/
#mkdir -p %{buildroot}/%{_mandir}/man8/
#cp -a doc/mount.fuse.8 %{buildroot}/%{_mandir}/man8/
	
pushd %{buildroot}/%{_libdir}
ln -s libfuse.so.%{version} libfuse.so.2
ln -s libfuse.so.%{version} libfuse.so
ln -s libulockmgr.so.1.0.1 libulockmgr.so.1
ln -s libulockmgr.so.1.0.1 libulockmgr.so
popd
	
 
	
# Get rid of static libs
	
rm -f %{buildroot}/%{_libdir}/*.a

%files
/usr/bin/fusermount3
/usr/include/fuse.h
/usr/include/fuse/
/usr/lib64/libfuse.so
/usr/lib64/libfuse.so.2
/usr/lib64/libfuse3.so.3.2.5
/usr/lib64/libulockmgr.so
/usr/lib64/libulockmgr.so.1
/usr/lib64/pkgconfig/fuse3.pc
/usr/sbin/mount.fuse3

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM

