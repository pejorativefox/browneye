Name:       sqlite3
Version:    3.24.0
Release:    1
Summary:    SQLlite database engine.
License:    GPL
Source0:    sqlite-autoconf-3240000.tar.gz
Prefix:     /usr

%description
The SQLite package is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. 

%prep
%setup -n sqlite-autoconf-3240000

%build
%configure  --disable-static  \
            --enable-fts{4,5} \
            CPPFLAGS="-DSQLITE_ENABLE_COLUMN_METADATA=1 \
                      -DSQLITE_ENABLE_UNLOCK_NOTIFY=1   \
                      -DSQLITE_ENABLE_DBSTAT_VTAB=1     \
                      -DSQLITE_SECURE_DELETE=1          \
                      -DSQLITE_ENABLE_FTS3_TOKENIZER=1
                      -DSQLITE_DISABLE_DIRSYNC=1 \
                      -DSQLITE_ENABLE_FTS3_PARENTHESIS=1 \
                      -DSQLITE_ENABLE_DBPAGE_VTAB \
		      -Wall -fno-strict-aliasing"
        
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/sqlite3
/usr/include/sqlite3.h
/usr/include/sqlite3ext.h
/usr/lib64/libsqlite3.so
/usr/lib64/libsqlite3.so.0
/usr/lib64/libsqlite3.so.0.8.6
/usr/lib64/pkgconfig/sqlite3.pc
/usr/share/man/man1/sqlite3.1.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 324
- Initial RPM

