Name:       libxshmfence
Version:    1.3
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
/usr/include/X11/xshmfence.h
/usr/lib64/libxshmfence.a
/usr/lib64/libxshmfence.so
/usr/lib64/libxshmfence.so.1
/usr/lib64/libxshmfence.so.1.0.0
/usr/lib64/pkgconfig/xshmfence.pc

%changelog
# let's skip this for now
