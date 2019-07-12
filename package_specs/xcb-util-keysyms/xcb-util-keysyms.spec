Name:       xcb-util-keysyms
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
/usr/include/xcb/xcb_keysyms.h
/usr/lib64/libxcb-keysyms.a
/usr/lib64/libxcb-keysyms.la
/usr/lib64/libxcb-keysyms.so
/usr/lib64/libxcb-keysyms.so.1
/usr/lib64/libxcb-keysyms.so.1.0.0
/usr/lib64/pkgconfig/xcb-keysyms.pc

%changelog
# let's skip this for now
