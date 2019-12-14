Name:       libxklavier
Version:    5.4
Release:    1
Summary:    High-level API for X Keyboard Extension
License:    LGPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
High-level API for X Keyboard Extension

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/libxklavier/xkl-enum-types.h
/usr/include/libxklavier/xkl_config_item.h
/usr/include/libxklavier/xkl_config_rec.h
/usr/include/libxklavier/xkl_config_registry.h
/usr/include/libxklavier/xkl_engine.h
/usr/include/libxklavier/xkl_engine_marshal.h
/usr/include/libxklavier/xklavier.h
/usr/lib64/girepository-1.0/Xkl-1.0.typelib
/usr/lib64/libxklavier.a
/usr/lib64/libxklavier.la
/usr/lib64/libxklavier.so
/usr/lib64/libxklavier.so.16
/usr/lib64/libxklavier.so.16.4.0
/usr/lib64/pkgconfig/libxklavier.pc
/usr/share/gir-1.0/Xkl-1.0.gir
/usr/share/gtk-doc/html/libxklavier/*
/usr/share/vala/vapi/libxklavier.deps
/usr/share/vala/vapi/libxklavier.vapi

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 5.4
- Initial RPM

