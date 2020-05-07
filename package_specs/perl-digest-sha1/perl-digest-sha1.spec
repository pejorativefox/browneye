Name:       perl-digest-sha1
Version:    2.13
Release:    1
Summary:    Digest::SHA1 - Perl interface to the SHA-1 algorithm
License:    GPL3
Source0:    Digest-SHA1-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 5.28.1-1

%description
Digest::SHA1 - Perl interface to the SHA-1 algorithm

%prep
%setup -n Digest-SHA1-%{version}

%build
perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name perllocal.pod -delete

%files
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/Digest/SHA1.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/Digest/SHA1/.packlist
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/Digest/SHA1/SHA1.so
/usr/share/man/man3/Digest::SHA1.3.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.44
- Initial RPM

