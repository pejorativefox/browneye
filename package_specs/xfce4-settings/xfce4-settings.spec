Name:       xfce4-settings
Version:    4.14.0
Release:    1
Summary:    Settings manager of the Xfce desktop
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Settings manager of the Xfce desktop

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/xfce4-accessibility-settings
/usr/bin/xfce4-appearance-settings
/usr/bin/xfce4-display-settings
/usr/bin/xfce4-find-cursor
/usr/bin/xfce4-keyboard-settings
/usr/bin/xfce4-mime-settings
/usr/bin/xfce4-mouse-settings
/usr/bin/xfce4-settings-editor
/usr/bin/xfce4-settings-manager
/usr/bin/xfsettingsd
/usr/etc/xdg/autostart/xfsettingsd.desktop
/usr/etc/xdg/menus/xfce-settings-manager.menu
/usr/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
/usr/lib64/xfce4/settings/appearance-install-theme
/usr/share/applications/xfce-display-settings.desktop
/usr/share/applications/xfce-keyboard-settings.desktop
/usr/share/applications/xfce-mouse-settings.desktop
/usr/share/applications/xfce-settings-manager.desktop
/usr/share/applications/xfce-ui-settings.desktop
/usr/share/applications/xfce4-accessibility-settings.desktop
/usr/share/applications/xfce4-mime-settings.desktop
/usr/share/applications/xfce4-settings-editor.desktop
/usr/share/icons/hicolor/128x128/devices/xfce-display-extend.png
/usr/share/icons/hicolor/128x128/devices/xfce-display-external.png
/usr/share/icons/hicolor/128x128/devices/xfce-display-internal.png
/usr/share/icons/hicolor/128x128/devices/xfce-display-mirror.png
/usr/share/icons/hicolor/128x128/devices/xfce-display-profile.png
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.0
- Initial RPM

