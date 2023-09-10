Name:       libxpm
Version:    3.5.16
Release:    1
Summary:    XPM file format
License:    GPL3
Prefix:     /usr
Source0:    libXpm-%{version}.tar.xz

%description
X Pixmap (XPM) image file format library.

%prep
%setup -q -n libXpm-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/cxpm
/usr/bin/sxpm
/usr/include/X11/xpm.h
/usr/lib64/libXpm.a
/usr/lib64/libXpm.so
/usr/lib64/libXpm.so.4
/usr/lib64/libXpm.so.4.11.0
/usr/lib64/pkgconfig/xpm.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 3.5.16
- Version bump
