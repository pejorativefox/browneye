Name:       drpm
Version:    0.4.1
Release:    1
Summary:    A library for making, reading and applying deltarpm packages
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
A library for making, reading and applying deltarpm packages

%prep
%setup

%build
mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DENABLE_TESTS=0 ..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/include/drpm.h
/usr/lib64/libdrpm.so
/usr/lib64/libdrpm.so.0
/usr/lib64/libdrpm.so.0.4.1
/usr/lib64/pkgconfig/drpm.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.4.1
- Initial RPM

