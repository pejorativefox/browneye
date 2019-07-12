Name:       openssh
Version:    8.0p1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build 
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/scp
/usr/bin/sftp
/usr/bin/ssh
/usr/bin/ssh-add
/usr/bin/ssh-agent
/usr/bin/ssh-keygen
/usr/bin/ssh-keyscan
/usr/etc/moduli
/usr/etc/ssh_config
/usr/etc/sshd_config
/usr/libexec/sftp-server
/usr/libexec/ssh-keysign
/usr/libexec/ssh-pkcs11-helper
/usr/sbin/sshd
/usr/share/man/man1/scp.1.gz
/usr/share/man/man1/sftp.1.gz
/usr/share/man/man1/ssh-add.1.gz
/usr/share/man/man1/ssh-agent.1.gz
/usr/share/man/man1/ssh-keygen.1.gz
/usr/share/man/man1/ssh-keyscan.1.gz
/usr/share/man/man1/ssh.1.gz
/usr/share/man/man5/moduli.5.gz
/usr/share/man/man5/ssh_config.5.gz
/usr/share/man/man5/sshd_config.5.gz
/usr/share/man/man8/sftp-server.8.gz
/usr/share/man/man8/ssh-keysign.8.gz
/usr/share/man/man8/ssh-pkcs11-helper.8.gz
/usr/share/man/man8/sshd.8.gz

%changelog
# let's skip this for now
