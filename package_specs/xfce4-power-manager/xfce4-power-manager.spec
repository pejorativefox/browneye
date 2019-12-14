Name:       xfce4-power-manager
Version:    1.6.5
Release:    1
Summary:    Power manager for Xfce desktop
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Power manager for Xfce desktop

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/xfce4-power-manager
/usr/bin/xfce4-power-manager-settings
/usr/etc/xdg/autostart/xfce4-power-manager.desktop
/usr/lib64/xfce4/panel/plugins/libxfce4powermanager.la
/usr/lib64/xfce4/panel/plugins/libxfce4powermanager.so
/usr/sbin/xfce4-pm-helper
/usr/sbin/xfpm-power-backlight-helper
/usr/share/applications/xfce4-power-manager-settings.desktop
/usr/share/icons/hicolor/*
/usr/share/locale/*
/usr/share/man/man1/xfce4-power-manager-settings.1.gz
/usr/share/man/man1/xfce4-power-manager.1.gz
/usr/share/metainfo/xfce4-power-manager.appdata.xml
/usr/share/polkit-1/actions/org.xfce.power.policy
/usr/share/xfce4/panel/plugins/power-manager-plugin.desktop

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.6.5
- Initial RPM

