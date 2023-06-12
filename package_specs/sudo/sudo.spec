Name:       sudo
Version:    1.8.23
Release:    1
Summary:    Sudo 
License:    Give certain users the ability to run some commands as root
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Sudo (su "do") allows a system administrator to delegate authority to give certain users (or groups of users) the ability to run some (or all) commands as root or another user while providing an audit trail of the commands and their arguments.

%prep
%setup

%build
%configure  --prefix=/usr              \
            --libexecdir=/usr/lib      \
            --with-secure-path         \
            --with-all-insults         \
            --with-env-editor          \
            --docdir=/usr/share/doc/sudo-1.8.23 \
            --with-passprompt="[sudo] password for %p: "
%make_build

%install
rm -rf %{buildroot}
#%make_install
make install DESTDIR="$RPM_BUILD_ROOT" install_uid=`id -u` install_gid=`id -g` sudoers_uid=`id -u` sudoers_gid=`id -g`

%post
ln -sfv libsudo_util.so.0.0.0 /usr/lib/sudo/libsudo_util.so.0

%files
/usr/bin/cvtsudoers
/usr/bin/sudo
/usr/bin/sudoedit
/usr/bin/sudoreplay
/usr/etc/sudoers
/usr/etc/sudoers.dist
/usr/include/sudo_plugin.h
/usr/lib/sudo/group_file.la
/usr/lib/sudo/group_file.so
/usr/lib/sudo/libsudo_util.la
/usr/lib/sudo/libsudo_util.so
/usr/lib/sudo/libsudo_util.so.0
/usr/lib/sudo/libsudo_util.so.0.0.0
/usr/lib/sudo/sudo_noexec.la
/usr/lib/sudo/sudo_noexec.so
/usr/lib/sudo/sudoers.la
/usr/lib/sudo/sudoers.so
/usr/lib/sudo/system_group.la
/usr/lib/sudo/system_group.so
/usr/sbin/visudo
/usr/share/doc/sudo-1.8.23/*
/usr/share/man/*
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.8.23
- Initial RPM

