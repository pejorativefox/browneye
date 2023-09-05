Name:       patch
Version:    2.7.6
Release:    1
Summary:    GNU patch utility
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The Patch package contains a program for modifying or creating files by applying a patch file typically created by the diff program. 

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
/usr/bin/patch
/usr/share/man/man1/patch.1.gz

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 2.7.6-1
- Version bump
