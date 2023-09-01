Name:       gnupg
Version:    2.4.3
Release:    1
Summary:    GNU's tool for secure communication and data storage.
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
GNU's tool for secure communication and data storage.

%prep
%setup

%build
%configure --enable-symcryptrun     \
           --docdir=/usr/share/doc/gnupg-2.2.9
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/info/dir

%files
/usr/bin/dirmngr
/usr/bin/dirmngr-client
/usr/bin/gpg*
/usr/bin/kbxutil
/usr/bin/watchgnupg
/usr/libexec/gpg*
/usr/libexec/scdaemon
/usr/libexec/dirmngr_ldap
/usr/sbin/addgnupghome
/usr/sbin/applygnupgdefaults
/usr/share/doc/gnupg-2.2.9/*
/usr/share/gnupg/distsigkey.gpg
/usr/share/gnupg/*
/usr/share/info/gnu*
/usr/share/locale/*
/usr/share/man/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.2.9
- Initial RPM

