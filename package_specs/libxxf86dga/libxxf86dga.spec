Name:       libxxf86dga
Version:    1.1.6
Release:    1
Summary:    Client library for the XFree86-DGA extension
License:    GPL3
Prefix:     /usr
Source0:    libXxf86dga-%{version}.tar.xz

%description
Client library for the XFree86-DGA extension

%prep
%setup -q -n libXxf86dga-%{version}

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
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.1.6-1
- Version bump
