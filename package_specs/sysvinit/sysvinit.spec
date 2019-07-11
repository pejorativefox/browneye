Name:       sysvinit
Version:    2.93
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Patch:      sysvinit-2.93-consolidated-1.patch
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0
%patch -p1

%build
%make_build

%install
rm -rf %{buildroot}


install -m 755 -d %{buildroot}/bin/ %{buildroot}/sbin/
install -m 755 -d %{buildroot}/usr/bin/
for i in ; do \
		install -o root -g root -m 755 src/$i %{buildroot}/bin/ ; \
	done
for i in init halt shutdown runlevel killall5 fstab-decode bootlogd; do \
		install -o root -g root -m 755 src/$i %{buildroot}/sbin/ ; \
	done
for i in ; do \
		install -o root -g root -m 755 $i %{buildroot}/usr/bin/ ; \
	done
install -m 755 -d %{buildroot}/etc/
install -o root -g root -m 755 doc/initscript.sample %{buildroot}/etc/
ln -sf halt %{buildroot}/sbin/reboot
ln -sf halt %{buildroot}/sbin/poweroff
ln -sf init %{buildroot}/sbin/telinit
#ln -sf /sbin/killall5 /bin/pidof
#if [ ! -f /usr/bin/lastb ]; then \
	#	ln -sf last /usr/bin/lastb; \
	#fi
install -m 755 -d %{buildroot}/usr/include/
install -o root -g root -m 644 src/initreq.h %{buildroot}/usr/include/
install -m 755 -d %{buildroot}/usr/share/man/man1/
install -m 755 -d %{buildroot}/usr/share/man/man5/
install -m 755 -d %{buildroot}/usr/share/man/man8/



rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/initscript.sample
/sbin/bootlogd
/sbin/fstab-decode
/sbin/halt
/sbin/init
/sbin/killall5
/sbin/poweroff
/sbin/reboot
/sbin/runlevel
/sbin/shutdown
/sbin/telinit
/usr/include/initreq.h

%changelog
# let's skip this for now
