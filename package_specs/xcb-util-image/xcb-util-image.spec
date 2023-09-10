Name:       xcb-util-image
Version:    0.4.1
Release:    1
Summary:    XCB image utilities
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz



%description
XCB image utilities

%prep
%setup -q


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
/usr/lib64/libxcb-image.so
/usr/lib64/libxcb-image.so.0
/usr/lib64/libxcb-image.so.0.0.0
/usr/lib64/pkgconfig/xcb-image.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.4.1-1
- Version bump
