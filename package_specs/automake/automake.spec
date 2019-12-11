Name:       automake
Version:    1.16.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup

%build
%configure --docdir=/usr/share/doc/automake-1.16.1
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/aclocal
/usr/bin/aclocal-1.16
/usr/bin/automake
/usr/bin/automake-1.16
/usr/share/aclocal-1.16/*
/usr/share/aclocal/README
/usr/share/automake-1.16/*
/usr/share/doc/automake-1.16.1/amhello-1.0.tar.gz
/usr/share/info/automake-history.info.gz
/usr/share/info/automake.info-1.gz
/usr/share/info/automake.info-2.gz
/usr/share/info/automake.info.gz
/usr/share/man/man1/aclocal-1.16.1.gz
/usr/share/man/man1/aclocal.1.gz
/usr/share/man/man1/automake-1.16.1.gz
/usr/share/man/man1/automake.1.gz


%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.16.1
- Initial RPM
