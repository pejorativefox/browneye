Name:       libsoup
Version:    2.62.3
Release:    1
Summary:    The libsoup is a HTTP client/server library for GNOME.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

BuildRequires: vala
BuildRequires: glib-networking

%description
The libsoup is a HTTP client/server library for GNOME.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/libsoup-gnome-2.4/libsoup/soup-cookie-jar-sqlite.h
/usr/include/libsoup-gnome-2.4/libsoup/soup-gnome-features.h
/usr/include/libsoup-gnome-2.4/libsoup/soup-gnome.h
/usr/lib64/girepository-1.0/Soup-2.4.typelib
/usr/lib64/girepository-1.0/SoupGNOME-2.4.typelib
/usr/lib64/libsoup-2.4.la
/usr/lib64/libsoup-2.4.so
/usr/lib64/libsoup-2.4.so.1
/usr/lib64/libsoup-2.4.so.1.8.0
/usr/lib64/libsoup-gnome-2.4.la
/usr/lib64/libsoup-gnome-2.4.so
/usr/lib64/libsoup-gnome-2.4.so.1
/usr/lib64/libsoup-gnome-2.4.so.1.8.0
/usr/lib64/pkgconfig/libsoup-2.4.pc
/usr/lib64/pkgconfig/libsoup-gnome-2.4.pc
/usr/share/gir-1.0/Soup-2.4.gir
/usr/share/gir-1.0/SoupGNOME-2.4.gir
/usr/share/gtk-doc/html/libsoup-2.4/*
/usr/include/libsoup-2.4/libsoup/*
/usr/share/locale/*
/usr/share/vala/vapi/libsoup-2.4.deps
/usr/share/vala/vapi/libsoup-2.4.vapi

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.62.3
- Initial RPM

