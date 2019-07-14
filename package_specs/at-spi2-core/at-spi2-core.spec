Name:       at-spi2-core
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
/etc/xdg/autostart/at-spi-dbus-bus.desktop
/usr/include/at-spi-2.0/atspi/atspi-accessible.h
/usr/include/at-spi-2.0/atspi/atspi-action.h
/usr/include/at-spi-2.0/atspi/atspi-application.h
/usr/include/at-spi-2.0/atspi/atspi-collection.h
/usr/include/at-spi-2.0/atspi/atspi-component.h
/usr/include/at-spi-2.0/atspi/atspi-constants.h
/usr/include/at-spi-2.0/atspi/atspi-device-listener.h
/usr/include/at-spi-2.0/atspi/atspi-document.h
/usr/include/at-spi-2.0/atspi/atspi-editabletext.h
/usr/include/at-spi-2.0/atspi/atspi-enum-types.h
/usr/include/at-spi-2.0/atspi/atspi-event-listener.h
/usr/include/at-spi-2.0/atspi/atspi-gmain.h
/usr/include/at-spi-2.0/atspi/atspi-hyperlink.h
/usr/include/at-spi-2.0/atspi/atspi-hypertext.h
/usr/include/at-spi-2.0/atspi/atspi-image.h
/usr/include/at-spi-2.0/atspi/atspi-matchrule.h
/usr/include/at-spi-2.0/atspi/atspi-misc.h
/usr/include/at-spi-2.0/atspi/atspi-object.h
/usr/include/at-spi-2.0/atspi/atspi-registry.h
/usr/include/at-spi-2.0/atspi/atspi-relation.h
/usr/include/at-spi-2.0/atspi/atspi-selection.h
/usr/include/at-spi-2.0/atspi/atspi-stateset.h
/usr/include/at-spi-2.0/atspi/atspi-table-cell.h
/usr/include/at-spi-2.0/atspi/atspi-table.h
/usr/include/at-spi-2.0/atspi/atspi-text.h
/usr/include/at-spi-2.0/atspi/atspi-types.h
/usr/include/at-spi-2.0/atspi/atspi-value.h
/usr/include/at-spi-2.0/atspi/atspi.h
/usr/lib/systemd/user/at-spi-dbus-bus.service
/usr/lib64/girepository-1.0/Atspi-2.0.typelib
/usr/lib64/libatspi.so
/usr/lib64/libatspi.so.0
/usr/lib64/libatspi.so.0.0.1
/usr/lib64/pkgconfig/atspi-2.pc
/usr/libexec/at-spi-bus-launcher
/usr/libexec/at-spi2-registryd
/usr/share/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
/usr/share/dbus-1/services/org.a11y.Bus.service
/usr/share/defaults/at-spi2/accessibility.conf
/usr/share/gir-1.0/Atspi-2.0.gir
/usr/share/locale/an/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/as/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ast/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/be/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/bg/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/bn_IN/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/bs/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ca/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ca@valencia/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/cs/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/da/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/de/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/el/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/en_CA/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/en_GB/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/eo/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/es/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/et/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/eu/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/fa/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/fi/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/fr/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/fur/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ga/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/gd/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/gl/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/gu/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/he/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/hi/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/hr/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/hu/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/id/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/it/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ja/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/kk/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/km/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/kn/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ko/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/lt/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/lv/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ml/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/mr/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ms/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/nb/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ne/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/nl/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/oc/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/or/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/pa/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/pl/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/pt/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/pt_BR/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ro/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ru/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/sk/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/sl/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/sq/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/sr/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/sr@latin/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/sv/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ta/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/te/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/tg/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/tr/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/ug/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/uk/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/uz@cyrillic/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/vi/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/zh_CN/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/zh_HK/LC_MESSAGES/at-spi2-core.mo
/usr/share/locale/zh_TW/LC_MESSAGES/at-spi2-core.mo

%changelog
# let's skip this for now

