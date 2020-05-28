Name:       atkmm
Version:    2.28.0
Release:    1
Summary:    atkmm is the C++ binding for the ATK library. 
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
atkmm is the C++ binding for the ATK library. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/lib64/atkmm-1.6/include/atkmmconfig.h
/usr/lib64/atkmm-1.6/proc/m4/convert.m4
/usr/lib64/atkmm-1.6/proc/m4/convert_atk.m4
/usr/lib64/libatkmm-1.6.la
/usr/lib64/libatkmm-1.6.so
/usr/lib64/libatkmm-1.6.so.1
/usr/lib64/libatkmm-1.6.so.1.1.0
/usr/lib64/pkgconfig/atkmm-1.6.pc
/usr/share/devhelp/books/atkmm-1.6/atkmm-1.6.devhelp2
/usr/include/atkmm-1.6/
/usr/share/doc/atkmm-1.6/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.28.0
- Initial RPM

