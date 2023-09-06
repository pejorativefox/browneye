Name:       libarchive
Version:    3.7.1
Release:    1
Summary:    Library for various archive formats
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The libarchive library provides a single interface for reading/writing various compression formats. 

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
/usr/bin/bsdcat
/usr/bin/bsdcpio
/usr/bin/bsdtar
/usr/include/archive.h
/usr/include/archive_entry.h
/usr/bin/bsdunzip
/usr/lib64/libarchive.a
/usr/lib64/libarchive.so
/usr/lib64/libarchive.so.13
/usr/lib64/libarchive.so.13.7.1
/usr/lib64/pkgconfig/libarchive.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 3.7.1-1
- Version bump
