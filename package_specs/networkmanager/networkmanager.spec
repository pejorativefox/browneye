Name:       NetworkManager
Version:    1.14.6
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
/usr/include/NetworkManager/NetworkManager.h
/usr/include/NetworkManager/NetworkManagerVPN.h
/usr/include/NetworkManager/nm-connection.h
/usr/include/NetworkManager/nm-setting-8021x.h
/usr/include/NetworkManager/nm-setting-adsl.h
/usr/include/NetworkManager/nm-setting-bluetooth.h
/usr/include/NetworkManager/nm-setting-bond.h
/usr/include/NetworkManager/nm-setting-bridge-port.h
/usr/include/NetworkManager/nm-setting-bridge.h
/usr/include/NetworkManager/nm-setting-cdma.h
/usr/include/NetworkManager/nm-setting-connection.h
/usr/include/NetworkManager/nm-setting-dcb.h
/usr/include/NetworkManager/nm-setting-generic.h
/usr/include/NetworkManager/nm-setting-gsm.h
/usr/include/NetworkManager/nm-setting-infiniband.h
/usr/include/NetworkManager/nm-setting-ip4-config.h
/usr/include/NetworkManager/nm-setting-ip6-config.h
/usr/include/NetworkManager/nm-setting-olpc-mesh.h
/usr/include/NetworkManager/nm-setting-ppp.h
/usr/include/NetworkManager/nm-setting-pppoe.h
/usr/include/NetworkManager/nm-setting-serial.h
/usr/include/NetworkManager/nm-setting-team-port.h
/usr/include/NetworkManager/nm-setting-team.h
/usr/include/NetworkManager/nm-setting-vlan.h
/usr/include/NetworkManager/nm-setting-vpn.h
/usr/include/NetworkManager/nm-setting-wimax.h
/usr/include/NetworkManager/nm-setting-wired.h
/usr/include/NetworkManager/nm-setting-wireless-security.h
/usr/include/NetworkManager/nm-setting-wireless.h
/usr/include/NetworkManager/nm-setting.h
/usr/include/NetworkManager/nm-utils-enum-types.h
/usr/include/NetworkManager/nm-utils.h
/usr/include/NetworkManager/nm-version-macros.h
/usr/include/NetworkManager/nm-version.h
/usr/include/libnm-glib/libnm_glib.h
/usr/include/libnm-glib/nm-access-point.h
/usr/include/libnm-glib/nm-active-connection.h
/usr/include/libnm-glib/nm-client.h
/usr/include/libnm-glib/nm-device-adsl.h
/usr/include/libnm-glib/nm-device-bond.h
/usr/include/libnm-glib/nm-device-bridge.h
/usr/include/libnm-glib/nm-device-bt.h
/usr/include/libnm-glib/nm-device-ethernet.h
/usr/include/libnm-glib/nm-device-generic.h
/usr/include/libnm-glib/nm-device-infiniband.h
/usr/include/libnm-glib/nm-device-modem.h
/usr/include/libnm-glib/nm-device-olpc-mesh.h
/usr/include/libnm-glib/nm-device-team.h
/usr/include/libnm-glib/nm-device-vlan.h
/usr/include/libnm-glib/nm-device-wifi.h
/usr/include/libnm-glib/nm-device-wimax.h
/usr/include/libnm-glib/nm-device.h
/usr/include/libnm-glib/nm-dhcp4-config.h
/usr/include/libnm-glib/nm-dhcp6-config.h
/usr/include/libnm-glib/nm-glib-enum-types.h
/usr/include/libnm-glib/nm-ip4-config.h
/usr/include/libnm-glib/nm-ip6-config.h
/usr/include/libnm-glib/nm-object.h
/usr/include/libnm-glib/nm-remote-connection.h
/usr/include/libnm-glib/nm-remote-settings.h
/usr/include/libnm-glib/nm-secret-agent.h
/usr/include/libnm-glib/nm-types.h
/usr/include/libnm-glib/nm-vpn-connection.h
/usr/include/libnm-glib/nm-vpn-enum-types.h
/usr/include/libnm-glib/nm-vpn-plugin-ui-interface.h
/usr/include/libnm-glib/nm-vpn-plugin-utils.h
/usr/include/libnm-glib/nm-vpn-plugin.h
/usr/include/libnm-glib/nm-wimax-nsp.h
/usr/include/libnm/NetworkManager.h
/usr/include/libnm/nm-access-point.h
/usr/include/libnm/nm-active-connection.h
/usr/include/libnm/nm-autoptr.h
/usr/include/libnm/nm-checkpoint.h
/usr/include/libnm/nm-client.h
/usr/include/libnm/nm-connection.h
/usr/include/libnm/nm-core-enum-types.h
/usr/include/libnm/nm-core-types.h
/usr/include/libnm/nm-dbus-interface.h
/usr/include/libnm/nm-device-6lowpan.h
/usr/include/libnm/nm-device-adsl.h
/usr/include/libnm/nm-device-bond.h
/usr/include/libnm/nm-device-bridge.h
/usr/include/libnm/nm-device-bt.h
/usr/include/libnm/nm-device-dummy.h
/usr/include/libnm/nm-device-ethernet.h
/usr/include/libnm/nm-device-generic.h
/usr/include/libnm/nm-device-infiniband.h
/usr/include/libnm/nm-device-ip-tunnel.h
/usr/include/libnm/nm-device-macsec.h
/usr/include/libnm/nm-device-macvlan.h
/usr/include/libnm/nm-device-modem.h
/usr/include/libnm/nm-device-olpc-mesh.h
/usr/include/libnm/nm-device-ovs-bridge.h
/usr/include/libnm/nm-device-ovs-interface.h
/usr/include/libnm/nm-device-ovs-port.h
/usr/include/libnm/nm-device-ppp.h
/usr/include/libnm/nm-device-team.h
/usr/include/libnm/nm-device-tun.h
/usr/include/libnm/nm-device-vlan.h
/usr/include/libnm/nm-device-vxlan.h
/usr/include/libnm/nm-device-wifi.h
/usr/include/libnm/nm-device-wimax.h
/usr/include/libnm/nm-device-wireguard.h
/usr/include/libnm/nm-device-wpan.h
/usr/include/libnm/nm-device.h
/usr/include/libnm/nm-dhcp-config.h
/usr/include/libnm/nm-enum-types.h
/usr/include/libnm/nm-errors.h
/usr/include/libnm/nm-ip-config.h
/usr/include/libnm/nm-object.h
/usr/include/libnm/nm-remote-connection.h
/usr/include/libnm/nm-secret-agent-old.h
/usr/include/libnm/nm-setting-6lowpan.h
/usr/include/libnm/nm-setting-8021x.h
/usr/include/libnm/nm-setting-adsl.h
/usr/include/libnm/nm-setting-bluetooth.h
/usr/include/libnm/nm-setting-bond.h
/usr/include/libnm/nm-setting-bridge-port.h
/usr/include/libnm/nm-setting-bridge.h
/usr/include/libnm/nm-setting-cdma.h
/usr/include/libnm/nm-setting-connection.h
/usr/include/libnm/nm-setting-dcb.h
/usr/include/libnm/nm-setting-dummy.h
/usr/include/libnm/nm-setting-ethtool.h
/usr/include/libnm/nm-setting-generic.h
/usr/include/libnm/nm-setting-gsm.h
/usr/include/libnm/nm-setting-infiniband.h
/usr/include/libnm/nm-setting-ip-config.h
/usr/include/libnm/nm-setting-ip-tunnel.h
/usr/include/libnm/nm-setting-ip4-config.h
/usr/include/libnm/nm-setting-ip6-config.h
/usr/include/libnm/nm-setting-macsec.h
/usr/include/libnm/nm-setting-macvlan.h
/usr/include/libnm/nm-setting-match.h
/usr/include/libnm/nm-setting-olpc-mesh.h
/usr/include/libnm/nm-setting-ovs-bridge.h
/usr/include/libnm/nm-setting-ovs-interface.h
/usr/include/libnm/nm-setting-ovs-patch.h
/usr/include/libnm/nm-setting-ovs-port.h
/usr/include/libnm/nm-setting-ppp.h
/usr/include/libnm/nm-setting-pppoe.h
/usr/include/libnm/nm-setting-proxy.h
/usr/include/libnm/nm-setting-serial.h
/usr/include/libnm/nm-setting-sriov.h
/usr/include/libnm/nm-setting-tc-config.h
/usr/include/libnm/nm-setting-team-port.h
/usr/include/libnm/nm-setting-team.h
/usr/include/libnm/nm-setting-tun.h
/usr/include/libnm/nm-setting-user.h
/usr/include/libnm/nm-setting-vlan.h
/usr/include/libnm/nm-setting-vpn.h
/usr/include/libnm/nm-setting-vxlan.h
/usr/include/libnm/nm-setting-wimax.h
/usr/include/libnm/nm-setting-wired.h
/usr/include/libnm/nm-setting-wireless-security.h
/usr/include/libnm/nm-setting-wireless.h
/usr/include/libnm/nm-setting-wpan.h
/usr/include/libnm/nm-setting.h
/usr/include/libnm/nm-simple-connection.h
/usr/include/libnm/nm-types.h
/usr/include/libnm/nm-utils.h
/usr/include/libnm/nm-version-macros.h
/usr/include/libnm/nm-version.h
/usr/include/libnm/nm-vpn-connection.h
/usr/include/libnm/nm-vpn-dbus-interface.h
/usr/include/libnm/nm-vpn-editor-plugin.h
/usr/include/libnm/nm-vpn-editor.h
/usr/include/libnm/nm-vpn-plugin-info.h
/usr/include/libnm/nm-vpn-plugin-old.h
/usr/include/libnm/nm-vpn-service-plugin.h
/usr/include/libnm/nm-wimax-nsp.h
/usr/lib64/NetworkManager/1.14.6/libnm-device-plugin-adsl.so
/usr/lib64/NetworkManager/1.14.6/libnm-device-plugin-wifi.so
/usr/lib64/girepository-1.0/NM-1.0.typelib
/usr/lib64/girepository-1.0/NMClient-1.0.typelib
/usr/lib64/girepository-1.0/NetworkManager-1.0.typelib
/usr/lib64/libnm-glib-vpn.so
/usr/lib64/libnm-glib-vpn.so.1
/usr/lib64/libnm-glib-vpn.so.1.2.0
/usr/lib64/libnm-glib.so
/usr/lib64/libnm-glib.so.4
/usr/lib64/libnm-glib.so.4.9.0
/usr/lib64/libnm-util.so
/usr/lib64/libnm-util.so.2
/usr/lib64/libnm-util.so.2.7.0
/usr/lib64/libnm.so
/usr/lib64/libnm.so.0
/usr/lib64/libnm.so.0.1.0
/usr/lib64/pkgconfig/NetworkManager.pc
/usr/lib64/pkgconfig/libnm-glib-vpn.pc
/usr/lib64/pkgconfig/libnm-glib.pc
/usr/lib64/pkgconfig/libnm-util.pc
/usr/lib64/pkgconfig/libnm.pc
/usr/libexec/nm-dhcp-helper
/usr/libexec/nm-dispatcher
/usr/libexec/nm-iface-helper
/usr/sbin/NetworkManager
/usr/share/bash-completion/completions/nmcli
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.AccessPoint.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.AgentManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Checkpoint.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Connection.Active.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DHCP4Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DHCP6Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Adsl.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bluetooth.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bond.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bridge.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Dummy.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Generic.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.IPTunnel.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Infiniband.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Lowpan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Macsec.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Macvlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Modem.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OlpcMesh.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OvsBridge.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OvsInterface.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OvsPort.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Ppp.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Statistics.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Team.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Tun.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Veth.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Vlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Vxlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.WiMax.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.WireGuard.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Wired.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Wireless.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Wpan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DnsManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.IP4Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.IP6Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.PPP.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.SecretAgent.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Settings.Connection.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Settings.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.VPN.Connection.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.VPN.Plugin.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.WiMax.Nsp.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.xml
/usr/share/dbus-1/system-services/org.freedesktop.nm_dispatcher.service
/usr/share/doc/NetworkManager/examples/server.conf
/usr/share/gir-1.0/NM-1.0.gir
/usr/share/gir-1.0/NMClient-1.0.gir
/usr/share/gir-1.0/NetworkManager-1.0.gir
/usr/share/locale/ar/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/as/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/be@latin/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/bg/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/bn_IN/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/bs/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ca/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/cs/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/da/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/de/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/dz/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/el/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/en_CA/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/en_GB/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/eo/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/es/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/et/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/eu/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/fi/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/fr/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/gd/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/gl/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/gu/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/he/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/hi/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/hr/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/hu/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/id/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/it/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ja/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ka/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/kn/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ko/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ku/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/lt/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/lv/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/mk/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ml/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/mr/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/nb/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ne/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/nl/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/oc/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/or/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/pa/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/pl/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/pt/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/pt_BR/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ru/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/rw/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/sk/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/sl/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/sq/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/sr/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/sr@latin/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/sv/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/ta/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/te/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/th/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/tr/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/uk/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/vi/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/wa/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/zh_CN/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/zh_HK/LC_MESSAGES/NetworkManager.mo
/usr/share/locale/zh_TW/LC_MESSAGES/NetworkManager.mo
/usr/share/polkit-1/actions/org.freedesktop.NetworkManager.policy


%changelog
# let's skip this for now

