Name:       pango
Version:    1.42.4
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
/usr/include/pango-1.0/pango/pango-attributes.h
/usr/include/pango-1.0/pango/pango-bidi-type.h
/usr/include/pango-1.0/pango/pango-break.h
/usr/include/pango-1.0/pango/pango-context.h
/usr/include/pango-1.0/pango/pango-coverage.h
/usr/include/pango-1.0/pango/pango-engine.h
/usr/include/pango-1.0/pango/pango-enum-types.h
/usr/include/pango-1.0/pango/pango-features.h
/usr/include/pango-1.0/pango/pango-font.h
/usr/include/pango-1.0/pango/pango-fontmap.h
/usr/include/pango-1.0/pango/pango-fontset.h
/usr/include/pango-1.0/pango/pango-glyph-item.h
/usr/include/pango-1.0/pango/pango-glyph.h
/usr/include/pango-1.0/pango/pango-gravity.h
/usr/include/pango-1.0/pango/pango-item.h
/usr/include/pango-1.0/pango/pango-language.h
/usr/include/pango-1.0/pango/pango-layout.h
/usr/include/pango-1.0/pango/pango-matrix.h
/usr/include/pango-1.0/pango/pango-modules.h
/usr/include/pango-1.0/pango/pango-ot.h
/usr/include/pango-1.0/pango/pango-renderer.h
/usr/include/pango-1.0/pango/pango-script.h
/usr/include/pango-1.0/pango/pango-tabs.h
/usr/include/pango-1.0/pango/pango-types.h
/usr/include/pango-1.0/pango/pango-utils.h
/usr/include/pango-1.0/pango/pango-version-macros.h
/usr/include/pango-1.0/pango/pango.h
/usr/include/pango-1.0/pango/pangocairo.h
/usr/include/pango-1.0/pango/pangofc-decoder.h
/usr/include/pango-1.0/pango/pangofc-font.h
/usr/include/pango-1.0/pango/pangofc-fontmap.h
/usr/include/pango-1.0/pango/pangoft2.h
/usr/include/pango-1.0/pango/pangoxft-render.h
/usr/include/pango-1.0/pango/pangoxft.h
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
/usr/libexec/installed-tests/pango/GraphemeBreakTest.txt
/usr/libexec/installed-tests/pango/all-unicode.txt
/usr/libexec/installed-tests/pango/boundaries.utf8
/usr/libexec/installed-tests/pango/cxx-test
/usr/libexec/installed-tests/pango/layouts/valid-1.expected
/usr/libexec/installed-tests/pango/layouts/valid-1.markup
/usr/libexec/installed-tests/pango/layouts/valid-2.expected
/usr/libexec/installed-tests/pango/layouts/valid-2.markup
/usr/libexec/installed-tests/pango/markup-parse
/usr/libexec/installed-tests/pango/markups/fail-1.expected
/usr/libexec/installed-tests/pango/markups/fail-1.markup
/usr/libexec/installed-tests/pango/markups/fail-2.expected
/usr/libexec/installed-tests/pango/markups/fail-2.markup
/usr/libexec/installed-tests/pango/markups/fail-3.expected
/usr/libexec/installed-tests/pango/markups/fail-3.markup
/usr/libexec/installed-tests/pango/markups/fail-4.expected
/usr/libexec/installed-tests/pango/markups/fail-4.markup
/usr/libexec/installed-tests/pango/markups/fail-5.expected
/usr/libexec/installed-tests/pango/markups/fail-5.markup
/usr/libexec/installed-tests/pango/markups/valid-1.expected
/usr/libexec/installed-tests/pango/markups/valid-1.markup
/usr/libexec/installed-tests/pango/markups/valid-2.expected
/usr/libexec/installed-tests/pango/markups/valid-2.markup
/usr/libexec/installed-tests/pango/markups/valid-3.expected
/usr/libexec/installed-tests/pango/markups/valid-3.markup
/usr/libexec/installed-tests/pango/markups/valid-4.expected
/usr/libexec/installed-tests/pango/markups/valid-4.markup
/usr/libexec/installed-tests/pango/markups/valid-5.expected
/usr/libexec/installed-tests/pango/markups/valid-5.markup
/usr/libexec/installed-tests/pango/markups/valid-6.expected
/usr/libexec/installed-tests/pango/markups/valid-6.markup
/usr/libexec/installed-tests/pango/markups/valid-7.expected
/usr/libexec/installed-tests/pango/markups/valid-7.markup
/usr/libexec/installed-tests/pango/markups/valid-8.expected
/usr/libexec/installed-tests/pango/markups/valid-8.markup
/usr/libexec/installed-tests/pango/markups/valid-9.expected
/usr/libexec/installed-tests/pango/markups/valid-9.markup
/usr/libexec/installed-tests/pango/test-font
/usr/libexec/installed-tests/pango/test-layout
/usr/libexec/installed-tests/pango/test-ot-tags
/usr/libexec/installed-tests/pango/test-pangocairo-threads
/usr/libexec/installed-tests/pango/testattributes
/usr/libexec/installed-tests/pango/testboundaries
/usr/libexec/installed-tests/pango/testboundaries_ucd
/usr/libexec/installed-tests/pango/testcolor
/usr/libexec/installed-tests/pango/testiter
/usr/libexec/installed-tests/pango/testscript
/usr/share/gir-1.0/Pango-1.0.gir
/usr/share/gir-1.0/PangoCairo-1.0.gir
/usr/share/gir-1.0/PangoFT2-1.0.gir
/usr/share/gir-1.0/PangoXft-1.0.gir
/usr/share/installed-tests/pango/cxx-test.test
/usr/share/installed-tests/pango/markup-parse.test
/usr/share/installed-tests/pango/test-font.test
/usr/share/installed-tests/pango/test-layout.test
/usr/share/installed-tests/pango/test-ot-tags.test
/usr/share/installed-tests/pango/test-pangocairo-threads.test
/usr/share/installed-tests/pango/testattributes.test
/usr/share/installed-tests/pango/testboundaries.test
/usr/share/installed-tests/pango/testboundaries_ucd.test
/usr/share/installed-tests/pango/testcolor.test
/usr/share/installed-tests/pango/testiter.test
/usr/share/installed-tests/pango/testscript.test


%changelog
# let's skip this for now

