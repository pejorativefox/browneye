Name:       m4
Version:    1.4.19
Release:    1
Summary:    M4 macro processor
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/m4
/usr/share/info/m4.info-1.gz
/usr/share/info/m4.info-2.gz
/usr/share/info/m4.info.gz
/usr/share/man/man1/m4.1.gz
/usr/share/locale/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.4.19
- Version bump
