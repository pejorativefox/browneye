Name:       autoconf
Version:    2.71
Release:    1
Summary:    Tool for producing configure scripts
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Autoconf is an extensible package of M4 macros that produce shell scripts to automatically configure software source code packages. 

%prep
%setup

%build
sed -e 's/SECONDS|/&SHLVL|/'               \
    -e '/BASH_ARGV=/a\        /^SHLVL=/ d' \
    -i.orig tests/local.at

%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/autoconf
/usr/bin/autoheader
/usr/bin/autom4te
/usr/bin/autoreconf
/usr/bin/autoscan
/usr/bin/autoupdate
/usr/bin/ifnames
/usr/share/autoconf/*
/usr/share/info/autoconf.info.gz
/usr/share/info/standards.info.gz
/usr/share/man/*

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 2.71-1
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.69
- Initial RPM

