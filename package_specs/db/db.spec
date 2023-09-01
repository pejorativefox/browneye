Name:       db
Version:    6.2.32
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
pushd build_unix
../dist/configure --prefix=/usr      \
                  --enable-compat185 \
                  --enable-dbm       \
                  --disable-static   \
                  --enable-cxx
%make_build
popd

%install    
rm -rf %{buildroot}
pushd build_unix
%make_install docdir=/usr/share/doc/db-6.2.32
popd
rm -vf %{buildroot}%{_infodir}/dir*
rm -rf %{buildroot}/usr/share/doc/
%files
/usr/bin/db_archive
/usr/bin/db_checkpoint
/usr/bin/db_convert
/usr/bin/db_deadlock
/usr/bin/db_dump
/usr/bin/db_hotbackup
/usr/bin/db_load
/usr/bin/db_log_verify
/usr/bin/db_printlog
/usr/bin/db_recover
/usr/bin/db_replicate
/usr/bin/db_stat
/usr/bin/db_tuner
/usr/bin/db_upgrade
/usr/bin/db_verify
/usr/include/db.h
/usr/include/db_185.h
/usr/include/db_cxx.h
/usr/lib/libdb-6.2.so
/usr/lib/libdb-6.so
/usr/lib/libdb.so
/usr/lib/libdb_cxx-6.2.so
/usr/lib/libdb_cxx-6.so
/usr/lib/libdb_cxx.so

%changelog
# let's skip this for now
