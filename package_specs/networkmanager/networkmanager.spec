Name:       NetworkManager
Version:    1.14.6
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Requires: shadow >= 4.6-1
Provides: pkgconfig(libnm)

%description
TODO

%prep
%setup

%build
sed '/initrd/d' -i src/meson.build
grep -rl '^#!.*python$' | xargs sed -i '1s/python/&3/'
mkdir build
pushd build
CXXFLAGS+="-O2 -fPIC"            \
meson --prefix /usr              \
      --sysconfdir /etc          \
      --localstatedir /var       \
      -Djson_validation=false    \
      -Dlibaudit=no              \
      -Dlibnm_glib=true          \
      -Dlibpsl=false             \
      -Dnmtui=true               \
      -Dovs=false                \
      -Dppp=false                \
      -Dselinux=false            \
      -Dudev_dir=/lib/udev       \
      -Dsession_tracking=no      \
      -Dmodem_manager=false      \
      -Dsystemdsystemunitdir=no  \
      -Dsystemd_journal=false    \
      -Dqt=false                 \
      ..
ninja

popd

%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%post
groupadd -fg 86 netdev

mkdir -pv /usr/share/polkit-1/rules.d/
cat > /usr/share/polkit-1/rules.d/org.freedesktop.NetworkManager.rules << "EOF"
polkit.addRule(function(action, subject) {
    if (action.id.indexOf("org.freedesktop.NetworkManager.") == 0 && subject.isInGroup("netdev")) {
        return polkit.Result.YES;
    }
});
EOF

mkdir -pv /etc/NetworkManager
cat >> /etc/NetworkManager/NetworkManager.conf << "EOF"
[main]
plugins=keyfile
EOF

%files
/etc/dbus-1/system.d/nm-dispatcher.conf
/etc/dbus-1/system.d/org.freedesktop.NetworkManager.conf
/lib/udev/rules.d/84-nm-drivers.rules
/lib/udev/rules.d/85-nm-unmanaged.rules
/lib/udev/rules.d/90-nm-thunderbolt.rules
/usr/bin/nm-online
/usr/bin/nmcli
/usr/bin/nmtui
/usr/bin/nmtui-connect
/usr/bin/nmtui-edit
/usr/bin/nmtui-hostname
/usr/include/*
/usr/share/vala/vapi/*
/usr/lib/NetworkManager/1.14.6/libnm-device-plugin-adsl.so
/usr/lib/NetworkManager/1.14.6/libnm-device-plugin-wifi.so
/usr/lib/girepository-1.0/NM-1.0.typelib
/usr/lib/girepository-1.0/NMClient-1.0.typelib
/usr/lib/girepository-1.0/NetworkManager-1.0.typelib
/usr/lib/libnm-glib-vpn.so
/usr/lib/libnm-glib-vpn.so.1
/usr/lib/libnm-glib-vpn.so.1.2.0
/usr/lib/libnm-glib.so
/usr/lib/libnm-glib.so.4
/usr/lib/libnm-glib.so.4.9.0
/usr/lib/libnm-util.so
/usr/lib/libnm-util.so.2
/usr/lib/libnm-util.so.2.7.0
/usr/lib/libnm.so
/usr/lib/libnm.so.0
/usr/lib/libnm.so.0.1.0
/usr/lib/pkgconfig/NetworkManager.pc
/usr/lib/pkgconfig/libnm-glib-vpn.pc
/usr/lib/pkgconfig/libnm-glib.pc
/usr/lib/pkgconfig/libnm-util.pc
/usr/lib/pkgconfig/libnm.pc
/usr/libexec/nm-dhcp-helper
/usr/libexec/nm-dispatcher
/usr/libexec/nm-iface-helper
/usr/sbin/NetworkManager
/usr/share/bash-completion/completions/nmcli
/usr/share/dbus-1*
/usr/share/doc/NetworkManager/examples/server.conf
/usr/share/gir-1.0/NM-1.0.gir
/usr/share/gir-1.0/NMClient-1.0.gir
/usr/share/gir-1.0/NetworkManager-1.0.gir
/usr/share/locale/*
/usr/share/polkit-1/actions/org.freedesktop.NetworkManager.policy


%changelog
# let's skip this for now

