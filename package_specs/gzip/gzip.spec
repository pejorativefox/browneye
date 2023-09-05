Name:       gzip
Version:    1.12
Release:    1
Summary:    GNU data compression program
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Gzip is a popular data compression program originally written by Jean-loup Gailly for the GNU project. 

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
/usr/bin/gunzip
/usr/bin/gzexe
/usr/bin/gzip
/usr/bin/uncompress
/usr/bin/zcat
/usr/bin/zcmp
/usr/bin/zdiff
/usr/bin/zegrep
/usr/bin/zfgrep
/usr/bin/zforce
/usr/bin/zgrep
/usr/bin/zless
/usr/bin/zmore
/usr/bin/znew
/usr/share/info/gzip.info.gz
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.12-1
- Version bump
