Name:       libXdamage
Version:    1.1.4
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
/usr/include/X11/extensions/Xdamage.h
/usr/lib64/libXdamage.a
/usr/lib64/libXdamage.la
/usr/lib64/libXdamage.so
/usr/lib64/libXdamage.so.1
/usr/lib64/libXdamage.so.1.1.0
/usr/lib64/pkgconfig/xdamage.pc

%changelog
# let's skip this for now
