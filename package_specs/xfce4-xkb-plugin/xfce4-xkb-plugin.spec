Name:       xfce4-xkb-plugin
Version:    0.8.1
Release:    1
Summary:    Plugin to switch keyboard layouts for the Xfce4 panel
License:    Custom
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Plugin to switch keyboard layouts for the Xfce4 panel

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/lib64/xfce4/panel/plugins/libxkb.la
/usr/lib64/xfce4/panel/plugins/libxkb.so
/usr/share/locale/*
/usr/share/xfce4/panel/plugins/xkb.desktop
/usr/share/xfce4/xkb/flags/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.8.1
- Initial RPM

