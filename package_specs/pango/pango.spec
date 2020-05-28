Name:       pango
Version:    1.42.4
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(pango)
Provides: pkgconfig(pangocairo)
Provides: pkgconfig(pangoft2)

%description
TODO

%prep
%setup -a 0

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
/usr/include/pango-1.0/*
/usr/lib/girepository-1.0/Pango-1.0.typelib
/usr/lib/girepository-1.0/PangoCairo-1.0.typelib
/usr/lib/girepository-1.0/PangoFT2-1.0.typelib
/usr/lib/girepository-1.0/PangoXft-1.0.typelib
/usr/lib/libpango-1.0.so
/usr/lib/libpango-1.0.so.0
/usr/lib/libpango-1.0.so.0.4200.3
/usr/lib/libpangocairo-1.0.so
/usr/lib/libpangocairo-1.0.so.0
/usr/lib/libpangocairo-1.0.so.0.4200.3
/usr/lib/libpangoft2-1.0.so
/usr/lib/libpangoft2-1.0.so.0
/usr/lib/libpangoft2-1.0.so.0.4200.3
/usr/lib/libpangoxft-1.0.so
/usr/lib/libpangoxft-1.0.so.0
/usr/lib/libpangoxft-1.0.so.0.4200.3
/usr/lib/pkgconfig/pango.pc
/usr/lib/pkgconfig/pangocairo.pc
/usr/lib/pkgconfig/pangoft2.pc
/usr/lib/pkgconfig/pangoxft.pc
/usr/libexec/installed-tests/pango/*
/usr/share/gir-1.0/Pango-1.0.gir
/usr/share/gir-1.0/PangoCairo-1.0.gir
/usr/share/gir-1.0/PangoFT2-1.0.gir
/usr/share/gir-1.0/PangoXft-1.0.gir
/usr/share/installed-tests/pango/*
/usr/share/man/man1/pango-view.1.gz

%changelog
# let's skip this for now

