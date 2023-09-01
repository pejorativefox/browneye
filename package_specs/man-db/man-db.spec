Name:       man-db
Version:    2.8.5
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

%configure  --docdir=/usr/share/doc/man-db-2.8.5 \
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
/usr/lib64/man-db/libman-2.8.5.so
/usr/lib64/man-db/libman.so
/usr/lib64/man-db/libmandb-2.8.5.so
/usr/lib64/man-db/libmandb.so
/usr/libexec/man-db/globbing
/usr/libexec/man-db/manconv
/usr/libexec/man-db/zsoelim
/usr/sbin/accessdb
/usr/share/doc/man-db-2.8.5/man-db-manual.ps
/usr/share/doc/man-db-2.8.5/man-db-manual.txt
/usr/share/locale/af/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/ast/LC_MESSAGES/man-db.mo
/usr/share/locale/be/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/bg/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/ca/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/ca/LC_MESSAGES/man-db.mo
/usr/share/locale/cs/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/cs/LC_MESSAGES/man-db.mo
/usr/share/locale/da/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/da/LC_MESSAGES/man-db.mo
/usr/share/locale/de/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/de/LC_MESSAGES/man-db.mo
/usr/share/locale/el/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/eo/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/eo/LC_MESSAGES/man-db.mo
/usr/share/locale/es/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/es/LC_MESSAGES/man-db.mo
/usr/share/locale/et/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/eu/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/fi/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/fi/LC_MESSAGES/man-db.mo
/usr/share/locale/fr/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/fr/LC_MESSAGES/man-db.mo
/usr/share/locale/ga/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/gl/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/hu/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/id/LC_MESSAGES/man-db.mo
/usr/share/locale/it/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/it/LC_MESSAGES/man-db.mo
/usr/share/locale/ja/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/ja/LC_MESSAGES/man-db.mo
/usr/share/locale/ko/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/ms/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/nb/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/nl/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/nl/LC_MESSAGES/man-db.mo
/usr/share/locale/pl/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/pl/LC_MESSAGES/man-db.mo
/usr/share/locale/pt/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/pt/LC_MESSAGES/man-db.mo
/usr/share/locale/pt_BR/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/pt_BR/LC_MESSAGES/man-db.mo
/usr/share/locale/ro/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/ro/LC_MESSAGES/man-db.mo
/usr/share/locale/ru/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/ru/LC_MESSAGES/man-db.mo
/usr/share/locale/rw/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/sk/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/sl/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/sr/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/sr/LC_MESSAGES/man-db.mo
/usr/share/locale/sv/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/sv/LC_MESSAGES/man-db.mo
/usr/share/locale/tr/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/tr/LC_MESSAGES/man-db.mo
/usr/share/locale/uk/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/vi/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/vi/LC_MESSAGES/man-db.mo
/usr/share/locale/zh_CN/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/zh_CN/LC_MESSAGES/man-db.mo
/usr/share/locale/zh_TW/LC_MESSAGES/man-db-gnulib.mo
/usr/share/locale/zh_TW/LC_MESSAGES/man-db.mo
/usr/share/man/it/man1/apropos.1.gz
/usr/share/man/it/man1/man.1.gz
/usr/share/man/it/man1/manpath.1.gz
/usr/share/man/it/man1/whatis.1.gz
/usr/share/man/it/man1/zsoelim.1.gz
/usr/share/man/it/man5/manpath.5.gz
/usr/share/man/it/man8/accessdb.8.gz
/usr/share/man/it/man8/catman.8.gz
/usr/share/man/it/man8/mandb.8.gz
/usr/share/man/man1/apropos.1.gz
/usr/share/man/man1/lexgrog.1.gz
/usr/share/man/man1/man.1.gz
/usr/share/man/man1/manconv.1.gz
/usr/share/man/man1/manpath.1.gz
/usr/share/man/man1/whatis.1.gz
/usr/share/man/man1/zsoelim.1.gz
/usr/share/man/man5/manpath.5.gz
/usr/share/man/man8/accessdb.8.gz
/usr/share/man/man8/catman.8.gz
/usr/share/man/man8/mandb.8.gz

%changelog
# let's skip this for now
