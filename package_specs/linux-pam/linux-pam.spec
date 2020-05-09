Name:       linux-pam
Version:    1.3.0
Release:    1
Summary:    PAM (Pluggable Authentication Modules) library
License:    GPL2
Source0:    Linux-PAM-%{version}.tar.bz2
Prefix:     /usr

%description
PAM (Pluggable Authentication Modules) library

%prep
%setup -n Linux-PAM-%{version}

%build
%configure --enable-securedir=/lib/security \
	   --includedir=%{_includedir}/security \
           --disable-selinux
%make_build

%install
rm -rf %{buildroot}
%make_install

chmod -v 4755 %{buildroot}/usr/sbin/unix_chkpwd

install -v -m755 -d %{buildroot}/etc/pam.d

cat > %{buildroot}/etc/pam.d/system-account << "EOF"
account   required    pam_unix.so
EOF


cat > %{buildroot}/etc/pam.d/system-auth << "EOF"
auth      required    pam_unix.so
EOF


cat > %{buildroot}/etc/pam.d/system-session << "EOF"
session   required    pam_unix.so
EOF

cat > %{buildroot}/etc/pam.d/useradd << "EOF"
auth      sufficient  pam_rootok.so

# include system auth, account, and session settings
auth      include     system-auth
account   include     system-account
session   include     system-session

# Always permit for authentication updates
password  required    pam_permit.so
EOF

cat > %{buildroot}/etc/pam.d/groupadd << "EOF"
auth      sufficient  pam_rootok.so

# include system auth, account, and session settings
auth      include     system-auth
account   include     system-account
session   include     system-session

# Always permit for authentication updates
password  required    pam_permit.so
EOF

cat > %{buildroot}/etc/pam.d/other << "EOF"
auth     required       pam_deny.so
account  required       pam_deny.so
password required       pam_deny.so
session  required       pam_deny.so
EOF



%files
/usr/share/locale/*
/usr/share/man/*
/etc/pam.d/other
/etc/pam.d/groupadd
/etc/pam.d/system-account
/etc/pam.d/system-auth
/etc/pam.d/system-session
/etc/pam.d/useradd
/lib/security/*
/usr/etc/environment
/usr/etc/security/*
/usr/include/security/*
/usr/lib64/libpam.la
/usr/lib64/libpam.so
/usr/lib64/libpam.so.0
/usr/lib64/libpam.so.0.84.2
/usr/lib64/libpam_misc.la
/usr/lib64/libpam_misc.so
/usr/lib64/libpam_misc.so.0
/usr/lib64/libpam_misc.so.0.82.1
/usr/lib64/libpamc.la
/usr/lib64/libpamc.so
/usr/lib64/libpamc.so.0
/usr/lib64/libpamc.so.0.82.1
/usr/sbin/mkhomedir_helper
/usr/sbin/pam_tally
/usr/sbin/pam_tally2
/usr/sbin/pam_timestamp_check
/usr/sbin/unix_chkpwd
/usr/sbin/unix_update
/usr/share/doc/Linux-PAM/draft-morgan-pam-current.txt
/usr/share/doc/Linux-PAM/index.html
/usr/share/doc/Linux-PAM/rfc86.0.txt

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.3.0
- Initial RPM

