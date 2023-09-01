Name:       libXrender
Version:    0.9.10
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
/usr/include/X11/extensions/Xrender.h
/usr/lib64/libXrender.a
/usr/lib64/libXrender.so
/usr/lib64/libXrender.so.1
/usr/lib64/libXrender.so.1.3.0
/usr/lib64/pkgconfig/xrender.pc
/usr/share/doc/libXrender/libXrender.txt

%changelog
# let's skip this for now
