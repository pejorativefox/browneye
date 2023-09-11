Name:       libxfixes
Version:    6.0.1
Release:    1
Summary:    Xlib-based library for the XFIXES Extension.
License:    GPL3
Prefix:     /usr
Source0:    libXfixes-%{version}.tar.xz

%description
Xlib-based library for the XFIXES Extension.

%prep
%setup -q -n libXfixes-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/Xfixes.h
/usr/lib64/libXfixes.a
/usr/lib64/libXfixes.so
/usr/lib64/libXfixes.so.3
/usr/lib64/libXfixes.so.3.1.0
/usr/lib64/pkgconfig/xfixes.pc
/usr/share/man/man3/Xfixes.3.gz

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 6.0.1-1
- Version bump
