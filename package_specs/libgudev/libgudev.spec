Name:       libgudev
Version:    230
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}_%{version}.tar.xz

%description
TODO

%prep
%setup -a 0

%build
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/gudev-1.0/gudev/gudev.h
/usr/include/gudev-1.0/gudev/gudevclient.h
/usr/include/gudev-1.0/gudev/gudevdevice.h
/usr/include/gudev-1.0/gudev/gudevenumerator.h
/usr/include/gudev-1.0/gudev/gudevenums.h
/usr/include/gudev-1.0/gudev/gudevenumtypes.h
/usr/include/gudev-1.0/gudev/gudevtypes.h
/usr/lib64/girepository-1.0/GUdev-1.0.typelib
/usr/lib64/libgudev-1.0.la
/usr/lib64/libgudev-1.0.so
/usr/lib64/libgudev-1.0.so.0
/usr/lib64/libgudev-1.0.so.0.2.0
/usr/lib64/pkgconfig/gudev-1.0.pc
/usr/share/gir-1.0/GUdev-1.0.gir


%changelog
# let's skip this for now

