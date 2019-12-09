Name:       intltool
Version:    0.51.0
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

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
# let's skip this for now
