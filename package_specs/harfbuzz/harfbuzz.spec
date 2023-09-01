Name:       harfbuzz
Version:    2.3.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

Provides: pkgconfig(harfbuzz)

%description
TODO

%prep
%setup -a 0

%build
%configure  --disable-static --with-gobject
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/hb-ot-shape-closure
/usr/bin/hb-shape
/usr/bin/hb-subset
/usr/bin/hb-view
/usr/include/harfbuzz/hb-aat-layout.h
/usr/include/harfbuzz/hb-aat.h
/usr/include/harfbuzz/hb-blob.h
/usr/include/harfbuzz/hb-buffer.h
/usr/include/harfbuzz/hb-common.h
/usr/include/harfbuzz/hb-deprecated.h
/usr/include/harfbuzz/hb-face.h
/usr/include/harfbuzz/hb-font.h
/usr/include/harfbuzz/hb-ft.h
/usr/include/harfbuzz/hb-glib.h
/usr/include/harfbuzz/hb-gobject-enums.h
/usr/include/harfbuzz/hb-gobject-structs.h
/usr/include/harfbuzz/hb-gobject.h
/usr/include/harfbuzz/hb-map.h
/usr/include/harfbuzz/hb-ot-color.h
/usr/include/harfbuzz/hb-ot-deprecated.h
/usr/include/harfbuzz/hb-ot-font.h
/usr/include/harfbuzz/hb-ot-layout.h
/usr/include/harfbuzz/hb-ot-math.h
/usr/include/harfbuzz/hb-ot-name.h
/usr/include/harfbuzz/hb-ot-shape.h
/usr/include/harfbuzz/hb-ot-var.h
/usr/include/harfbuzz/hb-ot.h
/usr/include/harfbuzz/hb-set.h
/usr/include/harfbuzz/hb-shape-plan.h
/usr/include/harfbuzz/hb-shape.h
/usr/include/harfbuzz/hb-subset.h
/usr/include/harfbuzz/hb-unicode.h
/usr/include/harfbuzz/hb-version.h
/usr/include/harfbuzz/hb.h
/usr/lib64/cmake/harfbuzz/harfbuzz-config.cmake
/usr/lib64/girepository-1.0/HarfBuzz-0.0.typelib
/usr/lib64/libharfbuzz-gobject.so
/usr/lib64/libharfbuzz-gobject.so.0
/usr/lib64/libharfbuzz-gobject.so.0.20301.0
/usr/lib64/libharfbuzz-subset.so
/usr/lib64/libharfbuzz-subset.so.0
/usr/lib64/libharfbuzz-subset.so.0.20301.0
/usr/lib64/libharfbuzz.so
/usr/lib64/libharfbuzz.so.0
/usr/lib64/libharfbuzz.so.0.20301.0
/usr/lib64/pkgconfig/harfbuzz-gobject.pc
/usr/lib64/pkgconfig/harfbuzz-subset.pc
/usr/lib64/pkgconfig/harfbuzz.pc
/usr/share/gir-1.0/HarfBuzz-0.0.gir
/usr/share/gtk-doc/html/harfbuzz/HarfBuzz.png
/usr/share/gtk-doc/html/harfbuzz/HarfBuzz.svg
/usr/share/gtk-doc/html/harfbuzz/a-clustering-example-for-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/aat-shaping.html
/usr/share/gtk-doc/html/harfbuzz/adding-text-to-the-buffer.html
/usr/share/gtk-doc/html/harfbuzz/annotation-glossary.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-10.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-11.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-20.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-22.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-28.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-30.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-31.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-38.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-39.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-41.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-42.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-5.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-7.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-8.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-0-5.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-1-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-1-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-2-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-3-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-4-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-4-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-4-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-5-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-6-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-7-5.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-7-7.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-8-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-8-1.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-8-5.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-8-6.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-9-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-0-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-1-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-full.html
/usr/share/gtk-doc/html/harfbuzz/buffers-language-script-and-direction.html
/usr/share/gtk-doc/html/harfbuzz/building.html
/usr/share/gtk-doc/html/harfbuzz/ch01s03.html
/usr/share/gtk-doc/html/harfbuzz/ch03s02.html
/usr/share/gtk-doc/html/harfbuzz/ch03s03.html
/usr/share/gtk-doc/html/harfbuzz/ch09.html
/usr/share/gtk-doc/html/harfbuzz/ch10.html
/usr/share/gtk-doc/html/harfbuzz/ch11.html
/usr/share/gtk-doc/html/harfbuzz/ch12.html
/usr/share/gtk-doc/html/harfbuzz/clusters.html
/usr/share/gtk-doc/html/harfbuzz/complex-scripts.html
/usr/share/gtk-doc/html/harfbuzz/customizing-unicode-functions.html
/usr/share/gtk-doc/html/harfbuzz/deprecated-api-index.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces.html
/usr/share/gtk-doc/html/harfbuzz/getting-started.html
/usr/share/gtk-doc/html/harfbuzz/graphite-shaping.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-aat-layout.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-blob.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-buffer.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-common.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-coretext.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-deprecated.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-face.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-font.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ft.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-glib.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-gobject.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-graphite2.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-icu.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-map.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-color.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-font.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-layout.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-math.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-name.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-shape.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-var.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-set.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-shape-plan.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-shape.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-unicode.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-uniscribe.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-version.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz.devhelp2
/usr/share/gtk-doc/html/harfbuzz/home.png
/usr/share/gtk-doc/html/harfbuzz/index.html
/usr/share/gtk-doc/html/harfbuzz/install-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/left-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/left.png
/usr/share/gtk-doc/html/harfbuzz/level-2.html
/usr/share/gtk-doc/html/harfbuzz/opentype-shaping-models.html
/usr/share/gtk-doc/html/harfbuzz/plans-and-caching.html
/usr/share/gtk-doc/html/harfbuzz/pt01.html
/usr/share/gtk-doc/html/harfbuzz/pt02.html
/usr/share/gtk-doc/html/harfbuzz/reordering-in-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/right-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/right.png
/usr/share/gtk-doc/html/harfbuzz/setting-buffer-properties.html
/usr/share/gtk-doc/html/harfbuzz/shaping-and-shape-plans.html
/usr/share/gtk-doc/html/harfbuzz/shaping-concepts.html
/usr/share/gtk-doc/html/harfbuzz/shaping-operations.html
/usr/share/gtk-doc/html/harfbuzz/style.css
/usr/share/gtk-doc/html/harfbuzz/text-runs.html
/usr/share/gtk-doc/html/harfbuzz/the-distinction-between-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/unicode-character-categories.html
/usr/share/gtk-doc/html/harfbuzz/up-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/up.png
/usr/share/gtk-doc/html/harfbuzz/using-harfbuzzs-native-opentype-implementation.html
/usr/share/gtk-doc/html/harfbuzz/using-your-own-font-functions.html
/usr/share/gtk-doc/html/harfbuzz/what-about-the-other-scripts.html
/usr/share/gtk-doc/html/harfbuzz/what-harfbuzz-doesnt-do.html
/usr/share/gtk-doc/html/harfbuzz/what-is-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/why-do-i-need-a-shaping-engine.html
/usr/share/gtk-doc/html/harfbuzz/why-is-it-called-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/working-with-harfbuzz-clusters.html
   /usr/include/harfbuzz/hb-icu.h
   /usr/lib64/libharfbuzz-icu.so
   /usr/lib64/libharfbuzz-icu.so.0
   /usr/lib64/libharfbuzz-icu.so.0.20301.0
   /usr/lib64/pkgconfig/harfbuzz-icu.pc

%changelog
# let's skip this for now

