Name:       gmp
Version:    6.3.0
Release:    1
Summary:    The GMP math libraries
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Library for arbitrary precision arithmetic

%prep
%setup -q -a0

%build
%configure --enable-cxx --disable-static --docdir=/usr/share/doc/gmp-%{version}
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/
/usr/lib64/
/usr/share/info/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 6.3.0
- Version bump
