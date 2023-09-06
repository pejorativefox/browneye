%define perl_ver 5.38.0

Name:       xml-parser
Version:    2.46
Release:    1
Summary:    Perl module for parsing XML documents 
License:    GPL3
Source0:    XML-Parser-%{version}.tar.gz
Prefix:     /usr

%description
Perl module for parsing XML documents 

%prep
%setup -q -n XML-Parser-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
rm -f %{buildroot}/usr/lib64/perl5/5.28.1/x86_64-linux-thread-multi/perllocal.pod

%files
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser.pm
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/Japanese_Encodings.msg
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/README
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/big5.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/euc-kr.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/ibm866.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/iso-8859-15.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/iso-8859-2.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/iso-8859-3.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/iso-8859-4.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/iso-8859-5.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/iso-8859-7.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/iso-8859-8.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/iso-8859-9.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/koi8-r.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/windows-1250.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/windows-1251.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/windows-1252.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/windows-1255.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/x-euc-jp-jisx0221.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/x-euc-jp-unicode.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/x-sjis-cp932.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/x-sjis-jdk117.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/x-sjis-jisx0221.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Encodings/x-sjis-unicode.enc
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Expat.pm
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/LWPExternEnt.pl
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Style/Debug.pm
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Style/Objects.pm
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Style/Stream.pm
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Style/Subs.pm
/usr/lib64/perl5/5.38.0/vendor_perl/XML/Parser/Style/Tree.pm
/usr/lib64/perl5/5.38.0/vendor_perl/auto/XML/Parser/Expat/Expat.so
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 5.38
- Version bump
