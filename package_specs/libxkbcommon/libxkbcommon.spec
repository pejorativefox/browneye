Name:       libxkbcommon
Version:    0.8.4
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
%configure
%make_build


%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/xkbcommon/xkbcommon-compat.h
/usr/include/xkbcommon/xkbcommon-compose.h
/usr/include/xkbcommon/xkbcommon-keysyms.h
/usr/include/xkbcommon/xkbcommon-names.h
/usr/include/xkbcommon/xkbcommon-x11.h
/usr/include/xkbcommon/xkbcommon.h
/usr/lib64/libxkbcommon-x11.a
/usr/lib64/libxkbcommon-x11.la
/usr/lib64/libxkbcommon-x11.so
/usr/lib64/libxkbcommon-x11.so.0
/usr/lib64/libxkbcommon-x11.so.0.0.0
/usr/lib64/libxkbcommon.a
/usr/lib64/libxkbcommon.la
/usr/lib64/libxkbcommon.so
/usr/lib64/libxkbcommon.so.0
/usr/lib64/libxkbcommon.so.0.0.0
/usr/lib64/pkgconfig/xkbcommon-x11.pc
/usr/lib64/pkgconfig/xkbcommon.pc

%changelog
# let's skip this for now

