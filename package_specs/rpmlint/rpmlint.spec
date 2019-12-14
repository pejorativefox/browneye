Name:       rpmlint
Version:    1.11
Release:    1
Summary:    Tool for checking common errors in rpm packages
License:    GPL
Source0:    rpmlint-rpmlint-%{version}.tar.gz
Prefix:     /usr

%description
Tool for checking common errors in rpm packages

%prep
%setup -n rpmlint-rpmlint-%{version}

%build
%make_build

%install
rm -rf %{buildroot}
%make_install DESTDIR=%{buildroot}

%files
/etc/rpmlint/config
/usr/bin/rpmdiff
/usr/bin/rpmlint
/usr/share/bash-completion/completions/rpmdiff
/usr/share/bash-completion/completions/rpmlint
/usr/share/man/man1/rpmdiff.1.gz
/usr/share/man/man1/rpmlint.1.gz
/usr/share/rpmlint/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.11
- Initial RPM

