Name:       libxinerama
Version:    1.1.5
Release:    1
Summary:    Xlib API for Xinerama extension to X11 Protocol
License:    GPL3
Prefix:     /usr
Source0:    libXinerama-%{version}.tar.xz

%description
Xlib API for Xinerama extension to X11 Protocol

%prep
%setup -q -n libXinerama-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/Xinerama.h
/usr/include/X11/extensions/panoramiXext.h
/usr/lib64/libXinerama.a
/usr/lib64/libXinerama.so
/usr/lib64/libXinerama.so.1
/usr/lib64/libXinerama.so.1.0.0
/usr/lib64/pkgconfig/xinerama.pc
/usr/share/man/man3/Xinerama.3.gz
/usr/share/man/man3/XineramaIsActive.3.gz
/usr/share/man/man3/XineramaQueryExtension.3.gz
/usr/share/man/man3/XineramaQueryScreens.3.gz
/usr/share/man/man3/XineramaQueryVersion.3.gz

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.1.5-1
- Version bump
