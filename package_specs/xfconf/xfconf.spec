Name:       xfconf
Version:    4.14.1
Release:    1
Summary:    Flexible, easy-to-use configuration management system
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Flexible, easy-to-use configuration management system

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/xfconf-query
/usr/include/xfce4/xfconf-0/xfconf/xfconf-binding.h
/usr/include/xfce4/xfconf-0/xfconf/xfconf-channel.h
/usr/include/xfce4/xfconf-0/xfconf/xfconf-errors.h
/usr/include/xfce4/xfconf-0/xfconf/xfconf-types.h
/usr/include/xfce4/xfconf-0/xfconf/xfconf.h
/usr/lib64/girepository-1.0/Xfconf-0.typelib
/usr/lib64/libxfconf-0.la
/usr/lib64/libxfconf-0.so
/usr/lib64/libxfconf-0.so.3
/usr/lib64/libxfconf-0.so.3.0.0
/usr/lib64/pkgconfig/libxfconf-0.pc
/usr/lib64/xfce4/xfconf/xfconfd
/usr/share/dbus-1/services/org.xfce.Xfconf.service
/usr/share/gir-1.0/Xfconf-0.gir
/usr/share/vala/vapi/libxfconf-0.deps
/usr/share/vala/vapi/libxfconf-0.vapi
/usr/share/gtk-doc/html/xfconf/*
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.1
- Initial RPM

