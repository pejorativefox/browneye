Name:       psmisc
Version:    23.6
Release:    1
Summary:    procfs tools
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
This package contains miscellaneous utilities that use the proc file-system.

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
/usr/bin/fuser
/usr/bin/killall
/usr/bin/peekfd
/usr/bin/prtstat
/usr/bin/pslog
/usr/bin/pstree
/usr/bin/pstree.x11
/usr/share/locale/
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump
