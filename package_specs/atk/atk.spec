Name:       atk
Version:    2.30.0
Release:    1
Summary:    ATK provides the set of accessibility interfaces
License:    LGPL
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
ATK provides the set of accessibility interfaces that are implemented by other toolkits and
applications. Using the ATK interfaces, accessibility tools have full access to view and 
control running applications. 

%prep
%setup

%build
mkdir build-atk
pushd build-atk

meson --prefix=/usr ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-atk
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/atk-1.0/atk/*
/usr/lib/girepository-1.0/Atk-1.0.typelib
/usr/lib/libatk-1.0.so
/usr/lib/libatk-1.0.so.0
/usr/lib/libatk-1.0.so.0.23009.1
/usr/lib/pkgconfig/atk.pc
/usr/share/gir-1.0/Atk-1.0.gir
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM release

