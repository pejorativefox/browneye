Name:       glib
Version:    2.77.2
Release:    1
Summary:    Glib low level system libraries
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides:   pkgconfig(glib-2.0)
Provides:   pkgconfig(gobject-2.0)
Provides:   pkgconfig(gmodule-2.0)
Provides:   pkgconfig(gmodule-no-export-2.0)
Provides:   pkgconfig(gio-unix-2.0)
Provides:   pkgconfig(gio-2.0)
Provides:   pkgconfig(gthread-2.0)

%description
GLib is a bundle of three low-level system libraries written in C and developed mainly by GNOME.

%prep
%setup -a 0

%build
mkdir build-glib
pushd build-glib

meson --prefix=/usr      \
      -Dman=false        \
      -Dselinux=disabled \
      --buildtype=release \
      ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-glib
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files -f ../../SOURCES/glib.filelist

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 2.77.2
- Version bump 
