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
/usr/lib/
/usr/libexec/installed-tests/pango/*
/usr/share/

%changelog
# let's skip this for now

