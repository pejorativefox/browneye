Name:       openssl
Version:    3.1.2
Release:    1
Summary:    OpenSSL software library
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

AutoReq: no

Requires: perl >= 0:5.004, libc.so.6()(64bit), libcrypto.so.1.1()(64bit), libdl.so.2()(64bit), libpthread.so.0()(64bit), libssl.so.1.1()(64bit)


%description
OpenSSL is a software library for applications that provide secure communications over computer networks 

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
%make_install MANSUFFIX=ssl
rm -vf %{buildroot}%{_infodir}/dir*
rm -rf %{buildroot}/usr/share/doc/openssl
rm -rf %{buildroot}/usr/share/man

%files
/usr/include/openssl/
/etc/ssl/ct_log_list.cnf
/etc/ssl/ct_log_list.cnf.dist
/etc/ssl/misc/CA.pl
/etc/ssl/misc/tsget
/etc/ssl/misc/tsget.pl
/etc/ssl/openssl.cnf
/etc/ssl/openssl.cnf.dist
/usr/bin/c_rehash
/usr/bin/openssl
/usr/lib64/engines-3/afalg.so                                                                                                                                                                         
/usr/lib64/engines-3/capi.so                                                                                                                                                                          
/usr/lib64/engines-3/loader_attic.so                                                                                                                                                                  
/usr/lib64/engines-3/padlock.so                                                                                                                                                                       
/usr/lib64/libcrypto.so                                                                                                                                                                               
/usr/lib64/libcrypto.so.3                                                                                                                                                                             
/usr/lib64/libssl.so                                                                                                                                                                                  
/usr/lib64/libssl.so.3                                                                                                                                                                                
/usr/lib64/ossl-modules/legacy.so                                                                                                                                                                     
/usr/lib64/pkgconfig/libcrypto.pc                                                                                                                                                                     
/usr/lib64/pkgconfig/libssl.pc                                                                                                                                                                        
/usr/lib64/pkgconfig/openssl.pc

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 3.1.2-1
- Version bump
