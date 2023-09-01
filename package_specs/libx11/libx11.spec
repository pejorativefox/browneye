Name:       libX11
Version:    1.8
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz



%description
TODO

%prep
%setup -a 0


%build
%configure ICE_LIBS=-lpthread
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/
/usr/lib64/libX11-xcb.a
/usr/lib64/libX11-xcb.so
/usr/lib64/libX11-xcb.so.1
/usr/lib64/libX11-xcb.so.1.0.0
/usr/lib64/libX11.a
/usr/lib64/libX11.so
/usr/lib64/libX11.so.6
/usr/lib64/libX11.so.6.4.0
/usr/lib64/pkgconfig/x11-xcb.pc
/usr/lib64/pkgconfig/x11.pc
/usr/share/

%changelog
# let's skip this for now
