Name:       linux-pam
Version:    1.3.0
Release:    3
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

%files
/usr/share/locale/*
/usr/share/man/*
/lib/security/*
/usr/etc/environment
/usr/etc/security/*
/usr/include/security/*
/usr/lib64/*
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

