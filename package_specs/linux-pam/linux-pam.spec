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
	   --includedir=%{_includedir}/security
%make_build

%install
rm -rf %{buildroot}
%make_install

chmod -v 4755 %{buildroot}/usr/sbin/unix_chkpwd

install -v -m755 -d %{buildroot}/etc/pam.d

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
/lib/security/pam_access.la
/lib/security/pam_access.so
/lib/security/pam_debug.la
/lib/security/pam_debug.so
/lib/security/pam_deny.la
/lib/security/pam_deny.so
/lib/security/pam_echo.la
/lib/security/pam_echo.so
/lib/security/pam_env.la
/lib/security/pam_env.so
/lib/security/pam_exec.la
/lib/security/pam_exec.so
/lib/security/pam_faildelay.la
/lib/security/pam_faildelay.so
/lib/security/pam_filter.la
/lib/security/pam_filter.so
/lib/security/pam_filter/upperLOWER
/lib/security/pam_ftp.la
/lib/security/pam_ftp.so
/lib/security/pam_group.la
/lib/security/pam_group.so
/lib/security/pam_issue.la
/lib/security/pam_issue.so
/lib/security/pam_keyinit.la
/lib/security/pam_keyinit.so
/lib/security/pam_lastlog.la
/lib/security/pam_lastlog.so
/lib/security/pam_limits.la
/lib/security/pam_limits.so
/lib/security/pam_listfile.la
/lib/security/pam_listfile.so
/lib/security/pam_localuser.la
/lib/security/pam_localuser.so
/lib/security/pam_loginuid.la
/lib/security/pam_loginuid.so
/lib/security/pam_mail.la
/lib/security/pam_mail.so
/lib/security/pam_mkhomedir.la
/lib/security/pam_mkhomedir.so
/lib/security/pam_motd.la
/lib/security/pam_motd.so
/lib/security/pam_namespace.la
/lib/security/pam_namespace.so
/lib/security/pam_nologin.la
/lib/security/pam_nologin.so
/lib/security/pam_permit.la
/lib/security/pam_permit.so
/lib/security/pam_pwhistory.la
/lib/security/pam_pwhistory.so
/lib/security/pam_rhosts.la
/lib/security/pam_rhosts.so
/lib/security/pam_rootok.la
/lib/security/pam_rootok.so
/lib/security/pam_securetty.la
/lib/security/pam_securetty.so
/lib/security/pam_shells.la
/lib/security/pam_shells.so
/lib/security/pam_stress.la
/lib/security/pam_stress.so
/lib/security/pam_succeed_if.la
/lib/security/pam_succeed_if.so
/lib/security/pam_tally.la
/lib/security/pam_tally.so
/lib/security/pam_tally2.la
/lib/security/pam_tally2.so
/lib/security/pam_time.la
/lib/security/pam_time.so
/lib/security/pam_timestamp.la
/lib/security/pam_timestamp.so
/lib/security/pam_umask.la
/lib/security/pam_umask.so
/lib/security/pam_unix.la
/lib/security/pam_unix.so
/lib/security/pam_userdb.la
/lib/security/pam_userdb.so
/lib/security/pam_warn.la
/lib/security/pam_warn.so
/lib/security/pam_wheel.la
/lib/security/pam_wheel.so
/lib/security/pam_xauth.la
/lib/security/pam_xauth.so
/usr/etc/environment
/usr/etc/security/access.conf
/usr/etc/security/group.conf
/usr/etc/security/limits.conf
/usr/etc/security/namespace.conf
/usr/etc/security/namespace.init
/usr/etc/security/pam_env.conf
/usr/etc/security/time.conf
/usr/include/security/_pam_compat.h
/usr/include/security/_pam_macros.h
/usr/include/security/_pam_types.h
/usr/include/security/pam_appl.h
/usr/include/security/pam_client.h
/usr/include/security/pam_ext.h
/usr/include/security/pam_filter.h
/usr/include/security/pam_misc.h
/usr/include/security/pam_modules.h
/usr/include/security/pam_modutil.h
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

