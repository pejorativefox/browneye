Name:       make-ca
Version:    1.2
Release:    4
Summary:    PKI setup script for LFS (and others)
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Source1:    certdata.txt
Prefix:     /usr

Requires:  p11-kit
Requires:  grep
Requires:  sed
Requires:  gawk

%description
PKI setup script for LFS (and others)

%prep
%setup

%build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/etc/ssl
ln -sfv /etc/pki/tls/certs/ca-bundle.crt \
        %{buildroot}/etc/ssl/ca-bundle.crt
mkdir -pv %{buildroot}/share/make-ca/
cp %{SOURCE1} %{buildroot}/share/make-ca

%post
make-ca -C /share/make-ca/certdata.txt

%files
/etc/ssl/ca-bundle.crt
/etc/make-ca.conf.dist
/usr/libexec/make-ca/copy-trust-modifications
/usr/sbin/make-ca
/usr/share/man/man8/make-ca.8.gz
/usr/lib/systemd/system/update-pki.service
/usr/lib/systemd/system/update-pki.timer
/share/make-ca/certdata.txt

%changelog
* Thu May 15 2020 Chris Statzer <chris.statzer@qq.com> 1.2
- Added certdata and post install command to build the certs.

