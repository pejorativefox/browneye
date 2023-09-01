Name:       libXxf86dga
Version:    1.1.4
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



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
/usr/include/X11/extensions/Xxf86dga.h
/usr/include/X11/extensions/xf86dga1.h
/usr/lib64/libXxf86dga.a
/usr/lib64/libXxf86dga.so
/usr/lib64/libXxf86dga.so.1
/usr/lib64/libXxf86dga.so.1.0.0
/usr/lib64/pkgconfig/xxf86dga.pc
/usr/share/

%changelog
# let's skip this for now
