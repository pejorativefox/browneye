Name:       libxrender
Version:    0.9.11
Release:    1
Summary:    Render Extension to the X11 protocol.
License:    GPL3
Prefix:     /usr
Source0:    libXrender-%{version}.tar.xz

%description
Render Extension to the X11 protocol.

%prep
%setup -q -n libXrender-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/Xrender.h
/usr/lib64/libXrender.a
/usr/lib64/libXrender.so
/usr/lib64/libXrender.so.1
/usr/lib64/libXrender.so.1.3.0
/usr/lib64/pkgconfig/xrender.pc
/usr/share/doc/libXrender/libXrender.txt

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.9.11-1
- Version bump
