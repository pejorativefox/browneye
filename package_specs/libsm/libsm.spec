Name:       libSM
Version:    1.2.3
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
/usr/include/X11/SM/SM.h
/usr/include/X11/SM/SMlib.h
/usr/include/X11/SM/SMproto.h
/usr/lib64/libSM.so
/usr/lib64/libSM.so.6
/usr/lib64/libSM.so.6.0.1
/usr/lib64/libSM.a
/usr/lib64/pkgconfig/sm.pc
/usr/share/doc/libSM/SMlib.xml
/usr/share/doc/libSM/xsmp.xml

%changelog
# let's skip this for now
