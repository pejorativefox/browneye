Name:       xfce4-panel
Version:    4.14.0
Release:    1
Summary:    Panel for the Xfce desktop environment
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Panel for the Xfce desktop environment

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/xfce4-panel
/usr/bin/xfce4-popup-applicationsmenu
/usr/bin/xfce4-popup-directorymenu
/usr/bin/xfce4-popup-windowmenu
/usr/etc/xdg/xfce4/panel/default.xml
/usr/include/xfce4/libxfce4panel-1.0/libxfce4panel/*
/usr/include/xfce4/libxfce4panel-2.0/libxfce4panel/*
/usr/lib64/girepository-1.0/libxfce4panel-2.0.typelib
/usr/lib64/libxfce4panel-1.0.la
/usr/lib64/libxfce4panel-1.0.so
/usr/lib64/libxfce4panel-1.0.so.4
/usr/lib64/libxfce4panel-1.0.so.4.0.0
/usr/lib64/libxfce4panel-2.0.la
/usr/lib64/libxfce4panel-2.0.so
/usr/lib64/libxfce4panel-2.0.so.4
/usr/lib64/libxfce4panel-2.0.so.4.0.0
/usr/lib64/pkgconfig/libxfce4panel-1.0.pc
/usr/lib64/pkgconfig/libxfce4panel-2.0.pc
/usr/lib64/xfce4/panel/migrate
/usr/lib64/xfce4/panel/plugins/*
/usr/lib64/xfce4/panel/wrapper-1.0
/usr/lib64/xfce4/panel/wrapper-2.0
/usr/share/applications/panel-desktop-handler.desktop
/usr/share/applications/panel-preferences.desktop
/usr/share/gir-1.0/libxfce4panel-2.0.gir
/usr/share/gtk-doc/html/libxfce4panel-2.0/*
/usr/share/icons/hicolor/16x16/apps/xfce4-panel-menu.png
/usr/share/icons/hicolor/16x16/apps/xfce4-panel.png
/usr/share/icons/hicolor/22x22/apps/xfce4-panel-menu.png
/usr/share/icons/hicolor/22x22/apps/xfce4-panel.png
/usr/share/icons/hicolor/24x24/apps/xfce4-panel-menu.png
/usr/share/icons/hicolor/24x24/apps/xfce4-panel.png
/usr/share/icons/hicolor/32x32/apps/xfce4-panel-menu.png
/usr/share/icons/hicolor/32x32/apps/xfce4-panel.png
/usr/share/icons/hicolor/48x48/apps/xfce4-panel-menu.png
/usr/share/icons/hicolor/48x48/apps/xfce4-panel.png
/usr/share/icons/hicolor/scalable/apps/xfce4-panel.svg
/usr/share/locale/*
/usr/share/vala/vapi/libxfce4panel-2.0.deps
/usr/share/vala/vapi/libxfce4panel-2.0.vapi
/usr/share/xfce4/panel/plugins/actions.desktop
/usr/share/xfce4/panel/plugins/applicationsmenu.desktop
/usr/share/xfce4/panel/plugins/clock.desktop
/usr/share/xfce4/panel/plugins/directorymenu.desktop
/usr/share/xfce4/panel/plugins/launcher.desktop
/usr/share/xfce4/panel/plugins/pager.desktop
/usr/share/xfce4/panel/plugins/separator.desktop
/usr/share/xfce4/panel/plugins/showdesktop.desktop
/usr/share/xfce4/panel/plugins/systray.desktop
/usr/share/xfce4/panel/plugins/tasklist.desktop
/usr/share/xfce4/panel/plugins/windowmenu.desktop

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.0
- Initial RPM

