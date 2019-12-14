Name:       libxfce4ui
Version:    4.14.1
Release:    1
Summary:    Commonly used Xfce widgets among Xfce applications
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Commonly used Xfce widgets among Xfce applications

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/share/gtk-doc/html/libxfce4ui/*
/usr/share/locale/*
/usr/include/xfce4/*
/usr/bin/xfce4-about
/usr/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
/usr/lib64/girepository-1.0/libxfce4ui-2.0.typelib
/usr/lib64/libxfce4kbd-private-2.la
/usr/lib64/libxfce4kbd-private-2.so
/usr/lib64/libxfce4kbd-private-2.so.0
/usr/lib64/libxfce4kbd-private-2.so.0.0.0
/usr/lib64/libxfce4kbd-private-3.la
/usr/lib64/libxfce4kbd-private-3.so
/usr/lib64/libxfce4kbd-private-3.so.0
/usr/lib64/libxfce4kbd-private-3.so.0.0.0
/usr/lib64/libxfce4ui-1.la
/usr/lib64/libxfce4ui-1.so
/usr/lib64/libxfce4ui-1.so.0
/usr/lib64/libxfce4ui-1.so.0.0.0
/usr/lib64/libxfce4ui-2.la
/usr/lib64/libxfce4ui-2.so
/usr/lib64/libxfce4ui-2.so.0
/usr/lib64/libxfce4ui-2.so.0.0.0
/usr/lib64/pkgconfig/libxfce4kbd-private-2.pc
/usr/lib64/pkgconfig/libxfce4kbd-private-3.pc
/usr/lib64/pkgconfig/libxfce4ui-1.pc
/usr/lib64/pkgconfig/libxfce4ui-2.pc
/usr/share/applications/xfce4-about.desktop
/usr/share/gir-1.0/libxfce4ui-2.0.gir
/usr/share/icons/hicolor/48x48/apps/xfce4-logo.png
/usr/share/vala/vapi/libxfce4ui-2.deps
/usr/share/vala/vapi/libxfce4ui-2.vapi

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.1
- Initial RPM

