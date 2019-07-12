Name:       font-util
Version:    1.3.1
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
/usr/bin/bdftruncate
/usr/bin/ucs2any
/usr/lib64/pkgconfig/fontutil.pc
/usr/share/aclocal/fontutil.m4
/usr/share/fonts/X11/util/map-ISO8859-1
/usr/share/fonts/X11/util/map-ISO8859-10
/usr/share/fonts/X11/util/map-ISO8859-11
/usr/share/fonts/X11/util/map-ISO8859-13
/usr/share/fonts/X11/util/map-ISO8859-14
/usr/share/fonts/X11/util/map-ISO8859-15
/usr/share/fonts/X11/util/map-ISO8859-16
/usr/share/fonts/X11/util/map-ISO8859-2
/usr/share/fonts/X11/util/map-ISO8859-3
/usr/share/fonts/X11/util/map-ISO8859-4
/usr/share/fonts/X11/util/map-ISO8859-5
/usr/share/fonts/X11/util/map-ISO8859-6
/usr/share/fonts/X11/util/map-ISO8859-7
/usr/share/fonts/X11/util/map-ISO8859-8
/usr/share/fonts/X11/util/map-ISO8859-9
/usr/share/fonts/X11/util/map-JISX0201.1976-0
/usr/share/fonts/X11/util/map-KOI8-R
/usr/share/man/man1/bdftruncate.1.gz
/usr/share/man/man1/ucs2any.1.gz

%changelog
# let's skip this for now

