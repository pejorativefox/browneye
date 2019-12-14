Name:       exo
Version:    0.12.8
Release:    1
Summary:    Application library for Xfce
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Application library for Xfce

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/exo-csource
/usr/bin/exo-desktop-item-edit
/usr/bin/exo-open
/usr/bin/exo-preferred-applications
/usr/etc/xdg/xfce4/helpers.rc
/usr/include/exo-1/*
/usr/include/exo-2/*
/usr/lib64/libexo-1.la
/usr/lib64/libexo-1.so
/usr/lib64/libexo-1.so.0
/usr/lib64/libexo-1.so.0.1.0
/usr/lib64/libexo-2.la
/usr/lib64/libexo-2.so
/usr/lib64/libexo-2.so.0
/usr/lib64/libexo-2.so.0.1.0
/usr/lib64/pkgconfig/exo-1.pc
/usr/lib64/pkgconfig/exo-2.pc
/usr/lib64/xfce4/exo-2/exo-helper-2
/usr/lib64/xfce4/exo/exo-compose-mail
/usr/share/applications/exo-file-manager.desktop
/usr/share/applications/exo-mail-reader.desktop
/usr/share/applications/exo-preferred-applications.desktop
/usr/share/applications/exo-terminal-emulator.desktop
/usr/share/applications/exo-web-browser.desktop
/usr/share/gtk-doc/html/exo-1/*
/usr/share/icons/hicolor/24x24/apps/preferences-desktop-default-applications.png
/usr/share/icons/hicolor/48x48/apps/preferences-desktop-default-applications.png
/usr/share/locale/*
/usr/share/man/man1/exo-csource.1.gz
/usr/share/man/man1/exo-open.1.gz
/usr/share/pixmaps/exo/exo-thumbnail-frame.png
/usr/share/xfce4/helpers/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.12.8
- Initial RPM

