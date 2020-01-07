Name:       json-glib
Version:    1.4.2
Release:    1
Summary:    Glib json support.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Glib json support.

%prep
%setup

%build
mkdir build
pushd build
meson --prefix=/usr ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/json-glib-format
/usr/bin/json-glib-validate
/usr/lib/girepository-1.0/Json-1.0.typelib
/usr/lib/libjson-glib-1.0.so
/usr/lib/libjson-glib-1.0.so.0
/usr/lib/libjson-glib-1.0.so.0.400.2
/usr/lib/pkgconfig/json-glib-1.0.pc
/usr/share/gir-1.0/Json-1.0.gir
/usr/share/installed-tests/*
/usr/libexec/installed-tests/json-glib-1.0/*
/usr/share/locale/*
/usr/include/json-glib-1.0/json-glib/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.4.2
- Initial RPM

