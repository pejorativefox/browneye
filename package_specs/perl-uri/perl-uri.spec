Name:       perl-uri
Version:    1.74
Release:    1
Summary:    Uniform Resource Identifiers
License:    GPL
Source0:    URI-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 5.28.1-1

%description
Uniform Resource Identifiers

%prep
%setup -n URI-%{version}

%build
perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name perllocal.pod -delete

%files
/usr/lib/perl5/site_perl/5.28.1/URI.pm
/usr/lib/perl5/site_perl/5.28.1/URI/*
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/URI/.packlist
/usr/share/man/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.74
- Initial RPM

