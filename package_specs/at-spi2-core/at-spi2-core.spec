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
/usr/include/at-spi-2.0/atspi/*
/usr/lib/systemd/user/at-spi-dbus-bus.service
/usr/lib/girepository-1.0/Atspi-2.0.typelib
/usr/lib/libatspi.so
/usr/lib/libatspi.so.0
/usr/lib/libatspi.so.0.0.1
/usr/lib/pkgconfig/atspi-2.pc
/usr/libexec/at-spi-bus-launcher
/usr/libexec/at-spi2-registryd
/usr/share/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
/usr/share/dbus-1/services/org.a11y.Bus.service
/usr/share/defaults/at-spi2/accessibility.conf
/usr/share/gir-1.0/Atspi-2.0.gir
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM


