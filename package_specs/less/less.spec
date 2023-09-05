Name:       less
Version:    643
Release:    1
Summary:    open-source file pager. 
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Less is a free, open-source file pager. 

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
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey
/usr/share/man/man1/less.1.gz
/usr/share/man/man1/lessecho.1.gz
/usr/share/man/man1/lesskey.1.gz

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 643-1
 Version bump
