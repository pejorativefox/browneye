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
%setup -q -a0

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
/usr/lib64/
/usr/share/info/mpfr.info.gz
/usr/share/doc/mpfr-%{version}/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.2.1
- Version bump
