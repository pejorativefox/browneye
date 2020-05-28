Name:       syslinux
Version:    6.04
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}-pre1.tar.gz
Patch:     syslinux-fix-build-with-glibc-2.25.patch
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0 -n syslinux-6.04-pre1 
%patch -p1

%build
%make_build

%install
rm -rf %{buildroot}
make install INSTALLROOT=%{buildroot}
rm -vf %{buildroot}%{_infodir}/dir*

%files
/sbin/extlinux
/usr/bin/gethostip
/usr/bin/isohybrid
/usr/bin/isohybrid.pl
/usr/bin/keytab-lilo
/usr/bin/lss16toppm
/usr/bin/md5pass
/usr/bin/memdiskfind
/usr/bin/mkdiskimage
/usr/bin/ppmtolss16
/usr/bin/pxelinux-options
/usr/bin/sha1pass
/usr/bin/syslinux
/usr/bin/syslinux2ansi
/usr/man/man1/extlinux.1.gz
/usr/man/man1/gethostip.1.gz
/usr/man/man1/isohybrid.1.gz
/usr/man/man1/lss16toppm.1.gz
/usr/man/man1/memdiskfind.1.gz
/usr/man/man1/ppmtolss16.1.gz
/usr/man/man1/syslinux.1.gz
/usr/man/man1/syslinux2ansi.1.gz

/usr/share/syslinux/

%changelog
# let's skip this for now
