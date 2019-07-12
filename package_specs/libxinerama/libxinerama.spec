Name:       libXinerama
Version:    1.1.4
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



%description
TODO

%prep
%setup -a 0


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
/usr/lib64/libXinerama.la
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
# let's skip this for now
