Name:       file
Version:    5.45
Release:    1
Summary:    A file type guesser
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
A file type guesser

%prep
%setup -q 

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/file
/usr/lib64/libmagic.so
/usr/lib64/libmagic.so.1
/usr/lib64/libmagic.so.1.0.0
/usr/include/magic.h
/usr/lib64/pkgconfig/libmagic.pc
/usr/share/man/
/usr/share/misc/magic.mgc

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 5.45
- Version bump
