Name:       perl-dbi
Version:    1.642
Release:    1
Summary:    Perl's Database Interface
License:    GPL
Source0:    DBI-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 5.28.1-1

%description
Perl's Database Interface

%prep
%setup -n DBI-%{version}

%build
perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name perllocal.pod -delete

%files
/usr/bin/dbilogstrip
/usr/bin/dbiprof
/usr/bin/dbiproxy
/usr/lib/perl5/site_perl/*
/usr/share/man/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.642
- Initial RPM

