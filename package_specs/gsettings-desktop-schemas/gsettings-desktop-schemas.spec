Name:       gsettings-desktop-schemas
Version:    3.28.0
Release:    1
Summary:    Collection of GSettings for GNOME desktop.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
 The GSettings Desktop Schemas package contains a collection of GSettings 
schemas for settings shared by various components of a GNOME Desktop. 

%prep
%setup

%build
sed -i -r 's:"(/system):"/org/gnome\1:g' schemas/*.in &&
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%post
glib-compile-schemas /usr/share/glib-2.0/schemas

%files
/usr/share/glib-2.0/schemas/*
/usr/share/locale/*
/usr/include/gsettings-desktop-schemas/gdesktop-enums.h
/usr/lib64/girepository-1.0/GDesktopEnums-3.0.typelib
/usr/share/GConf/gsettings/gsettings-desktop-schemas.convert
/usr/share/GConf/gsettings/wm-schemas.convert
/usr/share/gir-1.0/GDesktopEnums-3.0.gir
/usr/share/pkgconfig/gsettings-desktop-schemas.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Added this sample to help with adding new packages.

