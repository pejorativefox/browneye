Name:       libICE
Version:    1.0.9
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
/usr/include/X11/ICE/ICE.h
/usr/include/X11/ICE/ICEconn.h
/usr/include/X11/ICE/ICElib.h
/usr/include/X11/ICE/ICEmsg.h
/usr/include/X11/ICE/ICEproto.h
/usr/include/X11/ICE/ICEutil.h
/usr/lib64/libICE.a
/usr/lib64/libICE.la
/usr/lib64/libICE.so
/usr/lib64/libICE.so.6
/usr/lib64/libICE.so.6.3.0
/usr/lib64/pkgconfig/ice.pc
/usr/share/doc/libICE/ICElib.xml
/usr/share/doc/libICE/ice.xml

%changelog
# let's skip this for now
