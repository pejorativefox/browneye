Name:       gpgme
Version:    1.21.0
Release:    1
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

%files
/usr/bin/gpgme-json
/usr/bin/gpgme-tool
/usr/include/gpgme.h
/usr/lib64/
/usr/share/
/usr/include/gpgme++/*
/usr/lib/python3.7/site-packages/*

%files -n python2-gpgme
/usr/lib/python2.7/site-packages/

%changelog
* Wed May 20 2020 Chris Statzer <chris.statzer@qq.com> 1.11.1-2
- seperated out the python2 module to allow install without deps.

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.11.1-1
- Initial RPM

