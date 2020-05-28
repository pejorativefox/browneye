Name:       perl-ssleay
Version:    1.88
Release:    1
Summary:    Net::SSLeay - Perl extension for using OpenSSL
License:    Perl5
Source0:    Net-SSLeay-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 5.28.1-1

%description
Net::SSLeay - Perl extension for using OpenSSL

%prep
%setup -n Net-SSLeay-%{version}

%build
PERL_MM_USE_DEFAULT=1 perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name perllocal.pod -delete

%files
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/Net/SSLeay.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/Net/SSLeay.pod
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/Net/SSLeay/Handle.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/Net/*
/usr/share/man/man3/Net::SSLeay.3.gz
/usr/share/man/man3/Net::SSLeay::Handle.3.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.88-1
- Initial RPM

