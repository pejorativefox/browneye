Name:       man-db
Version:    2.11.2
Release:    1
Summary:    Man page utilities
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The Man-DB package contains programs for finding and viewing man pages.

%prep
%setup -q

%build

%configure  --docdir=/usr/share/doc/man-db-%{version} \
            --sysconfdir=/etc                    \
            --disable-setuid                     \
            --enable-cache-owner=bin             \
            --with-browser=/usr/bin/lynx         \
            --with-vgrind=/usr/bin/vgrind        \
            --with-grap=/usr/bin/grap            \
            --with-systemdtmpfilesdir=           \
            --with-systemdsystemunitdir=
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/man_db.conf
/usr/bin/apropos
/usr/bin/catman
/usr/bin/lexgrog
/usr/bin/man
/usr/bin/mandb
/usr/bin/manpath
/usr/bin/whatis
/usr/bin/man-recode
/usr/lib64/man-db/libman-%{version}.so
/usr/lib64/man-db/libman.so
/usr/lib64/man-db/libmandb-%{version}.so
/usr/lib64/man-db/libmandb.so
/usr/libexec/man-db/globbing
/usr/libexec/man-db/manconv
/usr/libexec/man-db/zsoelim
/usr/sbin/accessdb
/usr/share/doc/
/usr/share/locale/
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.11.12-1
- Version bump
