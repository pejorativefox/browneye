Name:       libxft
Version:    2.3.8
Release:    1
Summary:    Xorg font rendering library
License:    GPL3
Prefix:     /usr
Source0:    libXft-%{version}.tar.xz

%description
Client side font rendering library, using libfreetype, libX11, and the X Render extension to display anti-aliased text.

%prep
%setup -q -n libXft-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/Xft/Xft.h
/usr/include/X11/Xft/XftCompat.h
/usr/lib64/libXft.a
/usr/lib64/libXft.so
/usr/lib64/libXft.so.2
/usr/lib64/libXft.so.2.3.8
/usr/lib64/pkgconfig/xft.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.3.8-1
- Version bump
