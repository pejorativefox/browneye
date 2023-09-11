Name:       libxrandr
Version:    1.5.3
Release:    1
Summary:    Xlib Resize, Rotate and Reflection (RandR) extension library.
License:    GPL3
Prefix:     /usr
Source0:    libXrandr-%{version}.tar.xz

%description
Xlib Resize, Rotate and Reflection (RandR) extension library.

%prep
%setup -q -n libXrandr-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
 /usr/include/X11/extensions/Xrandr.h
/usr/lib64/libXrandr.a
/usr/lib64/libXrandr.so
/usr/lib64/libXrandr.so.2
/usr/lib64/libXrandr.so.2.2.0
/usr/lib64/pkgconfig/xrandr.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.5.3-1
- Version bump
