Name:       nspr
Version:    4.35
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
pushd nspr
%configure --enable-64bit
%make_build
popd

%install    
rm -rf %{buildroot}
pushd nspr
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/compile-et.pl
/usr/bin/nspr-config
/usr/bin/prerr.properties
/usr/include/
/usr/lib64/libnspr4.a
/usr/lib64/libnspr4.so
/usr/lib64/libplc4.a
/usr/lib64/libplc4.so
/usr/lib64/libplds4.a
/usr/lib64/libplds4.so
/usr/lib64/pkgconfig/nspr.pc
/usr/share/aclocal/nspr.m4

%changelog
# let's skip this for now
