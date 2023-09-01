Name:       xcb-util-cursor
Version:    0.1.3
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
/usr/include/xcb/xcb_cursor.h
/usr/lib64/libxcb-cursor.a
/usr/lib64/libxcb-cursor.so
/usr/lib64/libxcb-cursor.so.0
/usr/lib64/libxcb-cursor.so.0.0.0
/usr/lib64/pkgconfig/xcb-cursor.pc

%changelog
# let's skip this for now
