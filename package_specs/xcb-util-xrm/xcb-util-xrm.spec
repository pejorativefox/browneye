Name:       xcb-util-xrm
Version:    1.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

%description
TODO

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
/usr/include/xcb/xcb_xrm.h
/usr/lib64/libxcb-xrm.a
/usr/lib64/libxcb-xrm.so
/usr/lib64/libxcb-xrm.so.0
/usr/lib64/libxcb-xrm.so.0.0.0
/usr/lib64/pkgconfig/xcb-xrm.pc

%changelog
# let's skip this for now

