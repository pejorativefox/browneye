Name:       libice
Version:    1.1.1
Release:    1
Summary:    Inter-Client Exchange Library.
License:    GPL3
Prefix:     /usr
Source0:    libICE-%{version}.tar.xz

%description
Inter-Client Exchange Library.

%prep
%setup -q -n libICE-%{version}

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
/usr/lib64/libICE.so
/usr/lib64/libICE.so.6
/usr/lib64/libICE.so.6.3.0
/usr/lib64/pkgconfig/ice.pc
/usr/share/doc/libICE/ICElib.xml
/usr/share/doc/libICE/ice.xml

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.1.1-1
- Version bump
