Name:       libxxf86vm
Version:    1.1.5
Release:    1
Summary:    XFree86-VidMode X extension
License:    GPL3
Prefix:     /usr
Source0:    libXxf86vm-%{version}.tar.xz

%description
XFree86-VidMode X extension

%prep
%setup -q -n libXxf86vm-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/xf86vmode.h
/usr/lib64/libXxf86vm.a
/usr/lib64/libXxf86vm.so
/usr/lib64/libXxf86vm.so.1
/usr/lib64/libXxf86vm.so.1.0.0
/usr/lib64/pkgconfig/xxf86vm.pc
/usr/share/man/

%changelog
# let's skip this for now
