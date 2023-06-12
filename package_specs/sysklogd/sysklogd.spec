Name:       sysklogd
Version:    1.5.1
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
sed -i '/Error loading kernel symbols/{n;n;d}' ksym_mod.c
sed -i 's/union wait/int/' syslogd.c

%make_build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/share/man/man8/
mkdir -pv %{buildroot}/usr/share/man/man5/
mkdir -pv %{buildroot}/etc/
mkdir -pv %{buildroot}/usr/sbin/
#/usr/bin/install -o root -g root -m 644 sysklogd.8 %{buildroot}/usr/share/man/man8/sysklogd.8
##/usr/bin/install -o root -g root -m 644 syslogd.8 %{buildroot}/usr/share/man/man8/syslogd.8
#/usr/bin/install -o root -g root -m 644 syslog.conf.5 %{buildroot}/usr/share/man/man5/syslog.conf.5
#/usr/bin/install -o root -g root -m 644 klogd.8 %{buildroot}/usr/share/man/man8/klogd.8
/usr/bin/install -m 500 -s syslogd %{buildroot}/usr/sbin/syslogd
/usr/bin/install -m 500 -s klogd %{buildroot}/usr/sbin/klogd

rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/etc

cat > %{buildroot}/etc/syslog.conf << "EOF"
# Begin /etc/syslog.conf

auth,authpriv.* -/var/log/auth.log
*.*;auth,authpriv.none -/var/log/sys.log
daemon.* -/var/log/daemon.log
kern.* -/var/log/kern.log
mail.* -/var/log/mail.log
user.* -/var/log/user.log
*.emerg *

# End /etc/syslog.conf
EOF

%files
/etc/syslog.conf
/usr/sbin/klogd
/usr/sbin/syslogd
#/usr/share/man/man5/syslog.conf.5.gz
#/usr/share/man/man8/klogd.8.gz
#/usr/share/man/man8/sysklogd.8.gz
#/usr/share/man/man8/syslogd.8.gz

%changelog
# let's skip this for now
