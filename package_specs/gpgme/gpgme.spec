Name:       gpgme
Version:    1.11.1
Release:    1
Summary:    High-Level Crypto API for encryption
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
High-Level Crypto API for encryption

%prep
%setup

%build
export PYTHON_VERSION=3
%configure --disable-gpg-test 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/info/dir

%files
/usr/bin/gpgme-config
/usr/bin/gpgme-json
/usr/bin/gpgme-tool
/usr/include/gpgme.h
/usr/lib64/cmake/Gpgmepp/GpgmeppConfig.cmake
/usr/lib64/cmake/Gpgmepp/GpgmeppConfigVersion.cmake
/usr/lib64/libgpgme.la
/usr/lib64/libgpgme.so
/usr/lib64/libgpgme.so.11
/usr/lib64/libgpgme.so.11.20.1
/usr/lib64/libgpgmepp.la
/usr/lib64/libgpgmepp.so
/usr/lib64/libgpgmepp.so.6
/usr/lib64/libgpgmepp.so.6.7.0
/usr/share/aclocal/gpgme.m4
/usr/share/common-lisp/source/gpgme/gpgme-package.lisp
/usr/share/common-lisp/source/gpgme/gpgme.asd
/usr/share/common-lisp/source/gpgme/gpgme.lisp
/usr/share/info/gpgme.info-1.gz
/usr/share/info/gpgme.info-2.gz
/usr/share/info/gpgme.info.gz
/usr/include/gpgme++/*
/usr/lib/python3.7/site-packages/*
/usr/lib/python2.7/site-packages/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.11.1
- Initial RPM

