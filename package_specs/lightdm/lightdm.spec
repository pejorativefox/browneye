Name:       lightdm
Version:    1.24.0
Release:    1
Summary:    A lightweight display manager
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
A lightweight display manager

Requires: shadow >= 4.6

%prep
%setup

%build
%configure ITSTOOL="/bin/true" \
	   --libexecdir=/usr/lib/lightdm \
           --with-greeter-session=lightdm-gtk-greeter \
	   --with-greeter-user=lightdm
%make_build

%install
rm -rf %{buildroot}
%make_install
cp tests/src/lightdm-session %{buildroot}/usr/bin

%post
groupadd -g 65 lightdm       &&
useradd  -c "Lightdm Daemon" \
         -d /var/lib/lightdm \
         -u 65 -g lightdm    \
         -s /bin/false lightdm

install -v -dm755 -o lightdm -g lightdm /var/lib/lightdm
install -v -dm755 -o lightdm -g lightdm /var/lib/lightdm-data
install -v -dm755 -o lightdm -g lightdm /var/cache/lightdm
install -v -dm770 -o lightdm -g lightdm /var/log/lightdm

%files
/usr/bin/dm-tool
/usr/bin/lightdm-session
/usr/etc/apparmor.d/abstractions/lightdm
/usr/etc/apparmor.d/abstractions/lightdm_chromium-browser
/usr/etc/apparmor.d/lightdm-guest-session
/usr/etc/dbus-1/system.d/org.freedesktop.DisplayManager.conf
/usr/etc/init/lightdm.conf
/usr/etc/lightdm/keys.conf
/usr/etc/lightdm/lightdm.conf
/usr/etc/lightdm/users.conf
/usr/etc/pam.d/lightdm
/usr/etc/pam.d/lightdm-autologin
/usr/etc/pam.d/lightdm-greeter
/usr/include/lightdm-gobject-1/lightdm.h
/usr/include/lightdm-gobject-1/lightdm/greeter.h
/usr/include/lightdm-gobject-1/lightdm/language.h
/usr/include/lightdm-gobject-1/lightdm/layout.h
/usr/include/lightdm-gobject-1/lightdm/power.h
/usr/include/lightdm-gobject-1/lightdm/session.h
/usr/include/lightdm-gobject-1/lightdm/system.h
/usr/include/lightdm-gobject-1/lightdm/user.h
/usr/lib/lightdm/lightdm-guest-session
/usr/lib64/girepository-1.0/LightDM-1.typelib
/usr/lib64/liblightdm-gobject-1.a
/usr/lib64/liblightdm-gobject-1.la
/usr/lib64/liblightdm-gobject-1.so
/usr/lib64/liblightdm-gobject-1.so.0
/usr/lib64/liblightdm-gobject-1.so.0.0.0
/usr/lib64/pkgconfig/liblightdm-gobject-1.pc
/usr/sbin/lightdm
/usr/share/bash-completion/completions/dm-tool
/usr/share/bash-completion/completions/lightdm
/usr/share/gir-1.0/LightDM-1.gir
/usr/share/gtk-doc/html/lightdm-gobject-1/*
/usr/share/help/C/lightdm/*
/usr/share/locale/*
/usr/share/man/man1/dm-tool.1.gz
/usr/share/man/man1/lightdm.1.gz
/usr/share/vala/vapi/liblightdm-gobject-1.deps
/usr/share/vala/vapi/liblightdm-gobject-1.vapi

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.24.0
- Initial RPM

