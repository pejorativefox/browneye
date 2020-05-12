Name:       make-ca
Version:    1.2
Release:    3
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Source1:    certdata.txt
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

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
# let's skip this for now
