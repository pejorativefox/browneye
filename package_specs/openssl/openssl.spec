Name:       openssl
Version:    1.1.1a
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 0:5.004, libc.so.6()(64bit), libcrypto.so.1.1()(64bit), libdl.so.2()(64bit), libpthread.so.0()(64bit), libssl.so.1.1()(64bit)


%description
TODO

%prep
%setup

%build
./config --prefix=/usr         \
         --openssldir=/etc/ssl \
         shared                \
         zlib-dynamic
%make_build

%install
rm -rf %{buildroot}
sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
rm -rf %{buildroot}/usr/share/doc/openssl
rm -rf %{buildroot}/usr/share/man

%files
/etc/ssl/ct_log_list.cnf
/etc/ssl/ct_log_list.cnf.dist
/etc/ssl/misc/CA.pl
/etc/ssl/misc/tsget
/etc/ssl/misc/tsget.pl
/etc/ssl/openssl.cnf
/etc/ssl/openssl.cnf.dist
/usr/bin/c_rehash
/usr/bin/openssl
/usr/include/openssl/*
/usr/lib64/engines-1.1/afalg.so
/usr/lib64/engines-1.1/capi.so
/usr/lib64/engines-1.1/padlock.so
/usr/lib64/libcrypto.so
/usr/lib64/libcrypto.so.1.1
/usr/lib64/libssl.so
/usr/lib64/libssl.so.1.1
/usr/lib64/pkgconfig/libcrypto.pc
/usr/lib64/pkgconfig/libssl.pc
/usr/lib64/pkgconfig/openssl.pc

%changelog
# let's skip this for now
