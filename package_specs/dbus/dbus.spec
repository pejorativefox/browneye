Name:       dbus
Version:    1.12.12
Release:    3
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

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


%files
/etc/dbus-1/session.conf
/etc/dbus-1/system.conf
/usr/bin/dbus-cleanup-sockets
/usr/bin/dbus-daemon
/usr/bin/dbus-launch
/usr/bin/dbus-monitor
/usr/bin/dbus-run-session
/usr/bin/dbus-send
/usr/bin/dbus-test-tool
/usr/bin/dbus-update-activation-environment
/usr/bin/dbus-uuidgen
/usr/include/dbus-1.0/dbus/dbus-address.h
/usr/include/dbus-1.0/dbus/dbus-bus.h
/usr/include/dbus-1.0/dbus/dbus-connection.h
/usr/include/dbus-1.0/dbus/dbus-errors.h
/usr/include/dbus-1.0/dbus/dbus-macros.h
/usr/include/dbus-1.0/dbus/dbus-memory.h
/usr/include/dbus-1.0/dbus/dbus-message.h
/usr/include/dbus-1.0/dbus/dbus-misc.h
/usr/include/dbus-1.0/dbus/dbus-pending-call.h
/usr/include/dbus-1.0/dbus/dbus-protocol.h
/usr/include/dbus-1.0/dbus/dbus-server.h
/usr/include/dbus-1.0/dbus/dbus-shared.h
/usr/include/dbus-1.0/dbus/dbus-signature.h
/usr/include/dbus-1.0/dbus/dbus-syntax.h
/usr/include/dbus-1.0/dbus/dbus-threads.h
/usr/include/dbus-1.0/dbus/dbus-types.h
/usr/include/dbus-1.0/dbus/dbus.h
/usr/lib64/cmake/DBus1/DBus1Config.cmake
/usr/lib64/cmake/DBus1/DBus1ConfigVersion.cmake
/usr/lib64/dbus-1.0/include/dbus/dbus-arch-deps.h
/usr/lib64/libdbus-1.la
/usr/lib64/libdbus-1.so
/usr/lib64/libdbus-1.so.3
/usr/lib64/libdbus-1.so.3.19.9
/usr/lib64/pkgconfig/dbus-1.pc
/usr/libexec/dbus-daemon-launch-helper
/usr/share/dbus-1/session.conf
/usr/share/dbus-1/system.conf
/usr/share/doc/dbus-1.12.12/diagram.png
/usr/share/doc/dbus-1.12.12/diagram.svg
/usr/share/doc/dbus-1.12.12/examples/GetAllMatchRules.py
/usr/share/doc/dbus-1.12.12/examples/example-session-disable-stats.conf
/usr/share/doc/dbus-1.12.12/examples/example-system-enable-stats.conf
/usr/share/doc/dbus-1.12.12/system-activation.txt
/usr/share/xml/dbus-1/busconfig.dtd
/usr/share/xml/dbus-1/introspect.dtd

%changelog
# let's skip this for now

