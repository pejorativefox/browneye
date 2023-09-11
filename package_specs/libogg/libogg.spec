Name:       libogg
Version:    1.3.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -q

%build
%configure  --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/libogg-1.3.3
%make_build

%install    
rm -rf %{buildroot}
%make_install

%files
/usr/include/ogg/config_types.h
/usr/include/ogg/ogg.h
/usr/include/ogg/os_types.h
/usr/lib64/libogg.so
/usr/lib64/libogg.so.0
/usr/lib64/libogg.so.0.8.3
/usr/lib64/pkgconfig/ogg.pc
/usr/share/aclocal/ogg.m4
/usr/share/doc/libogg-1.3.3/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.3.3-1
- Version bump

