Name:       intltool
Version:    0.51.0
Release:    1
Summary:    gettext file processor
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
intltool is a set of tools to centralize translation of many different file formats using GNU gettext-compatible PO files.

%prep
%setup -q -a0

%build
sed -i 's:\\\${:\\\$\\{:' intltool-update.in
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/intltool-extract
/usr/bin/intltool-merge
/usr/bin/intltool-prepare
/usr/bin/intltool-update
/usr/bin/intltoolize
/usr/share/aclocal/intltool.m4
/usr/share/intltool/Makefile.in.in
/usr/share/man/*

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 0.51.0-1
- Version bump
