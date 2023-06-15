Name:       xorriso
Version:    1.5.6
Release:    1
Summary:    ISO 9660 Rock Ridge Filesystem Manipulator for GNU/Linux, FreeBSD, Solaris, NetBSD
License:    GPL-3
Source0:    %{name}-%{version}.pl01.tar.gz
Prefix:     /usr

%description
xorriso copies file objects from POSIX compliant filesystems into Rock Ridge enhanced ISO 9660 filesystems and allows session-wise manipulation of such filesystems. It can load the management information of existing ISO images and it writes the session results to optical media or to filesystem objects. 

%prep
%setup

%build
%configure --disable-launch-frontend \
           --enable-launch-frontend-setuid
%make_build

%install
rm -rf %{buildroot}
%make_install
rm %{buildroot}/usr/bin/xorriso-tcltk
rm %{buildroot}/usr/share/info/dir

%files
/usr/bin/osirrox
/usr/bin/xorrecord
/usr/bin/xorriso
/usr/bin/xorriso-dd-target
#/usr/bin/xorriso-tcltk
/usr/bin/xorrisofs
/usr/share/info/xorrecord.info.gz
/usr/share/info/xorriso-dd-target.info.gz
/usr/share/info/xorriso-tcltk.info.gz
/usr/share/info/xorriso.info.gz
/usr/share/info/xorrisofs.info.gz
/usr/share/man/man1/xorrecord.1.gz
/usr/share/man/man1/xorriso-dd-target.1.gz
/usr/share/man/man1/xorriso-tcltk.1.gz
/usr/share/man/man1/xorriso.1.gz
/usr/share/man/man1/xorrisofs.1.gz

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 1.5.6
- Initial RPM

