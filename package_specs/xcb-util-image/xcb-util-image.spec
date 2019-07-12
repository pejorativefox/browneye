Name:       xcb-util-image
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
/usr/include/xcb/xcb_bitops.h
/usr/include/xcb/xcb_image.h
/usr/include/xcb/xcb_pixel.h
/usr/lib64/libxcb-image.a
/usr/lib64/libxcb-image.la
/usr/lib64/libxcb-image.so
/usr/lib64/libxcb-image.so.0
/usr/lib64/libxcb-image.so.0.0.0
/usr/lib64/pkgconfig/xcb-image.pc

%changelog
# let's skip this for now
