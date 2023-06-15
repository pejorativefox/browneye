Name:       mtools
Version:    4.0.43
Release:    1
Summary:    Mtools is a collection of utilities to access MS-DOS disks from GNU and Unix without mounting them.
License:    GPL-3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Mtools is a collection of utilities to access MS-DOS disks from GNU and Unix without mounting them.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
rm %{buildroot}/usr/share/info/dir

%files
/usr/bin/amuFormat.sh
/usr/bin/floppyd
/usr/bin/floppyd_installtest
/usr/bin/lz
/usr/bin/mattrib
/usr/bin/mbadblocks
/usr/bin/mcat
/usr/bin/mcd
/usr/bin/mcheck
/usr/bin/mcomp
/usr/bin/mcopy
/usr/bin/mdel
/usr/bin/mdeltree
/usr/bin/mdir
/usr/bin/mdu
/usr/bin/mformat
/usr/bin/minfo
/usr/bin/mkmanifest
/usr/bin/mlabel
/usr/bin/mmd
/usr/bin/mmount
/usr/bin/mmove
/usr/bin/mpartition
/usr/bin/mrd
/usr/bin/mren
/usr/bin/mshortname
/usr/bin/mshowfat
/usr/bin/mtools
/usr/bin/mtoolstest
/usr/bin/mtype
/usr/bin/mxtar
/usr/bin/mzip
/usr/bin/tgz
/usr/bin/uz
/usr/share/info/mtools.info.gz
/usr/share/man/man1/
/usr/share/man/man5/

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

