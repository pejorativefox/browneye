Name:       atk
Version:    2.30.0
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
mkdir build-atk
pushd build-atk

meson --prefix=/usr ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-atk
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/atk-1.0/atk/atk-enum-types.h
/usr/include/atk-1.0/atk/atk.h
/usr/include/atk-1.0/atk/atkaction.h
/usr/include/atk-1.0/atk/atkcomponent.h
/usr/include/atk-1.0/atk/atkdocument.h
/usr/include/atk-1.0/atk/atkeditabletext.h
/usr/include/atk-1.0/atk/atkgobjectaccessible.h
/usr/include/atk-1.0/atk/atkhyperlink.h
/usr/include/atk-1.0/atk/atkhyperlinkimpl.h
/usr/include/atk-1.0/atk/atkhypertext.h
/usr/include/atk-1.0/atk/atkimage.h
/usr/include/atk-1.0/atk/atkmisc.h
/usr/include/atk-1.0/atk/atknoopobject.h
/usr/include/atk-1.0/atk/atknoopobjectfactory.h
/usr/include/atk-1.0/atk/atkobject.h
/usr/include/atk-1.0/atk/atkobjectfactory.h
/usr/include/atk-1.0/atk/atkplug.h
/usr/include/atk-1.0/atk/atkrange.h
/usr/include/atk-1.0/atk/atkregistry.h
/usr/include/atk-1.0/atk/atkrelation.h
/usr/include/atk-1.0/atk/atkrelationset.h
/usr/include/atk-1.0/atk/atkrelationtype.h
/usr/include/atk-1.0/atk/atkselection.h
/usr/include/atk-1.0/atk/atksocket.h
/usr/include/atk-1.0/atk/atkstate.h
/usr/include/atk-1.0/atk/atkstateset.h
/usr/include/atk-1.0/atk/atkstreamablecontent.h
/usr/include/atk-1.0/atk/atktable.h
/usr/include/atk-1.0/atk/atktablecell.h
/usr/include/atk-1.0/atk/atktext.h
/usr/include/atk-1.0/atk/atkutil.h
/usr/include/atk-1.0/atk/atkvalue.h
/usr/include/atk-1.0/atk/atkversion.h
/usr/include/atk-1.0/atk/atkwindow.h
/usr/lib64/girepository-1.0/Atk-1.0.typelib
/usr/lib64/libatk-1.0.so
/usr/lib64/libatk-1.0.so.0
/usr/lib64/libatk-1.0.so.0.23009.1
/usr/lib64/pkgconfig/atk.pc
/usr/share/gir-1.0/Atk-1.0.gir
/usr/share/locale/af/LC_MESSAGES/atk10.mo
/usr/share/locale/am/LC_MESSAGES/atk10.mo
/usr/share/locale/an/LC_MESSAGES/atk10.mo
/usr/share/locale/ar/LC_MESSAGES/atk10.mo
/usr/share/locale/as/LC_MESSAGES/atk10.mo
/usr/share/locale/ast/LC_MESSAGES/atk10.mo
/usr/share/locale/az/LC_MESSAGES/atk10.mo
/usr/share/locale/be/LC_MESSAGES/atk10.mo
/usr/share/locale/be@latin/LC_MESSAGES/atk10.mo
/usr/share/locale/bg/LC_MESSAGES/atk10.mo
/usr/share/locale/bn/LC_MESSAGES/atk10.mo
/usr/share/locale/bn_IN/LC_MESSAGES/atk10.mo
/usr/share/locale/bs/LC_MESSAGES/atk10.mo
/usr/share/locale/ca/LC_MESSAGES/atk10.mo
/usr/share/locale/ca@valencia/LC_MESSAGES/atk10.mo
/usr/share/locale/cs/LC_MESSAGES/atk10.mo
/usr/share/locale/cy/LC_MESSAGES/atk10.mo
/usr/share/locale/da/LC_MESSAGES/atk10.mo
/usr/share/locale/de/LC_MESSAGES/atk10.mo
/usr/share/locale/dz/LC_MESSAGES/atk10.mo
/usr/share/locale/el/LC_MESSAGES/atk10.mo
/usr/share/locale/en@shaw/LC_MESSAGES/atk10.mo
/usr/share/locale/en_CA/LC_MESSAGES/atk10.mo
/usr/share/locale/en_GB/LC_MESSAGES/atk10.mo
/usr/share/locale/eo/LC_MESSAGES/atk10.mo
/usr/share/locale/es/LC_MESSAGES/atk10.mo
/usr/share/locale/et/LC_MESSAGES/atk10.mo
/usr/share/locale/eu/LC_MESSAGES/atk10.mo
/usr/share/locale/fa/LC_MESSAGES/atk10.mo
/usr/share/locale/fi/LC_MESSAGES/atk10.mo
/usr/share/locale/fr/LC_MESSAGES/atk10.mo
/usr/share/locale/fur/LC_MESSAGES/atk10.mo
/usr/share/locale/ga/LC_MESSAGES/atk10.mo
/usr/share/locale/gd/LC_MESSAGES/atk10.mo
/usr/share/locale/gl/LC_MESSAGES/atk10.mo
/usr/share/locale/gu/LC_MESSAGES/atk10.mo
/usr/share/locale/he/LC_MESSAGES/atk10.mo
/usr/share/locale/hi/LC_MESSAGES/atk10.mo
/usr/share/locale/hr/LC_MESSAGES/atk10.mo
/usr/share/locale/hu/LC_MESSAGES/atk10.mo
/usr/share/locale/hy/LC_MESSAGES/atk10.mo
/usr/share/locale/id/LC_MESSAGES/atk10.mo
/usr/share/locale/is/LC_MESSAGES/atk10.mo
/usr/share/locale/it/LC_MESSAGES/atk10.mo
/usr/share/locale/ja/LC_MESSAGES/atk10.mo
/usr/share/locale/ka/LC_MESSAGES/atk10.mo
/usr/share/locale/kk/LC_MESSAGES/atk10.mo
/usr/share/locale/km/LC_MESSAGES/atk10.mo
/usr/share/locale/kn/LC_MESSAGES/atk10.mo
/usr/share/locale/ko/LC_MESSAGES/atk10.mo
/usr/share/locale/ku/LC_MESSAGES/atk10.mo
/usr/share/locale/li/LC_MESSAGES/atk10.mo
/usr/share/locale/lt/LC_MESSAGES/atk10.mo
/usr/share/locale/lv/LC_MESSAGES/atk10.mo
/usr/share/locale/mai/LC_MESSAGES/atk10.mo
/usr/share/locale/mk/LC_MESSAGES/atk10.mo
/usr/share/locale/ml/LC_MESSAGES/atk10.mo
/usr/share/locale/mn/LC_MESSAGES/atk10.mo
/usr/share/locale/mr/LC_MESSAGES/atk10.mo
/usr/share/locale/ms/LC_MESSAGES/atk10.mo
/usr/share/locale/nb/LC_MESSAGES/atk10.mo
/usr/share/locale/ne/LC_MESSAGES/atk10.mo
/usr/share/locale/nl/LC_MESSAGES/atk10.mo
/usr/share/locale/nn/LC_MESSAGES/atk10.mo
/usr/share/locale/oc/LC_MESSAGES/atk10.mo
/usr/share/locale/or/LC_MESSAGES/atk10.mo
/usr/share/locale/pa/LC_MESSAGES/atk10.mo
/usr/share/locale/pl/LC_MESSAGES/atk10.mo
/usr/share/locale/ps/LC_MESSAGES/atk10.mo
/usr/share/locale/pt/LC_MESSAGES/atk10.mo
/usr/share/locale/pt_BR/LC_MESSAGES/atk10.mo
/usr/share/locale/ro/LC_MESSAGES/atk10.mo
/usr/share/locale/ru/LC_MESSAGES/atk10.mo
/usr/share/locale/rw/LC_MESSAGES/atk10.mo
/usr/share/locale/si/LC_MESSAGES/atk10.mo
/usr/share/locale/sk/LC_MESSAGES/atk10.mo
/usr/share/locale/sl/LC_MESSAGES/atk10.mo
/usr/share/locale/sq/LC_MESSAGES/atk10.mo
/usr/share/locale/sr/LC_MESSAGES/atk10.mo
/usr/share/locale/sr@ije/LC_MESSAGES/atk10.mo
/usr/share/locale/sr@latin/LC_MESSAGES/atk10.mo
/usr/share/locale/sv/LC_MESSAGES/atk10.mo
/usr/share/locale/ta/LC_MESSAGES/atk10.mo
/usr/share/locale/te/LC_MESSAGES/atk10.mo
/usr/share/locale/tg/LC_MESSAGES/atk10.mo
/usr/share/locale/th/LC_MESSAGES/atk10.mo
/usr/share/locale/tk/LC_MESSAGES/atk10.mo
/usr/share/locale/tr/LC_MESSAGES/atk10.mo
/usr/share/locale/tt/LC_MESSAGES/atk10.mo
/usr/share/locale/ug/LC_MESSAGES/atk10.mo
/usr/share/locale/uk/LC_MESSAGES/atk10.mo
/usr/share/locale/vi/LC_MESSAGES/atk10.mo
/usr/share/locale/wa/LC_MESSAGES/atk10.mo
/usr/share/locale/xh/LC_MESSAGES/atk10.mo
/usr/share/locale/yi/LC_MESSAGES/atk10.mo
/usr/share/locale/zh_CN/LC_MESSAGES/atk10.mo
/usr/share/locale/zh_HK/LC_MESSAGES/atk10.mo
/usr/share/locale/zh_TW/LC_MESSAGES/atk10.mo
/usr/share/locale/zu/LC_MESSAGES/atk10.mo

%changelog
# let's skip this for now

