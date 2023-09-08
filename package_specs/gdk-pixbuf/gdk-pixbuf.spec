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

%prep
%setup -q

%build
mkdir build-pb
pushd build-pb

meson setup --prefix=/usr -Dman=false \
      -Dgtk_doc=false --buildtype=release \
      --wrap-mode=nofallback \
      ..
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
/usr/bin/gdk-pixbuf-csource
/usr/bin/gdk-pixbuf-pixdata
/usr/bin/gdk-pixbuf-query-loaders
/usr/bin/gdk-pixbuf-thumbnailer
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-bmp.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-gif.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ico.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.so
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.so
/usr/lib64/girepository-1.0/GdkPixbuf-2.0.typelib
/usr/lib64/girepository-1.0/GdkPixdata-2.0.typelib
/usr/lib64/libgdk_pixbuf-2.0.so
/usr/lib64/libgdk_pixbuf-2.0.so.0
/usr/lib64/libgdk_pixbuf-2.0.so.0.4200.9
/usr/lib64/pkgconfig/gdk-pixbuf-2.0.pc
/usr/share/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer
/usr/libexec/installed-tests/gdk-pixbuf/
/usr/share/gir-1.0/GdkPixbuf-2.0.gir
/usr/share/gir-1.0/GdkPixdata-2.0.gir
/usr/share/installed-tests/
/usr/include/gdk-pixbuf-2.0/
/usr/share/locale/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 2.42.9
- Version bump
