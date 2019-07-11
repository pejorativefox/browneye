Name:       gmp
Version:    6.1.2
Release:    1
Summary:    The GMP math libraries
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure --enable-cxx --disable-static --docdir=/usr/share/doc/gmp-6.1.2
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/gmp.h
/usr/include/gmpxx.h
/usr/lib64/libgmp.la
/usr/lib64/libgmp.so
/usr/lib64/libgmp.so.10
/usr/lib64/libgmp.so.10.3.2
/usr/lib64/libgmpxx.la
/usr/lib64/libgmpxx.so
/usr/lib64/libgmpxx.so.4
/usr/lib64/libgmpxx.so.4.5.2
/usr/share/info/gmp.info-1.gz
/usr/share/info/gmp.info-2.gz
/usr/share/info/gmp.info.gz



%changelog
# let's skip this for now
