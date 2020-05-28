Name:       librepo
Version:    1.11.0
Release:    2
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
/usr/include/
/usr/lib64/librepo.so
/usr/lib64/librepo.so.0
/usr/lib64/pkgconfig/librepo.pc
/usr/lib/python3.7/site-packages/librepo/__init__.py
/usr/lib/python3.7/site-packages/librepo/_librepo.so

%changelog
* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 1.11.0-2
- Updated build to use python3

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.11.0-1
- Initial RPM

