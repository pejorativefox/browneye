Name:       perl-io-sockets-ssl
Version:    2.068
Release:    1
Summary:    Perl IO::Socket::SSL - SSL sockets with IO::Socket interface
License:    Perl5
Source0:    IO-Socket-SSL-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 5.28.1-1

%description
Perl IO::Socket::SSL - SSL sockets with IO::Socket interface

%prep
%setup -n IO-Socket-SSL-%{version}

%build
SKIP_RNG_TEST=1 PERL_MM_USE_DEFAULT=1 perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name perllocal.pod -delete

%files
/usr/lib/perl5/site_perl/5.28.1/IO/Socket/SSL.pm
/usr/lib/perl5/site_perl/5.28.1/IO/Socket/SSL.pod
/usr/lib/perl5/site_perl/5.28.1/IO/Socket/SSL/Intercept.pm
/usr/lib/perl5/site_perl/5.28.1/IO/Socket/SSL/PublicSuffix.pm
/usr/lib/perl5/site_perl/5.28.1/IO/Socket/SSL/Utils.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/IO/Socket/SSL/.packlist
/usr/share/man/man3/IO::Socket::SSL.3.gz
/usr/share/man/man3/IO::Socket::SSL::Intercept.3.gz
/usr/share/man/man3/IO::Socket::SSL::PublicSuffix.3.gz
/usr/share/man/man3/IO::Socket::SSL::Utils.3.gz

%changelog
* Mon May 18 2020 Chris Statzer <chris.statzer@qq.com> 2.068-1
- Initial RPM

