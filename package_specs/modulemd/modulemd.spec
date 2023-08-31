Name:       modulemd
Version:    2.15.0
Release:    1
Summary:    C Library for manipulating module metadata files 
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
C Library for manipulating module metadata files 

%prep
%setup

%build
mkdir build
pushd build
meson setup --prefix=/usr \
            -Dwith_docs=false \
            ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/modulemd-validator
/usr/include/modulemd-2.0/
/usr/lib/
/usr/share/

%changelog
* Thu Aug 31 2023 Chris Statzer <chris.statzer@gmail.com> 2.15.0
- Version bump

* Wed May 13 2020 Chris Statzer <chris.statzer@qq.com> 2.9.3
- Update of library to current stable

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.8.16
- Initial RPM

