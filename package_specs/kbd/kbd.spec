Name:       kbd
Version:    2.6.1
Release:    1
Summary:    Utilities for managing Linux console
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Patch:      kbd-2.6.1-backspace-1.patch
Prefix:     /usr

%description
The kbd project contains utilities for managing Linux console (Linux console, virtual terminals, keyboard, etc.) – mainly, what they do is loading console fonts and keyboard maps.

%prep
%setup -q 
%patch -p1

%build
sed -i 's/\(RESIZECONS_PROGS=\)yes/\1no/g' configure
sed -i 's/resizecons.8 //' docs/man/man8/Makefile.in

%configure --disable-vlock
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files -f ../../SOURCES/kbd.filelist

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 2.6.1-1
- Version bump
