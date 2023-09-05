Name:       diffutils
Version:    3.10
Release:    1
Summary:    GNU file difference utilities
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
GNU Diffutils is a package of several programs related to finding differences between files.

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
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff
/usr/share/info/diffutils.info.gz
/usr/share/locale/
/usr/share/man/man1/cmp.1.gz
/usr/share/man/man1/diff.1.gz
/usr/share/man/man1/diff3.1.gz
/usr/share/man/man1/sdiff.1.gz

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 3.10-1
- Version bump
