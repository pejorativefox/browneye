Name:       xtrans
Version:    1.3.5
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
%configure ICE_LIBS=-lpthread
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/Xtrans/Xtrans.c
/usr/include/X11/Xtrans/Xtrans.h
/usr/include/X11/Xtrans/Xtransint.h
/usr/include/X11/Xtrans/Xtranslcl.c
/usr/include/X11/Xtrans/Xtranssock.c
/usr/include/X11/Xtrans/Xtransutil.c
/usr/include/X11/Xtrans/transport.c
/usr/share/aclocal/xtrans.m4
/usr/share/doc/xtrans/xtrans.xml
/usr/share/pkgconfig/xtrans.pc

%changelog
# let's skip this for now
