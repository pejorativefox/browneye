Name:       gnupg
Version:    2.2.9
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
rpm -rf %{buildroot}/usr/share/info/dir

%files
/usr/bin/dirmngr
/usr/bin/dirmngr-client
/usr/bin/gpg
/usr/bin/gpg-agent
/usr/bin/gpg-connect-agent
/usr/bin/gpgconf
/usr/bin/gpgparsemail
/usr/bin/gpgscm
/usr/bin/gpgsm
/usr/bin/gpgtar
/usr/bin/gpgv
/usr/bin/kbxutil
/usr/bin/symcryptrun
/usr/bin/watchgnupg
/usr/libexec/gpg-check-pattern
/usr/libexec/gpg-preset-passphrase
/usr/libexec/gpg-protect-tool
/usr/libexec/gpg-wks-client
/usr/libexec/scdaemon
/usr/sbin/addgnupghome
/usr/sbin/applygnupgdefaults
/usr/share/doc/gnupg-2.2.9/*
/usr/share/gnupg/distsigkey.gpg
/usr/share/gnupg/*
/usr/share/info/gnupg.info-1.gz
/usr/share/info/gnupg.info-2.gz
/usr/share/info/gnupg.info.gz
/usr/share/locale/*
/usr/share/man/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.2.9
- Initial RPM

