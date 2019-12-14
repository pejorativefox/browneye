Name:       xfwm4
Version:    4.14.0
Release:    1
Summary:    Xfce's window manager
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Xfce's window manager

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
   /usr/bin/xfwm4
   /usr/bin/xfwm4-settings
   /usr/bin/xfwm4-tweaks-settings
   /usr/bin/xfwm4-workspace-settings
   /usr/lib64/xfce4/xfwm4/helper-dialog
   /usr/share/applications/xfce-wm-settings.desktop
   /usr/share/applications/xfce-wmtweaks-settings.desktop
   /usr/share/applications/xfce-workspaces-settings.desktop
   /usr/share/icons/hicolor/*
   /usr/share/locale/*
   /usr/share/themes/*
   /usr/share/xfwm4/defaults

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.0
- Initial RPM

