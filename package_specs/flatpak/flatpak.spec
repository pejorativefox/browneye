Name:       flatpak
Version:    1.5.1
Release:    1
Summary:    Flatpak app distribution system.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Flatpak app distribution system.

%prep
%setup

%build
%configure --disable-documentation
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/flatpak
/usr/bin/flatpak-bisect
/usr/bin/flatpak-coredumpctl
/usr/etc/dbus-1/system.d/org.freedesktop.Flatpak.SystemHelper.conf
/usr/etc/profile.d/flatpak.sh
/usr/include/flatpak/*
/usr/lib/systemd/system/flatpak-system-helper.service
/usr/lib/systemd/user-environment-generators/60-flatpak
/usr/lib/systemd/user/flatpak-portal.service
/usr/lib/systemd/user/flatpak-session-helper.service
/usr/lib64/girepository-1.0/Flatpak-1.0.typelib
/usr/lib64/libflatpak.la
/usr/lib64/libflatpak.so
/usr/lib64/libflatpak.so.0
/usr/lib64/libflatpak.so.0.10501.0
/usr/lib64/pkgconfig/flatpak.pc
/usr/libexec/flatpak-bwrap
/usr/libexec/flatpak-dbus-proxy
/usr/libexec/flatpak-portal
/usr/libexec/flatpak-session-helper
/usr/libexec/flatpak-system-helper
/usr/libexec/flatpak-validate-icon
/usr/libexec/revokefs-fuse
/usr/share/bash-completion/completions/flatpak
/usr/share/dbus-1/interfaces/org.freedesktop.Flatpak.Authenticator.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Flatpak.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Flatpak.xml
/usr/share/dbus-1/services/org.freedesktop.Flatpak.service
/usr/share/dbus-1/services/org.freedesktop.portal.Flatpak.service
/usr/share/dbus-1/system-services/org.freedesktop.Flatpak.SystemHelper.service
/usr/share/flatpak/triggers/desktop-database.trigger
/usr/share/flatpak/triggers/gtk-icon-cache.trigger
/usr/share/flatpak/triggers/mime-database.trigger
/usr/share/gdm/env.d/flatpak.env
/usr/share/gir-1.0/Flatpak-1.0.gir
/usr/share/locale/*
/usr/share/polkit-1/actions/org.freedesktop.Flatpak.policy
/usr/share/polkit-1/rules.d/org.freedesktop.Flatpak.rules
/usr/share/zsh/site-functions/_flatpak

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.5.1
- Initial RPM

