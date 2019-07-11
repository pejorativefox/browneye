Name:       gzip
Version:    1.10
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build

%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/gunzip
/usr/bin/gzexe
/usr/bin/gzip
/usr/bin/uncompress
/usr/bin/zcat
/usr/bin/zcmp
/usr/bin/zdiff
/usr/bin/zegrep
/usr/bin/zfgrep
/usr/bin/zforce
/usr/bin/zgrep
/usr/bin/zless
/usr/bin/zmore
/usr/bin/znew
/usr/share/info/gzip.info.gz
/usr/share/man/man1/gunzip.1.gz
/usr/share/man/man1/gzexe.1.gz
/usr/share/man/man1/gzip.1.gz
/usr/share/man/man1/zcat.1.gz
/usr/share/man/man1/zcmp.1.gz
/usr/share/man/man1/zdiff.1.gz
/usr/share/man/man1/zforce.1.gz
/usr/share/man/man1/zgrep.1.gz
/usr/share/man/man1/zless.1.gz
/usr/share/man/man1/zmore.1.gz
/usr/share/man/man1/znew.1.gz

%changelog
# let's skip this for now
