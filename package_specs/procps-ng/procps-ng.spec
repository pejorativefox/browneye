Name:       procps-ng
Version:    3.3.15
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure  --docdir=/usr/share/doc/procps-ng-3.3.15 \
            --disable-static                         \
            --disable-kill

%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/free
/usr/bin/pgrep
/usr/bin/pidof
/usr/bin/pkill
/usr/bin/pmap
/usr/bin/ps
/usr/bin/pwdx
/usr/bin/slabtop
/usr/bin/tload
/usr/bin/top
/usr/bin/uptime
/usr/bin/vmstat
/usr/bin/w
/usr/bin/watch
/usr/include/proc/alloc.h
/usr/include/proc/devname.h
/usr/include/proc/escape.h
/usr/include/proc/numa.h
/usr/include/proc/procps.h
/usr/include/proc/pwcache.h
/usr/include/proc/readproc.h
/usr/include/proc/sig.h
/usr/include/proc/slab.h
/usr/include/proc/sysinfo.h
/usr/include/proc/version.h
/usr/include/proc/wchan.h
/usr/include/proc/whattime.h
/usr/lib64/libprocps.la
/usr/lib64/libprocps.so
/usr/lib64/libprocps.so.7
/usr/lib64/libprocps.so.7.1.0
/usr/lib64/pkgconfig/libprocps.pc
/usr/sbin/sysctl
/usr/share/doc/procps-ng-3.3.15/FAQ
/usr/share/doc/procps-ng-3.3.15/bugs.md
/usr/share/locale/de/LC_MESSAGES/procps-ng.mo
/usr/share/locale/fr/LC_MESSAGES/procps-ng.mo
/usr/share/locale/pl/LC_MESSAGES/procps-ng.mo
/usr/share/locale/pt_BR/LC_MESSAGES/procps-ng.mo
/usr/share/locale/sv/LC_MESSAGES/procps-ng.mo
/usr/share/locale/uk/LC_MESSAGES/procps-ng.mo
/usr/share/locale/vi/LC_MESSAGES/procps-ng.mo
/usr/share/locale/zh_CN/LC_MESSAGES/procps-ng.mo
/usr/share/man/man1/free.1.gz
/usr/share/man/man1/pgrep.1.gz
/usr/share/man/man1/pidof.1.gz
/usr/share/man/man1/pkill.1.gz
/usr/share/man/man1/pmap.1.gz
/usr/share/man/man1/procps.1.gz
/usr/share/man/man1/ps.1.gz
/usr/share/man/man1/pwdx.1.gz
/usr/share/man/man1/slabtop.1.gz
/usr/share/man/man1/tload.1.gz
/usr/share/man/man1/top.1.gz
/usr/share/man/man1/uptime.1.gz
/usr/share/man/man1/w.1.gz
/usr/share/man/man1/watch.1.gz
/usr/share/man/man3/openproc.3.gz
/usr/share/man/man3/readproc.3.gz
/usr/share/man/man3/readproctab.3.gz
/usr/share/man/man5/sysctl.conf.5.gz
/usr/share/man/man8/sysctl.8.gz
/usr/share/man/man8/vmstat.8.gz

%changelog
# let's skip this for now
