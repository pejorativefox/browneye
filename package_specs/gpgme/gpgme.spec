Name:       gpgme
Version:    1.11.1
Release:    2
Summary:    High-Level Crypto API for encryption
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
High-Level Crypto API for encryption

%package -n python2-gpgme
Summary: python2 gpgme module
%description -n python2-gpgme
python2 gpgme module

%prep
%setup

%build
export PYTHON_VERSION=3.7
export PYTHON=/bin/python3.7
%configure --disable-gpg-test 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/info/dir
# TODO: this is a terrible kludge and i have no idea why its working this way
cp -r %{buildroot}/usr/lib/python3.7/site-packages/gpg-1.11.1-py3.7-linux-x86_64.egg/gpg \
    %{buildroot}/usr/lib/python3.7/site-packages/

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

%files -n python2-gpgme
/usr/lib/python2.7/site-packages/

%changelog
* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 1.11.1-2
- seperated out the python2 module to allow install without deps.

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.11.1-1
- Initial RPM

