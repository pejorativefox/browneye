Name:       at-spi2-core
Version:    2.48.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(atspi-2)

%description
TODO

%prep
%setup

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
/etc/xdg/Xwayland-session.d/00-at-spi
/usr/lib/systemd/user/at-spi-dbus-bus.service
/usr/include/at-spi-2.0/atspi/*
/usr/include/atk-1.0/
/usr/include/at-spi2-atk/2.0/atk-bridge.h
/usr/lib64/girepository-1.0/Atspi-2.0.typelib
/usr/lib64/libatspi.so
/usr/lib64/libatspi.so.0
/usr/lib64/libatspi.so.0.0.1
/usr/lib64/pkgconfig/atspi-2.pc
/usr/lib64/girepository-1.0/Atk-1.0.typelib
/usr/lib64/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
/usr/lib64/gtk-2.0/modules/libatk-bridge.so
/usr/lib64/libatk-1.0.so
/usr/lib64/libatk-1.0.so.0
/usr/lib64/libatk-1.0.so.0.24812.1
/usr/lib64/libatk-bridge-2.0.so
/usr/lib64/libatk-bridge-2.0.so.0
/usr/lib64/libatk-bridge-2.0.so.0.0.0
/usr/lib64/pkgconfig/atk-bridge-2.0.pc
/usr/lib64/pkgconfig/atk.pc
/usr/libexec/at-spi-bus-launcher
/usr/libexec/at-spi2-registryd
/usr/share/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
/usr/share/dbus-1/services/org.a11y.Bus.service
/usr/share/defaults/at-spi2/accessibility.conf
/usr/share/gir-1.0/Atspi-2.0.gir
/usr/share/locale/
/usr/share/gir-1.0/Atk-1.0.gir

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM


