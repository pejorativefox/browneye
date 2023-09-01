Name:       gdk-pixbuf
Version:    2.42.9
Release:    1
Summary:    Image loading library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(gdk-pixbuf-2.0)
Requires: librsvg

%description
GdkPixbuf is a library that loads image data in various formats and stores it as linear buffers in memory.

Requires: librsvg

%prep
%setup -a 0

%build
mkdir build-pb
pushd build-pb

meson --prefix=/usr -Dman=false -Dgtk_doc=false ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-pb
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%post
update-mime-database /usr/share/mime
gdk-pixbuf-query-loaders --update-cache


%files
/usr/bin/
/usr/include/gdk-pixbuf-2.0/
/usr/lib/
/usr/libexec/
/usr/share/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 2.42.9
- Version bump
