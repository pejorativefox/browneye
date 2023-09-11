Name:       libxv
Version:    1.0.12
Release:    1
Summary:    Xlib-based library for the Xv extension
License:    GPL3
Prefix:     /usr
Source0:    libXv-%{version}.tar.xz

%description
Xlib-based library for the X Video (Xv) extension

%prep
%setup -q -n libXv-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/Xvlib.h
/usr/lib64/libXv.a
/usr/lib64/libXv.so
/usr/lib64/libXv.so.1
/usr/lib64/libXv.so.1.0.0
/usr/lib64/pkgconfig/xv.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.0.12-1
- Version bump
