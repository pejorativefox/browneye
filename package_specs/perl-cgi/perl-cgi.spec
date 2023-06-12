Name:       perl-cgi
Version:    4.57
Release:    1
Summary:    Perl CGI module
License:    Artistic License 2.0
Source0:    CGI-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 5.28.1-1

%description
Perl CGI module

%prep
%setup -n CGI-%{version}

%build
perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name perllocal.pod -delete

%files
/usr/lib/perl5/site_perl/5.28.1/CGI.pm
/usr/lib/perl5/site_perl/5.28.1/CGI.pod
/usr/lib/perl5/site_perl/5.28.1/CGI/Carp.pm
/usr/lib/perl5/site_perl/5.28.1/CGI/Cookie.pm
/usr/lib/perl5/site_perl/5.28.1/CGI/File/Temp.pm
/usr/lib/perl5/site_perl/5.28.1/CGI/HTML/Functions.pm
/usr/lib/perl5/site_perl/5.28.1/CGI/HTML/Functions.pod
/usr/lib/perl5/site_perl/5.28.1/CGI/Pretty.pm
/usr/lib/perl5/site_perl/5.28.1/CGI/Push.pm
/usr/lib/perl5/site_perl/5.28.1/CGI/Util.pm
/usr/lib/perl5/site_perl/5.28.1/Fh.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/CGI/.packlist
/usr/share/man/man3/CGI.3.gz
/usr/share/man/man3/CGI::Carp.3.gz
/usr/share/man/man3/CGI::Cookie.3.gz
/usr/share/man/man3/CGI::HTML::Functions.3.gz
/usr/share/man/man3/CGI::Pretty.3.gz
/usr/share/man/man3/CGI::Push.3.gz
/usr/share/man/man3/CGI::Util.3.gz

%changelog
* Mon Jun 12 2023 Chris Statzer <chris.statzer@gmail.com> 4.57
- Version Bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.44
- Initial RPM

