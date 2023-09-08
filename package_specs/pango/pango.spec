Name:       pango
Version:    1.50.14
Release:    1
Summary:    text layout library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

BuildRequires: fontconfig >= 2.13.1
BuildRequires: fribidi >= 1.0.13
BuildRequires: glib >= 2.76.4

Provides: pkgconfig(pango)
Provides: pkgconfig(pangocairo)
Provides: pkgconfig(pangoft2)

%description
Pango is a library for laying out and rendering text

%prep
%setup -q

%build
mkdir build-glib
pushd build-glib

meson --prefix=/usr --sysconfdir=/etc ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-glib
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/pango-list
/usr/bin/pango-view
/usr/bin/pango-segmentation
/usr/lib64/girepository-1.0/Pango-1.0.typelib
/usr/lib64/girepository-1.0/PangoCairo-1.0.typelib
/usr/lib64/girepository-1.0/PangoFT2-1.0.typelib
/usr/lib64/girepository-1.0/PangoFc-1.0.typelib
/usr/lib64/girepository-1.0/PangoOT-1.0.typelib
/usr/lib64/libpango-1.0.so
/usr/lib64/libpango-1.0.so.0
/usr/lib64/libpango-1.0.so.0.5000.14
/usr/lib64/libpangocairo-1.0.so
/usr/lib64/libpangocairo-1.0.so.0
/usr/lib64/libpangocairo-1.0.so.0.5000.14
/usr/lib64/libpangoft2-1.0.so
/usr/lib64/libpangoft2-1.0.so.0
/usr/lib64/libpangoft2-1.0.so.0.5000.14
/usr/lib64/pkgconfig/pango.pc
/usr/lib64/pkgconfig/pangocairo.pc
/usr/lib64/pkgconfig/pangofc.pc
/usr/lib64/pkgconfig/pangoft2.pc
/usr/lib64/pkgconfig/pangoot.pc
/usr/share/gir-1.0/Pango-1.0.gir
/usr/share/gir-1.0/PangoCairo-1.0.gir
/usr/share/gir-1.0/PangoFT2-1.0.gir
/usr/share/gir-1.0/PangoFc-1.0.gir
/usr/share/gir-1.0/PangoOT-1.0.gir
/usr/include/pango-1.0/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.50.14-1
- Version bump
