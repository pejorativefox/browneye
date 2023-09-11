Name:       libxcursor
Version:    1.2.1
Release:    1
Summary:    Xlib-based Cursor management library
License:    GPL3
Prefix:     /usr
Source0:    libXcursor-%{version}.tar.xz

BuildRequires: libxrender

%description
Xlib-based Cursor management library

%prep
%setup -q -n libXcursor-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/Xcursor/Xcursor.h
/usr/lib64/libXcursor.a
/usr/lib64/libXcursor.so
/usr/lib64/libXcursor.so.1
/usr/lib64/libXcursor.so.1.0.2
/usr/lib64/pkgconfig/xcursor.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.2.1-1
- Version bump
