Name:       xfdesktop
Version:    4.14.1
Release:    1
Summary:    A desktop manager for Xfce
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
A desktop manager for Xfce

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/xfdesktop
/usr/bin/xfdesktop-settings
/usr/share/applications/xfce-backdrop-settings.desktop
/usr/share/backgrounds/xfce/xfce-blue.jpg
/usr/share/backgrounds/xfce/xfce-stripes.png
/usr/share/backgrounds/xfce/xfce-teal.jpg
/usr/share/icons/hicolor/32x32/apps/xfce4-backdrop.png
/usr/share/icons/hicolor/32x32/apps/xfce4-menueditor.png
/usr/share/icons/hicolor/48x48/apps/xfce4-backdrop.png
/usr/share/icons/hicolor/48x48/apps/xfce4-menueditor.png
/usr/share/icons/hicolor/scalable/apps/xfce4-backdrop.svg
/usr/share/icons/hicolor/scalable/apps/xfce4-menueditor.svg
/usr/share/locale/*
/usr/share/man/man1/xfdesktop.1.gz
/usr/share/pixmaps/xfce4_xicon.png
/usr/share/pixmaps/xfce4_xicon1.png
/usr/share/pixmaps/xfce4_xicon2.png
/usr/share/pixmaps/xfce4_xicon3.png
/usr/share/pixmaps/xfce4_xicon4.png
/usr/share/pixmaps/xfdesktop/xfdesktop-fallback-icon.png

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.1
- Initial RPM

