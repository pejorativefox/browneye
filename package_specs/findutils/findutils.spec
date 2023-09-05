Name:       findutils
Version:    4.9.0
Release:    1
Summary:    GNU find utilities
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The GNU Find Utilities are the basic directory searching utilities of the GNU operating system.

%prep
%setup -q

%build
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/find
/usr/bin/locate
/usr/bin/updatedb
/usr/bin/xargs
/usr/libexec/frcode
/usr/share/info/
/usr/share/locale/
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 4.9.0-1
- Version bump
