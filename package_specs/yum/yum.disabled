Name:       yum
Version:    3.4.3
Release:    1
Summary:    Yum package manager
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description


%prep
%setup

%build
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/etc/bash_completion.d/yum.bash
/etc/cron.daily/0yum.cron
/etc/dbus-1/system.d/yum-updatesd.conf
/etc/logrotate.d/yum
/etc/rc.d/init.d/yum-cron
/etc/rc.d/init.d/yum-updatesd
/etc/sysconfig/yum-cron
/etc/yum/version-groups.conf
/etc/yum/yum-daily.yum
/etc/yum/yum-updatesd.conf
/etc/yum/yum-weekly.yum
/etc/yum/yum.conf
/usr/bin/yum
/usr/sbin/yum-updatesd
/usr/lib/python2.7/site-packages/rpmUtils/*
/usr/lib/python2.7/site-packages/yum/*
/usr/share/locale/*
/usr/share/man/*
/usr/share/yum-cli/callback.py
/usr/share/yum-cli/callback.pyc
/usr/share/yum-cli/cli.py
/usr/share/yum-cli/cli.pyc
/usr/share/yum-cli/output.py
/usr/share/yum-cli/output.pyc
/usr/share/yum-cli/shell.py
/usr/share/yum-cli/shell.pyc
/usr/share/yum-cli/utils.py
/usr/share/yum-cli/utils.pyc
/usr/share/yum-cli/yumcommands.py
/usr/share/yum-cli/yumcommands.pyc
/usr/share/yum-cli/yummain.py
/usr/share/yum-cli/yummain.pyc
/usr/share/yum-cli/yumupd.py
/usr/share/yum-cli/yumupd.pyc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Added this sample to help with adding new packages.
