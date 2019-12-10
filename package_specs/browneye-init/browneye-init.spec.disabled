Name:       browneye-init
Version:    0.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    lfs-bootscripts-20180820.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0 -n lfs-bootscripts-20180820

%build


%make_build

%install    
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

cat > %{buildroot}/etc/inittab << "EOF"
# Begin /etc/inittab

id:3:initdefault:

si::sysinit:/etc/rc.d/init.d/rc S

l0:0:wait:/etc/rc.d/init.d/rc 0
l1:S1:wait:/etc/rc.d/init.d/rc 1
l2:2:wait:/etc/rc.d/init.d/rc 2
l3:3:wait:/etc/rc.d/init.d/rc 3
l4:4:wait:/etc/rc.d/init.d/rc 4
l5:5:wait:/etc/rc.d/init.d/rc 5
l6:6:wait:/etc/rc.d/init.d/rc 6

ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now

su:S016:once:/sbin/sulogin

1:2345:respawn:/sbin/agetty --noclear tty1 9600
2:2345:respawn:/sbin/agetty tty2 9600
3:2345:respawn:/sbin/agetty tty3 9600
4:2345:respawn:/sbin/agetty tty4 9600
5:2345:respawn:/sbin/agetty tty5 9600
6:2345:respawn:/sbin/agetty tty6 9600

# End /etc/inittab
EOF

mv %{buildroot}/etc/sysconfig/createfiles %{buildroot}/etc/sysconfig/createfiles-sysv

rm -vf %{buildroot}%{_infodir}/dir*


%files
/etc/inittab
/etc/init.d
/etc/rc.d/init.d/checkfs
/etc/rc.d/init.d/cleanfs
/etc/rc.d/init.d/console
/etc/rc.d/init.d/halt
/etc/rc.d/init.d/localnet
/etc/rc.d/init.d/modules
/etc/rc.d/init.d/mountfs
/etc/rc.d/init.d/mountvirtfs
/etc/rc.d/init.d/network
/etc/rc.d/init.d/rc
/etc/rc.d/init.d/reboot
/etc/rc.d/init.d/sendsignals
/etc/rc.d/init.d/setclock
/etc/rc.d/init.d/swap
/etc/rc.d/init.d/sysctl
/etc/rc.d/init.d/sysklogd
/etc/rc.d/init.d/template
/etc/rc.d/init.d/udev
/etc/rc.d/init.d/udev_retry
/etc/rc.d/rc0.d/K80network
/etc/rc.d/rc0.d/K90sysklogd
/etc/rc.d/rc0.d/S60sendsignals
/etc/rc.d/rc0.d/S65swap
/etc/rc.d/rc0.d/S70mountfs
/etc/rc.d/rc0.d/S90localnet
/etc/rc.d/rc0.d/S99halt
/etc/rc.d/rc1.d/K80network
/etc/rc.d/rc1.d/K90sysklogd
/etc/rc.d/rc2.d/K80network
/etc/rc.d/rc2.d/K90sysklogd
/etc/rc.d/rc3.d/S10sysklogd
/etc/rc.d/rc3.d/S20network
/etc/rc.d/rc4.d/S10sysklogd
/etc/rc.d/rc4.d/S20network
/etc/rc.d/rc5.d/S10sysklogd
/etc/rc.d/rc5.d/S20network
/etc/rc.d/rc6.d/K80network
/etc/rc.d/rc6.d/K90sysklogd
/etc/rc.d/rc6.d/S60sendsignals
/etc/rc.d/rc6.d/S65swap
/etc/rc.d/rc6.d/S70mountfs
/etc/rc.d/rc6.d/S90localnet
/etc/rc.d/rc6.d/S99reboot
/etc/rc.d/rcS.d/S00mountvirtfs
/etc/rc.d/rcS.d/S05modules
/etc/rc.d/rcS.d/S08localnet
/etc/rc.d/rcS.d/S10udev
/etc/rc.d/rcS.d/S20swap
/etc/rc.d/rcS.d/S30checkfs
/etc/rc.d/rcS.d/S40mountfs
/etc/rc.d/rcS.d/S45cleanfs
/etc/rc.d/rcS.d/S50udev_retry
/etc/rc.d/rcS.d/S70console
/etc/rc.d/rcS.d/S90sysctl
/etc/sysconfig/createfiles-sysv
/etc/sysconfig/modules
/etc/sysconfig/rc.site
/etc/sysconfig/udev_retry
/lib/lsb
/lib/services/init-functions
/lib/services/ipv4-static
/lib/services/ipv4-static-route
/sbin/ifdown
/sbin/ifup
/usr/share/man/man8/ifdown.8.gz
/usr/share/man/man8/ifup.8.gz

%changelog
# let's skip this for now
