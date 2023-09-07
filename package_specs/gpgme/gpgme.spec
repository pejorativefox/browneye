Name:       gpgme
Version:    1.21.0
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
export PYTHON_VERSION=3.11
export PYTHON=/bin/python3.11
%configure --disable-gpg-test 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/info/dir
ln -sfv gpg-1.21.0-py3.11-linux-x86_64.egg/gpg/ %{buildroot}/usr/lib64/python3.11/site-packages/gpg

%files
/usr/bin/gpgme-json
/usr/bin/gpgme-tool
/usr/include/gpgme.h
/usr/bin/gpgme-config
/usr/lib64/cmake/Gpgmepp/GpgmeppConfig.cmake
/usr/lib64/cmake/Gpgmepp/GpgmeppConfigVersion.cmake
/usr/lib64/libgpgme.so
/usr/lib64/libgpgme.so.11
/usr/lib64/libgpgme.so.11.30.0
/usr/lib64/libgpgmepp.so
/usr/lib64/libgpgmepp.so.6
/usr/lib64/libgpgmepp.so.6.18.0
/usr/lib64/pkgconfig/gpgme-glib.pc
/usr/lib64/pkgconfig/gpgme.pc
/usr/share/
/usr/include/gpgme++/*
/usr/lib64/python3.11/site-packages/

%changelog
* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 1.11.1-2
- seperated out the python2 module to allow install without deps.

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.11.1-1
- Initial RPM

