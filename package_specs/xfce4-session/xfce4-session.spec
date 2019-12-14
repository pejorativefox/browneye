Name:       xfce4-session
Version:    4.14.0
Release:    1
Summary:    A session manager for Xfce
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
A session manager for Xfce

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/startxfce4
/usr/bin/xfce4-session
/usr/bin/xfce4-session-logout
/usr/bin/xfce4-session-settings
/usr/bin/xflock4
/usr/etc/xdg/autostart/xscreensaver.desktop
/usr/etc/xdg/xfce4/Xft.xrdb
/usr/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
/usr/etc/xdg/xfce4/xinitrc
/usr/lib64/xfce4/session/xfsm-shutdown-helper
/usr/share/applications/xfce-session-settings.desktop
/usr/share/applications/xfce4-session-logout.desktop
/usr/share/icons/hicolor/128x128/apps/xfce4-session.png
/usr/share/icons/hicolor/48x48/actions/xfsm-hibernate.png
/usr/share/icons/hicolor/48x48/actions/xfsm-logout.png
/usr/share/icons/hicolor/48x48/actions/xfsm-reboot.png
/usr/share/icons/hicolor/48x48/actions/xfsm-shutdown.png
/usr/share/icons/hicolor/48x48/actions/xfsm-suspend.png
/usr/share/icons/hicolor/48x48/apps/xfce4-session.png
/usr/share/icons/hicolor/scalable/apps/xfce4-session.svg
/usr/share/locale/*
/usr/share/man/man1/xfce4-session-logout.1.gz
/usr/share/man/man1/xfce4-session.1.gz
/usr/share/polkit-1/actions/org.xfce.session.policy
/usr/share/xsessions/xfce.desktop

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.0
- Initial RPM

