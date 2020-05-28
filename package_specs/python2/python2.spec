Name:       python2
Version:    2.7.15
Release:    3
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    Python-%{version}.tar.xz

Provides: /bin/python2

AutoReq: no

Requires: /bin/sh /usr/bin/env /usr/bin/pkg-config /usr/bin/python2.7 libbz2.so.1.0()(64bit) libc.so.6()(64bit) libc.so.6(GLIBC_2.14)(64bit) libc.so.6(GLIBC_2.2.5)(64bit) libc.so.6(GLIBC_2.28)(64bit) libc.so.6(GLIBC_2.3)(64bit) libc.so.6(GLIBC_2.3.2)(64bit) libc.so.6(GLIBC_2.7)(64bit) libcrypt.so.1()(64bit) libcrypt.so.1(GLIBC_2.2.5)(64bit) libcrypto.so.1.1()(64bit) libcrypto.so.1.1(OPENSSL_1_1_0)(64bit) libdl.so.2()(64bit) libdl.so.2(GLIBC_2.2.5)(64bit) libexpat.so.1()(64bit) libffi.so.6()(64bit) libgdbm.so.6()(64bit) libgdbm_compat.so.4()(64bit) libm.so.6()(64bit) libm.so.6(GLIBC_2.2.5)(64bit) libm.so.6(GLIBC_2.29)(64bit) libncursesw.so.6()(64bit) libpanelw.so.6()(64bit) libpthread.so.0()(64bit) libpthread.so.0(GLIBC_2.2.5)(64bit) libpython2.7.so.1.0()(64bit) libreadline.so.8()(64bit) libsqlite3.so.0()(64bit) libssl.so.1.1()(64bit) libssl.so.1.1(OPENSSL_1_1_0)(64bit) libutil.so.1()(64bit) libutil.so.1(GLIBC_2.2.5)(64bit) libz.so.1()(64bit) libz.so.1(ZLIB_1.2.0)(64bit) python(abi) = 2.7


%description
TODO

%prep
%setup -n Python-%{version}

%build
%configure  --enable-shared     \
            --with-system-expat \
            --with-system-ffi   \
            --without-ensurepip \
            --enable-unicode=ucs4
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm %{buildroot}/usr/bin/2to3
rm -rf %{buildroot}/usr/lib/python2.7/test
rm %{buildroot}/usr/bin/python

%files
/usr/bin/idle
/usr/bin/pydoc
/usr/bin/python-config
/usr/bin/python2
/usr/bin/python2-config
/usr/bin/python2.7
/usr/bin/python2.7-config
/usr/bin/smtpd.py
/usr/lib64/python2.7/lib-dynload/_sqlite3.so
/usr/include/python2.7/
/usr/lib/python2.7/
/usr/lib64/libpython2.7.so
/usr/lib64/libpython2.7.so.1.0
/usr/lib64/pkgconfig/python-2.7.pc
/usr/lib64/pkgconfig/python.pc
/usr/lib64/pkgconfig/python2.pc
/usr/lib64/python2.7/
/usr/share/man/man1/python.1.gz
/usr/share/man/man1/python2.1.gz
/usr/share/man/man1/python2.7.1.gz

%changelog
# let's skip this for now

