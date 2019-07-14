Name:       libcroco
Version:    0.6.12
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -a 0

%build
%configure  --disable-static --enable-tee
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/croco-0.6-config
/usr/bin/csslint-0.6
/usr/include/libcroco-0.6/libcroco/cr-additional-sel.h
/usr/include/libcroco-0.6/libcroco/cr-attr-sel.h
/usr/include/libcroco-0.6/libcroco/cr-cascade.h
/usr/include/libcroco-0.6/libcroco/cr-declaration.h
/usr/include/libcroco-0.6/libcroco/cr-doc-handler.h
/usr/include/libcroco-0.6/libcroco/cr-enc-handler.h
/usr/include/libcroco-0.6/libcroco/cr-fonts.h
/usr/include/libcroco-0.6/libcroco/cr-input.h
/usr/include/libcroco-0.6/libcroco/cr-num.h
/usr/include/libcroco-0.6/libcroco/cr-om-parser.h
/usr/include/libcroco-0.6/libcroco/cr-parser.h
/usr/include/libcroco-0.6/libcroco/cr-parsing-location.h
/usr/include/libcroco-0.6/libcroco/cr-prop-list.h
/usr/include/libcroco-0.6/libcroco/cr-pseudo.h
/usr/include/libcroco-0.6/libcroco/cr-rgb.h
/usr/include/libcroco-0.6/libcroco/cr-sel-eng.h
/usr/include/libcroco-0.6/libcroco/cr-selector.h
/usr/include/libcroco-0.6/libcroco/cr-simple-sel.h
/usr/include/libcroco-0.6/libcroco/cr-statement.h
/usr/include/libcroco-0.6/libcroco/cr-string.h
/usr/include/libcroco-0.6/libcroco/cr-style.h
/usr/include/libcroco-0.6/libcroco/cr-stylesheet.h
/usr/include/libcroco-0.6/libcroco/cr-term.h
/usr/include/libcroco-0.6/libcroco/cr-tknzr.h
/usr/include/libcroco-0.6/libcroco/cr-token.h
/usr/include/libcroco-0.6/libcroco/cr-utils.h
/usr/include/libcroco-0.6/libcroco/libcroco-config.h
/usr/include/libcroco-0.6/libcroco/libcroco.h
/usr/lib64/libcroco-0.6.la
/usr/lib64/libcroco-0.6.so
/usr/lib64/libcroco-0.6.so.3
/usr/lib64/libcroco-0.6.so.3.0.1
/usr/lib64/pkgconfig/libcroco-0.6.pc
/usr/share/gtk-doc/html/libcroco/ch01.html
/usr/share/gtk-doc/html/libcroco/home.png
/usr/share/gtk-doc/html/libcroco/index.html
/usr/share/gtk-doc/html/libcroco/left-insensitive.png
/usr/share/gtk-doc/html/libcroco/left.png
/usr/share/gtk-doc/html/libcroco/libcroco-cr-additional-sel.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-attr-sel.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-cascade.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-declaration.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-doc-handler.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-enc-handler.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-fonts.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-input.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-num.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-om-parser.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-parser.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-parsing-location.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-prop-list.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-pseudo.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-rgb.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-sel-eng.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-selector.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-simple-sel.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-statement.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-string.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-style.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-stylesheet.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-term.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-tknzr.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-token.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-utils.html
/usr/share/gtk-doc/html/libcroco/libcroco-libcroco-config.html
/usr/share/gtk-doc/html/libcroco/libcroco.devhelp2
/usr/share/gtk-doc/html/libcroco/right-insensitive.png
/usr/share/gtk-doc/html/libcroco/right.png
/usr/share/gtk-doc/html/libcroco/style.css
/usr/share/gtk-doc/html/libcroco/up-insensitive.png
/usr/share/gtk-doc/html/libcroco/up.png

%changelog
# let's skip this for now

