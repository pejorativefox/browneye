Name:       linux-pam
Version:    1.3.0
Release:    2 
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

cat > %{buildroot}/etc/pam.d/other << "EOF"
# Begin /etc/pam.d/other

auth            required        pam_unix.so     nullok
account         required        pam_unix.so
session         required        pam_unix.so
password        required        pam_unix.so     nullok

# End /etc/pam.d/otheruth     required       pam_deny.so
EOF

%files
/usr/share/locale/*
/usr/share/man/*
/etc/pam.d/other
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

