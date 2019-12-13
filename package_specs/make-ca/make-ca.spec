Name:       make-ca
Version:    1.2
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
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

%files
/etc/ssl/ca-bundle.crt
/etc/make-ca.conf.dist
/usr/libexec/make-ca/copy-trust-modifications
/usr/sbin/make-ca
/usr/share/man/man8/make-ca.8.gz
/usr/lib/systemd/system/update-pki.service
/usr/lib/systemd/system/update-pki.timer

%changelog
# let's skip this for now
