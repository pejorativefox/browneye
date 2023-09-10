Name:       xcb-util
Version:    0.4.1
Release:    1
Summary:    XCB utilities
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
XCB utilities

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
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.4.1-1
- Version bump
