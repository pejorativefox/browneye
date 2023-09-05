Name:       make
Version:    4.4.1
Release:    1
Summary:    GNU make
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The Make package contains a program for controlling the generation of executables and other non-source files of a package from source files.

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
/usr/bin/make
/usr/include/gnumake.h
/usr/share/info/make.info-1.gz
/usr/share/info/make.info.gz
/usr/share/info/make.info-2.gz
/usr/share/info/make.info-3.gz
/usr/share/locale/
/usr/share/man/man1/make.1.gz

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump
