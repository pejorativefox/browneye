Name:       modulemd
Version:    2.9.3
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
meson    --prefix=/usr \
         -Dwith_docs=false \
         -Dskip_formatters=true \
         -Dskip_introspection=true \
         -Ddeveloper_build=false ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/modulemd-validator
/usr/include/modulemd-2.0/*
/usr/lib/libmodulemd.so
/usr/lib/libmodulemd.so.2
/usr/lib/libmodulemd.so.2.9.3
/usr/lib/pkgconfig/modulemd-2.0.pc
/usr/lib/python3.7/site-packages/gi/overrides/Modulemd.py
/usr/share/man/man1/modulemd-validator.1.gz

%changelog
* Wed May 13 2020 Chris Statzer <chris.statzer@qq.com> 2.9.3
- Update of library to current stable

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.8.16
- Initial RPM

