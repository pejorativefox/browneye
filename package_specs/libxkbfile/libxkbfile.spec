Name:       libxkbfile
Version:    1.0.9
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
# let's skip this for now
