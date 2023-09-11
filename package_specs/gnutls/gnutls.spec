Name:       gnutls
Version:    3.5.19
Release:    1
Summary:    GnuTLS Library.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

BuildRequires: nettle

%description
The GnuTLS package contains libraries and userspace tools which provide a secure 
layer over a reliable transport layer. Currently the GnuTLS library implements 
the proposed standards by the IETF's TLS working group. 

%prep
%setup

%build
%configure    --with-default-trust-store-pkcs11="pkcs11:" \
              --with-included-unistring
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/info/dir

%files
/usr/share/man/*
/usr/share/info/*
/usr/share/locale/*
/usr/share/doc/gnutls/*
/usr/bin/certtool
/usr/bin/gnutls-cli
/usr/bin/gnutls-cli-debug
/usr/bin/gnutls-serv
/usr/bin/ocsptool
/usr/bin/p11tool
/usr/bin/psktool
/usr/bin/srptool
/usr/include/gnutls/*
/usr/lib64/libgnutls.so
/usr/lib64/libgnutls.so.30
/usr/lib64/libgnutls.so.30.14.11
/usr/lib64/libgnutlsxx.so
/usr/lib64/libgnutlsxx.so.28
/usr/lib64/libgnutlsxx.so.28.1.0
/usr/lib64/pkgconfig/gnutls.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.5.19
- Initial RPM

