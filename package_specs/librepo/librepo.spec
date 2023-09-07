Name:       librepo
Version:    1.15.2
Release:    1
Summary:    A library providing C and Python (libcURL like) API for downloading packages.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
A library providing C and Python (libcURL like) API for downloading packages.

%prep
%setup

%build
mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DENABLE_DOCS=0 ..
%make_build 
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/lib64/librepo.so
/usr/lib64/librepo.so.0
/usr/lib64/pkgconfig/librepo.pc
/usr/include/librepo/
/usr/lib64/python3.11/site-packages/librepo/

%changelog
* Thu Aug 31 2023 Chris Statzer <chris.statzer@gmail.com> 1.15.2
- Version bump

* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 1.11.0-2
- Updated build to use python3

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.11.0-1
- Initial RPM

