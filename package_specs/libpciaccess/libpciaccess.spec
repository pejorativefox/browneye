Name:       libpciaccess
Version:    0.14
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
/usr/include/pciaccess.h
/usr/lib64/libpciaccess.a
/usr/lib64/libpciaccess.so
/usr/lib64/libpciaccess.so.0
/usr/lib64/libpciaccess.so.0.11.1
/usr/lib64/pkgconfig/pciaccess.pc

%changelog
# let's skip this for now
