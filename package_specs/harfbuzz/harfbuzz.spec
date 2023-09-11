Name:       harfbuzz
Version:    8.1.1
Release:    1
Summary:    Text shaping engine
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(harfbuzz)

%description
The HarfBuzz package contains an OpenType text shaping engine.

%prep
%setup -q

%build
%configure  --disable-static --with-gobject
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/hb-info
/usr/bin/hb-ot-shape-closure
/usr/bin/hb-shape
/usr/bin/hb-subset
/usr/bin/hb-view
/usr/lib64/cmake/harfbuzz/harfbuzz-config.cmake
/usr/lib64/girepository-1.0/HarfBuzz-0.0.typelib
/usr/lib64/libharfbuzz-cairo.so
/usr/lib64/libharfbuzz-cairo.so.0
/usr/lib64/libharfbuzz-cairo.so.0.60811.0
/usr/lib64/libharfbuzz-gobject.so
/usr/lib64/libharfbuzz-gobject.so.0
/usr/lib64/libharfbuzz-gobject.so.0.60811.0
/usr/lib64/libharfbuzz-subset.so
/usr/lib64/libharfbuzz-subset.so.0
/usr/lib64/libharfbuzz-subset.so.0.60811.0
/usr/lib64/libharfbuzz.so
/usr/lib64/libharfbuzz.so.0
/usr/lib64/libharfbuzz.so.0.60811.0
/usr/lib64/pkgconfig/harfbuzz-cairo.pc
/usr/lib64/pkgconfig/harfbuzz-gobject.pc
/usr/lib64/pkgconfig/harfbuzz-subset.pc
/usr/lib64/pkgconfig/harfbuzz.pc
/usr/share/gir-1.0/HarfBuzz-0.0.gir
/usr/include/harfbuzz/
/usr/share/gtk-doc/html/harfbuzz/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 8.1.1-1
- Version bump
