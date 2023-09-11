Name:       libxkbfile
Version:    1.1.2
Release:    1
Summary:    library to parse the XKB configuration data files
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
libxkbfile is used by the X servers and utilities to parse the XKB configuration data files

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
/usr/include/X11/extensions/XKBbells.h
/usr/include/X11/extensions/XKBconfig.h
/usr/include/X11/extensions/XKBfile.h
/usr/include/X11/extensions/XKBrules.h
/usr/include/X11/extensions/XKM.h
/usr/include/X11/extensions/XKMformat.h
/usr/lib64/libxkbfile.a
/usr/lib64/libxkbfile.so
/usr/lib64/libxkbfile.so.1
/usr/lib64/libxkbfile.so.1.0.2
/usr/lib64/pkgconfig/xkbfile.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.1.2-1
- Version bump
