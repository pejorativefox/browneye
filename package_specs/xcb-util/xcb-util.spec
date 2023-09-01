Name:       xcb-util
Version:    0.4.0
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
/usr/include/xcb/xcb_atom.h
/usr/include/xcb/xcb_aux.h
/usr/include/xcb/xcb_event.h
/usr/include/xcb/xcb_util.h
/usr/lib64/libxcb-util.a
/usr/lib64/libxcb-util.so
/usr/lib64/libxcb-util.so.1
/usr/lib64/libxcb-util.so.1.0.0
/usr/lib64/pkgconfig/xcb-atom.pc
/usr/lib64/pkgconfig/xcb-aux.pc
/usr/lib64/pkgconfig/xcb-event.pc
/usr/lib64/pkgconfig/xcb-util.pc

%changelog
# let's skip this for now
