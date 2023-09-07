Name:       cairo
Version:    1.17.6
Release:    1
Summary:    2D graphics library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
Cairo is a 2D graphics library with support for multiple output devices.

%prep
%setup -q

%build
sed 's/PTR/void */' -i util/cairo-trace/lookup-symbol.c
sed -e "/@prefix@/a exec_prefix=@exec_prefix@" \
    -i util/cairo-script/cairo-script-interpreter.pc.in

%configure  --prefix=/usr    \
            --disable-static \
            --enable-tee
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/cairo-sphinx
/usr/bin/cairo-trace
/usr/include/cairo/cairo-deprecated.h
/usr/include/cairo/cairo-features.h
/usr/include/cairo/cairo-ft.h
/usr/include/cairo/cairo-gobject.h
/usr/include/cairo/cairo-pdf.h
/usr/include/cairo/cairo-ps.h
/usr/include/cairo/cairo-script-interpreter.h
/usr/include/cairo/cairo-script.h
/usr/include/cairo/cairo-svg.h
/usr/include/cairo/cairo-tee.h
/usr/include/cairo/cairo-version.h
/usr/include/cairo/cairo.h
/usr/lib64/cairo/cairo-fdr.so
/usr/lib64/cairo/cairo-sphinx.so
/usr/lib64/cairo/libcairo-trace.so
/usr/lib64/libcairo-gobject.so
/usr/lib64/libcairo-gobject.so.2
/usr/lib64/libcairo-gobject.so.2.11706.0
/usr/lib64/libcairo-script-interpreter.so
/usr/lib64/libcairo-script-interpreter.so.2
/usr/lib64/libcairo-script-interpreter.so.2.11706.0
/usr/lib64/libcairo.so
/usr/lib64/libcairo.so.2
/usr/lib64/libcairo.so.2.11706.0
/usr/lib64/pkgconfig/cairo-ft.pc
/usr/lib64/pkgconfig/cairo-gobject.pc
/usr/lib64/pkgconfig/cairo-pdf.pc
/usr/lib64/pkgconfig/cairo-png.pc
/usr/lib64/pkgconfig/cairo-ps.pc
/usr/lib64/pkgconfig/cairo-script-interpreter.pc
/usr/lib64/pkgconfig/cairo-script.pc
/usr/lib64/pkgconfig/cairo-svg.pc
/usr/lib64/pkgconfig/cairo-tee.pc
/usr/lib64/pkgconfig/cairo.pc
/usr/share/gtk-doc/html/cairo/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.17.6-1
- Version bump
