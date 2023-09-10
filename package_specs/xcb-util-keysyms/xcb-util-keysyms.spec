Name:       xcb-util-keysyms
Version:    0.4.1
Release:    1
Summary:    XCB key symbols
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
XCB key symbols

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
/usr/include/xcb/xcb_keysyms.h
/usr/lib64/libxcb-keysyms.a
/usr/lib64/libxcb-keysyms.so
/usr/lib64/libxcb-keysyms.so.1
/usr/lib64/libxcb-keysyms.so.1.0.0
/usr/lib64/pkgconfig/xcb-keysyms.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.4.1-1
- Version bump
