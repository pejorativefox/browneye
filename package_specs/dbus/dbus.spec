Name:       dbus
Version:    1.12.12
Release:    3
Summary:    D-BUS message bus
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz

%description
D-BUS is a system for sending messages between applications.

%prep
%setup

%build
%configure  --sysconfdir=/etc                    \
            --localstatedir=/var                 \
            --disable-doxygen-docs               \
            --disable-xml-docs                   \
            --disable-static                     \
            --docdir=/usr/share/doc/dbus-1.12.12 \
            --with-console-auth-dir=/run/console \
            --with-system-pid-file=/run/dbus/pid \
            --with-system-socket=/run/dbus/system_bus_socket
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%post
mkdir -pv /var/lib/dbus
mkdir -pv /run/dbus
useradd -c "D-Bus Message Daemon User" -d /var/run/dbus \
        -u 18 -g messagebus -s /bin/false messagebus
chown -v root:messagebus /usr/libexec/dbus-daemon-launch-helper &&
chmod -v      4750       /usr/libexec/dbus-daemon-launch-helper

%package daemon
Summary:        D-BUS message bus
%description daemon
The DBUS daemon

%files daemon
/etc/dbus-1/session.conf
/etc/dbus-1/system.conf
/usr/bin/dbus-cleanup-sockets
/usr/bin/dbus-daemon
/usr/bin/dbus-monitor
/usr/bin/dbus-run-session
/usr/bin/dbus-send
/usr/bin/dbus-test-tool
/usr/bin/dbus-update-activation-environment
/usr/bin/dbus-uuidgen
/usr/include/dbus-1.0/*
/usr/lib64/cmake/DBus1/DBus1Config.cmake
/usr/lib64/cmake/DBus1/DBus1ConfigVersion.cmake
/usr/lib64/dbus-1.0/include/dbus/dbus-arch-deps.h
/usr/lib64/pkgconfig/dbus-1.pc
/usr/libexec/dbus-daemon-launch-helper
/usr/share/dbus-1/session.conf
/usr/share/dbus-1/system.conf
/usr/share/doc/dbus-%{version}/*
/usr/share/xml/dbus-1/busconfig.dtd
/usr/share/xml/dbus-1/introspect.dtd

%package x11
Summary:  x11 addons for D-BUS
%description x11
D-BUS contains some tools that require Xlib to be installed

%files x11
/usr/bin/dbus-launch

%package libs
Summary: D-BUS libraries
%description libs
This package contains libraries for accessing D-BUS.

%files libs
/usr/lib64/libdbus-1.so
/usr/lib64/libdbus-1.so.3
/usr/lib64/libdbus-1.so.3.19.9

%changelog
* Thu May 15 2020 Chris Statzer <chris.statzer@qq.com> 1.12.12
- Split up the dbus components into seperate packages isolating the
  X11 and lib components.

