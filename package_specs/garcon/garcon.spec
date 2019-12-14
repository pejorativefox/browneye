Name:       garcon
Version:    0.6.4
Release:    1
Summary:    Implementation of the freedesktop.org menu specification
License:    LGPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Implementation of the freedesktop.org menu specification

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/etc/xdg/menus/xfce-applications.menu
/usr/include/garcon-1/garcon/*
/usr/lib64/libgarcon-1.la
/usr/lib64/libgarcon-1.so
/usr/lib64/libgarcon-1.so.0
/usr/lib64/libgarcon-1.so.0.0.0
/usr/lib64/libgarcon-gtk2-1.la
/usr/lib64/libgarcon-gtk2-1.so
/usr/lib64/libgarcon-gtk2-1.so.0
/usr/lib64/libgarcon-gtk2-1.so.0.0.0
/usr/lib64/libgarcon-gtk3-1.la
/usr/lib64/libgarcon-gtk3-1.so
/usr/lib64/libgarcon-gtk3-1.so.0
/usr/lib64/libgarcon-gtk3-1.so.0.0.0
/usr/lib64/pkgconfig/garcon-1.pc
/usr/lib64/pkgconfig/garcon-gtk2-1.pc
/usr/lib64/pkgconfig/garcon-gtk3-1.pc
/usr/share/desktop-directories/*
/usr/share/gtk-doc/html/garcon/*
/usr/share/locale/*
/usr/include/garcon-gtk2-1/garcon-gtk/garcon-gtk-menu.h
/usr/include/garcon-gtk2-1/garcon-gtk/garcon-gtk.h
/usr/include/garcon-gtk3-1/garcon-gtk/garcon-gtk-menu.h
/usr/include/garcon-gtk3-1/garcon-gtk/garcon-gtk.h

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.6.4
- Initial RPM

