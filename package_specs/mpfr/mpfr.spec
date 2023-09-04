Name:       mpfr
Version:    4.2.1
Release:    1
Summary:    Library for multiple-precision floating-point computation
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Library for multiple-precision floating-point computation

%prep
%setup -q

%build
%configure --disable-static --enable-thread-safe --docdir=/usr/share/doc/mpfr-%{version}
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/mpf2mpfr.h
/usr/include/mpfr.h
/usr/lib64/libmpfr.so
/usr/lib64/libmpfr.so.6
/usr/lib64/libmpfr.so.6.2.1
/usr/lib64/pkgconfig/mpfr.pc
/usr/share/doc/mpfr-4.2.1/
/usr/share/info/mpfr.info.gz

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.2.1
- Version bump
