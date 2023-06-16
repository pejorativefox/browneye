Name:       NetworkManager
Version:    1.42.4
Release:    1
Summary:    Network configuration tool suite.
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2
Source1:    NetworkManager.conf
Source2:    org.freedesktop.NetworkManager.rules
Source3:    networkmanager-service.conf
Requires: shadow >= 4.6-1
Provides: pkgconfig(libnm)

%description
NetworkManager is the standard Linux network configuration tool suite.

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
      -Dlibaudit=no              \
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

# configuration
mkdir -pv %{buildroot}/etc/NetworkManager
cp %{SOURCE1} %{buildroot}/etc/NetworkManager/

# polkit policy
mkdir -pv %{buildroot}/usr/share/polkit-1/rules.d/
cp %{SOURCE2} %{buildroot}/usr/share/polkit-1/rules.d/

# finit service file
mkdir -pv %{buildroot}/etc/finit.d/available/
cp %{SOURCE3} %{buildroot}/etc/finit.d/available/networkmanager.conf


%post
groupadd -fg 86 netdev

%files
/etc/NetworkManager/NetworkManager.conf
/etc/finit.d/available/networkmanager.conf
/lib/udev/rules.d/84-nm-drivers.rules
/lib/udev/rules.d/85-nm-unmanaged.rules
/lib/udev/rules.d/90-nm-thunderbolt.rules
/usr/bin/nm-online
/usr/bin/nmcli
/usr/bin/nmtui
/usr/bin/nmtui-connect
/usr/bin/nmtui-edit
/usr/bin/nmtui-hostname
/usr/include/libnm/
/usr/lib/NetworkManager/1.42.4/libnm-device-plugin-adsl.so
/usr/lib/NetworkManager/1.42.4/libnm-device-plugin-wifi.so
/usr/lib/firewalld/zones/nm-shared.xml
/usr/lib/girepository-1.0/NM-1.0.typelib
/usr/lib/libnm.so
/usr/lib/libnm.so.0
/usr/lib/libnm.so.0.1.0
/usr/lib/pkgconfig/libnm.pc
/usr/libexec/nm-daemon-helper
/usr/libexec/nm-dhcp-helper
/usr/libexec/nm-dispatcher
/usr/libexec/nm-priv-helper
/usr/sbin/NetworkManager
/usr/share/dbus-1/
/usr/share/doc/NetworkManager/examples/server.conf
/usr/share/gir-1.0/NM-1.0.gir
/usr/share/locale/
/usr/share/polkit-1/
/usr/share/vala/vapi/libnm.deps
/usr/share/vala/vapi/libnm.vapi
/usr/share/bash-completion/completions/nmcli

%changelog
* Fri Jun 16 2023 Chris Statzer <chris.statzer@gmail.com> 1.42.4
- Changed the name of the finit service file.

* Thu May 14 2020 Chris Statzer <chris.statzer@qq.com> 1.14.6
- Moved old cat file kludges out, added finit service
