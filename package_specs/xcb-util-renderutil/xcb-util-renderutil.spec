Name:       xcb-util-renderutil
Version:    0.3.9
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
/usr/include/xcb/xcb_renderutil.h
/usr/lib64/libxcb-render-util.a
/usr/lib64/libxcb-render-util.la
/usr/lib64/libxcb-render-util.so
/usr/lib64/libxcb-render-util.so.0
/usr/lib64/libxcb-render-util.so.0.0.0
/usr/lib64/pkgconfig/xcb-renderutil.pc


%changelog
# let's skip this for now
