Name:       xcb-util-wm
Version:    0.4.1
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
/usr/include/xcb/xcb_ewmh.h
/usr/include/xcb/xcb_icccm.h
/usr/lib64/libxcb-ewmh.a
/usr/lib64/libxcb-ewmh.so
/usr/lib64/libxcb-ewmh.so.2
/usr/lib64/libxcb-ewmh.so.2.0.0
/usr/lib64/libxcb-icccm.a
/usr/lib64/libxcb-icccm.so
/usr/lib64/libxcb-icccm.so.4
/usr/lib64/libxcb-icccm.so.4.0.0
/usr/lib64/pkgconfig/xcb-ewmh.pc
/usr/lib64/pkgconfig/xcb-icccm.pc



%changelog
# let's skip this for now
