Name:       upower
Version:    0.99.7
Release:    1
Summary:    Abstraction for enumerating power devices, listening to device events and querying history and statistics
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

BuildRequires: libgudev
BuildRequires: libusb
BuildRequires: udev

%description
Abstraction for enumerating power devices, listening to device events and querying history and statistics

%prep
%setup

%build
%configure --disable-man-pages --disable-gtk-doc-html --enable-deprecated
%make_build XSLTPROC="/bin/true"

%install
rm -rf %{buildroot}
%make_install XSLTPROC="/bin/true"

%files
/usr/bin/upower
/usr/etc/UPower/UPower.conf
/usr/etc/dbus-1/system.d/org.freedesktop.UPower.conf
/usr/include/libupower-glib/up-autocleanups.h
/usr/include/libupower-glib/up-client.h
/usr/include/libupower-glib/up-device.h
/usr/include/libupower-glib/up-history-item.h
/usr/include/libupower-glib/up-stats-item.h
/usr/include/libupower-glib/up-types.h
/usr/include/libupower-glib/up-version.h
/usr/include/libupower-glib/up-wakeup-item.h
/usr/include/libupower-glib/up-wakeups.h
/usr/include/libupower-glib/upower.h
/usr/lib64/girepository-1.0/UPowerGlib-1.0.typelib
/usr/lib64/libupower-glib.a
/usr/lib64/libupower-glib.so
/usr/lib64/libupower-glib.so.3
/usr/lib64/libupower-glib.so.3.0.1
/usr/lib64/pkgconfig/upower-glib.pc
/usr/lib/udev/rules.d/95-upower-csr.rules
/usr/lib/udev/rules.d/95-upower-hid.rules
/usr/lib/udev/rules.d/95-upower-wup.rules
/usr/libexec/upowerd
/usr/share/dbus-1/interfaces/org.freedesktop.UPower.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.UPower.KbdBacklight.xml
/usr/share/dbus-1/interfaces/org.freedesktop.UPower.Wakeups.xml
/usr/share/dbus-1/interfaces/org.freedesktop.UPower.xml
/usr/share/dbus-1/system-services/org.freedesktop.UPower.service
/usr/share/gir-1.0/UPowerGlib-1.0.gir
/usr/share/locale/fr/LC_MESSAGES/upower.mo
/usr/share/locale/it/LC_MESSAGES/upower.mo
/usr/share/locale/pl/LC_MESSAGES/upower.mo
/usr/share/locale/sv/LC_MESSAGES/upower.mo

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.99.7
- Initial RPM

