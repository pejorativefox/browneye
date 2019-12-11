Name:       librsvg
Version:    2.44.12
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup

%build
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/rsvg-convert
/usr/bin/rsvg-view-3
/usr/include/librsvg-2.0/librsvg/librsvg-enum-types.h
/usr/include/librsvg-2.0/librsvg/librsvg-features.h
/usr/include/librsvg-2.0/librsvg/rsvg-cairo.h
/usr/include/librsvg-2.0/librsvg/rsvg.h
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.la
/usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.so
/usr/lib64/girepository-1.0/Rsvg-2.0.typelib
/usr/lib64/librsvg-2.la
/usr/lib64/librsvg-2.so
/usr/lib64/librsvg-2.so.2
/usr/lib64/librsvg-2.so.2.44.12
/usr/lib64/pkgconfig/librsvg-2.0.pc
/usr/share/doc/librsvg/COMPILING.md
/usr/share/doc/librsvg/CONTRIBUTING.md
/usr/share/doc/librsvg/README.md
/usr/share/doc/librsvg/code-of-conduct.md
/usr/share/gir-1.0/Rsvg-2.0.gir
/usr/share/gtk-doc/html/rsvg-2.0/annotation-glossary.html
/usr/share/gtk-doc/html/rsvg-2.0/api-index-full.html
/usr/share/gtk-doc/html/rsvg-2.0/ch01.html
/usr/share/gtk-doc/html/rsvg-2.0/home.png
/usr/share/gtk-doc/html/rsvg-2.0/index.html
/usr/share/gtk-doc/html/rsvg-2.0/left-insensitive.png
/usr/share/gtk-doc/html/rsvg-2.0/left.png
/usr/share/gtk-doc/html/rsvg-2.0/licence.html
/usr/share/gtk-doc/html/rsvg-2.0/object-tree.html
/usr/share/gtk-doc/html/rsvg-2.0/right-insensitive.png
/usr/share/gtk-doc/html/rsvg-2.0/right.png
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-2.0.devhelp2
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-RsvgHandle.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-Using-RSVG-with-GIO.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-Using-RSVG-with-GdkPixbuf.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-Using-RSVG-with-cairo.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg-Version-check-and-feature-tests.html
/usr/share/gtk-doc/html/rsvg-2.0/rsvg.html
/usr/share/gtk-doc/html/rsvg-2.0/style.css
/usr/share/gtk-doc/html/rsvg-2.0/up-insensitive.png
/usr/share/gtk-doc/html/rsvg-2.0/up.png
/usr/share/man/man1/rsvg-convert.1.gz
/usr/share/thumbnailers/librsvg.thumbnailer

%changelog
# let's skip this for now

