Name:       libpeas
Version:    1.26.0
Release:    1
Summary:    libpeas is a GObject based plugins engine, and is targeted at giving every application the chance to assume its own extensibility. 
License:    GPL
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(atk-2.0)
Provides: pkgconfig(atk)

%description
libpeas is a GObject based plugins engine, and is targeted at giving every application the chance to assume its own extensibility. 

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
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/peas-demo
/usr/include/libpeas-1.0/*
/usr/lib64/girepository-1.0/Peas-1.0.typelib
/usr/lib64/girepository-1.0/PeasGtk-1.0.typelib
/usr/lib64/libpeas-1.0.so
/usr/lib64/libpeas-1.0.so.0
/usr/lib64/libpeas-1.0.so.0.2600.0
/usr/lib64/libpeas-1.0/loaders/libpython3loader.so
/usr/lib64/libpeas-gtk-1.0.so
/usr/lib64/libpeas-gtk-1.0.so.0
/usr/lib64/libpeas-gtk-1.0.so.0.2600.0
/usr/lib64/peas-demo/*
/usr/lib64/pkgconfig/libpeas-1.0.pc
/usr/lib64/pkgconfig/libpeas-gtk-1.0.pc
/usr/share/gir-1.0/Peas-1.0.gir
/usr/share/gir-1.0/PeasGtk-1.0.gir
/usr/share/icons/hicolor/*
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.26.0
- Initial RPM release

