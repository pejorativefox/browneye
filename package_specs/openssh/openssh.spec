Name:       openssh
Version:    8.0p1
Release:    5
Summary:    OpenSSH is the premier connectivity tool for remote login with the SSH protocol. 
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Source1:    sshd_config
Source2:    sshd-service.conf
Source3:    make_sshd_keys
Prefix:     /usr

%description
OpenSSH is the premier connectivity tool for remote login with the SSH protocol.
 
%prep
%setup

%build 
%configure --sysconfdir=/etc
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

rm %{buildroot}/etc/sshd_config
mkdir -pv %{buildroot}/etc/
cp -v %{SOURCE1} %{buildroot}/etc/sshd_config

mkdir -pv %{buildroot}/etc/finit.d/available
cp %{SOURCE2} %{buildroot}/etc/finit.d/available/sshd.conf

mkdir -pv %{buildroot}/sbin
cp %{SOURCE3} %{buildroot}/sbin

%post
install  -v -m700 -d /var/lib/sshd &&
chown    -v root:sys /var/lib/sshd &&

groupadd -g 50 sshd        &&
useradd  -c 'sshd PrivSep' \
         -d /var/lib/sshd  \
         -g sshd           \
         -s /bin/false     \
         -u 50 sshd
make_sshd_keys

%files
/usr/bin/scp
/usr/bin/sftp
/usr/bin/ssh
/usr/bin/ssh-add
/usr/bin/ssh-agent
/usr/bin/ssh-keygen
/usr/bin/ssh-keyscan
/etc/moduli
/etc/ssh_config
/usr/libexec/sftp-server
/usr/libexec/ssh-keysign
/usr/libexec/ssh-pkcs11-helper
/usr/sbin/sshd
/usr/share/man/*
/etc/finit.d/available/sshd.conf
/etc/sshd_config
/sbin/make_sshd_keys

%changelog
* Fri Jun 16 2023 Chris Statzer <chris.statzer@gmail.com> 8.0p1-5
- Renamed service destination file to follow the naming scheme

* Thu May 14 2020 Chris Statzer <chris.statzer@qq.com> 8.0p1
- Added finit services and a default configuration

