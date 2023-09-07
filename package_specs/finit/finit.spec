
Name:       finit
Version:    4.4
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
TODO

%prep
%setup -q

%build
%configure --enable-dbus-plugin --enable-rw-rootfs --enable-progress 
%make_build

%install
#rm -rf %{buildroot}
%make_install

%files
/usr/sbin/finit
/usr/sbin/halt
/usr/sbin/init
/usr/sbin/initctl
/usr/sbin/poweroff
/usr/sbin/reboot
/usr/sbin/shutdown
/usr/sbin/suspend
/usr/sbin/telinit
/usr/include/finit/cgroup.h
/usr/include/finit/cond.h
/usr/include/finit/conf.h
/usr/include/finit/finit.h
/usr/include/finit/helpers.h
/usr/include/finit/log.h
/usr/include/finit/plugin.h
/usr/include/finit/service.h
/usr/include/finit/svc.h
/usr/lib64/finit/plugins/bootmisc.so
/usr/lib64/finit/plugins/dbus.so
/usr/lib64/finit/plugins/modprobe.so
/usr/lib64/finit/plugins/netlink.so
/usr/lib64/finit/plugins/pidfile.so
/usr/lib64/finit/plugins/procps.so
/usr/lib64/finit/plugins/rtc.so
/usr/lib64/finit/plugins/sys.so
/usr/lib64/finit/plugins/tty.so
/usr/lib64/finit/plugins/urandom.so
/usr/lib64/finit/plugins/usr.so
/usr/lib64/finit/rescue.conf
/usr/lib64/finit/sample.conf
/usr/lib64/finit/system/hotplug.conf
/usr/lib64/finit/tmpfiles.d/finit.conf
/usr/lib64/tmpfiles.d/dnsmasq.conf
/usr/lib64/tmpfiles.d/etc.conf
/usr/lib64/tmpfiles.d/frr.conf
/usr/lib64/tmpfiles.d/legacy.conf
/usr/lib64/tmpfiles.d/lldpd.conf
/usr/lib64/tmpfiles.d/openswan.conf
/usr/lib64/tmpfiles.d/quagga.conf
/usr/lib64/tmpfiles.d/sshd.conf
/usr/lib64/tmpfiles.d/uuidd.conf
/usr/lib64/tmpfiles.d/var.conf
/usr/lib64/tmpfiles.d/x11.conf
/usr/libexec/finit/getty
/usr/libexec/finit/logit
/usr/share/doc/finit/
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 4.4-1
- Version bump
