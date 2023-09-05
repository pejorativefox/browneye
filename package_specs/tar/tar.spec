Name:       tar
Version:    1.35
Release:    1
Summary:    GNU tar utility
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The Tar package provides the ability to create tar archives as well as perform various other kinds of archive manipulation. Tar can be used on previously created archives to extract files, to store additional files, or to update or list files which were already stored. 

%prep
%setup -q

%build
export FORCE_UNSAFE_CONFIGURE=1
%configure 
%make_build
unset FORCE_UNSAFE_CONFIGURE
%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/tar
/usr/libexec/rmt
/usr/share/info/tar.info-1.gz
/usr/share/info/tar.info-2.gz
/usr/share/info/tar.info-3.gz
/usr/share/info/tar.info.gz
/usr/share/locale/
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.35-1
- Version bump
