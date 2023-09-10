Name:       xcb-util-renderutil
Version:    0.3.10
Release:    1
Summary:    XCB render utilities
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz



%description
XCB render utilities

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
/usr/include/xcb/xcb_renderutil.h
/usr/lib64/libxcb-render-util.a
/usr/lib64/libxcb-render-util.so
/usr/lib64/libxcb-render-util.so.0
/usr/lib64/libxcb-render-util.so.0.0.0
/usr/lib64/pkgconfig/xcb-renderutil.pc


%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.3.10-1
- Version bump
