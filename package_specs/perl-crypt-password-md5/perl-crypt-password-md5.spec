Name:       perl-crypt-password-md5
Version:    1.40
Release:    1
Summary:    Crypt::PasswdMD5 - Provide interoperable MD5-based crypt() functions
License:    GPL 
Source0:    Crypt-PasswdMD5-%{version}.tgz
Prefix:     /usr

AutoReq: no

Requires: perl >= 5.28.1-1

%description
Crypt::PasswdMD5 - Provide interoperable MD5-based crypt() functions

%prep
%setup -n Crypt-PasswdMD5-%{version}

%build
perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name perllocal.pod -delete

%files
/usr/lib/perl5/site_perl/5.28.1/Crypt/PasswdMD5.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/Crypt/PasswdMD5/.packlist
/usr/share/man/man3/Crypt::PasswdMD5.3.gz

%changelog
* Thu May 07 2020 Chris Statzer <chris.statzer@qq.com> 1.40
- Initial RPM

