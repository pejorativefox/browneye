Name:       thunar
Version:    1.8.9
Release:    1
Summary:    Modern file manager for Xfce
License:    GPL2
Source0:    Thunar-%{version}.tar.bz2
Prefix:     /usr

%description
Modern file manager for Xfce

%prep
%setup -n Thunar-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/Thunar
/usr/bin/thunar
/usr/bin/thunar-settings
/usr/etc/xdg/Thunar/uca.xml
/usr/include/thunarx-3/*
/usr/lib/systemd/user/thunar.service
/usr/lib64/Thunar/ThunarBulkRename
/usr/lib64/Thunar/thunar-sendto-email
/usr/lib64/girepository-1.0/Thunarx-3.0.typelib
/usr/lib64/libthunarx-3.la
/usr/lib64/libthunarx-3.so
/usr/lib64/libthunarx-3.so.0
/usr/lib64/libthunarx-3.so.0.0.0
/usr/lib64/pkgconfig/thunarx-3.pc
/usr/lib64/thunarx-3/thunar-apr.la
/usr/lib64/thunarx-3/thunar-apr.so
/usr/lib64/thunarx-3/thunar-sbr.la
/usr/lib64/thunarx-3/thunar-sbr.so
/usr/lib64/thunarx-3/thunar-uca.la
/usr/lib64/thunarx-3/thunar-uca.so
/usr/lib64/thunarx-3/thunar-wallpaper-plugin.la
/usr/lib64/thunarx-3/thunar-wallpaper-plugin.so
/usr/lib64/xfce4/panel/plugins/libthunar-tpa.la
/usr/lib64/xfce4/panel/plugins/libthunar-tpa.so
/usr/share/Thunar/sendto/thunar-sendto-email.desktop
/usr/share/applications/Thunar-bulk-rename.desktop
/usr/share/applications/Thunar-folder-handler.desktop
/usr/share/applications/Thunar.desktop
/usr/share/applications/thunar-settings.desktop
/usr/share/dbus-1/services/org.xfce.FileManager.service
/usr/share/dbus-1/services/org.xfce.Thunar.FileManager1.service
/usr/share/dbus-1/services/org.xfce.Thunar.service
/usr/share/doc/Thunar/README.gtkrc
/usr/share/gir-1.0/Thunarx-3.0.gir
/usr/share/gtk-doc/html/thunarx/*
/usr/share/icons/hicolor/128x128/apps/Thunar.png
/usr/share/icons/hicolor/16x16/apps/Thunar.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_folder-copy.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_folder-move.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_thunar-shortcuts.png
/usr/share/icons/hicolor/24x24/apps/Thunar.png
/usr/share/icons/hicolor/24x24/stock/navigation/stock_folder-copy.png
/usr/share/icons/hicolor/24x24/stock/navigation/stock_folder-move.png
/usr/share/icons/hicolor/48x48/apps/Thunar.png
/usr/share/icons/hicolor/64x64/apps/Thunar.png
/usr/share/icons/hicolor/scalable/apps/Thunar.svg
/usr/share/locale/*
/usr/share/man/man1/Thunar.1.gz
/usr/share/metainfo/org.xfce.thunar.appdata.xml
/usr/share/pixmaps/Thunar/Thunar-about-logo.png
/usr/share/polkit-1/actions/org.xfce.thunar.policy
/usr/share/xfce4/panel/plugins/thunar-tpa.desktop

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.8.9
- Initial RPM

