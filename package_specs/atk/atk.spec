Name:       atk
Version:    2.38.0
Release:    1
Summary:    ATK provides the set of accessibility interfaces
License:    LGPL
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(atk-2.0)
Provides: pkgconfig(atk)

%description
ATK provides the set of accessibility interfaces that are implemented by other toolkits and
applications. Using the ATK interfaces, accessibility tools have full access to view and 
control running applications. 

%prep
%setup -q

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
/usr/include/atk-1.0/atk/
/usr/lib64/girepository-1.0/Atk-1.0.typelib
/usr/lib64/libatk-1.0.so
/usr/lib64/libatk-1.0.so.0
/usr/lib64/libatk-1.0.so.0.23809.1
/usr/lib64/pkgconfig/atk.pc
/usr/share/gir-1.0/Atk-1.0.gir
/usr/share/locale/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.38.0-1
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM release

