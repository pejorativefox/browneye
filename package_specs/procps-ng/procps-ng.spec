Name:       procps-ng
Version:    4.0.3
Release:    1
Summary:    Process monitoring utilities
License:    GPL3
Source0:    procps-ng-%{version}.tar.xz
Prefix:     /usr

%description
The Procps-ng package contains programs for monitoring processes. 

%prep
%setup -q 

%build
%configure  --docdir=/usr/share/doc/procps-ng-%{version} \
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
/usr/bin/pidwait
/usr/include/libproc2/diskstats.h
/usr/include/libproc2/meminfo.h
/usr/include/libproc2/misc.h
/usr/include/libproc2/pids.h
/usr/include/libproc2/slabinfo.h
/usr/include/libproc2/stat.h
/usr/include/libproc2/vmstat.h
/usr/include/libproc2/xtra-procps-debug.h
/usr/lib64/libproc2.so
/usr/lib64/libproc2.so.0
/usr/lib64/libproc2.so.0.0.1
/usr/lib64/pkgconfig/libproc2.pc
/usr/sbin/sysctl
/usr/share/doc/
/usr/share/locale/
/usr/share/man/

%changelog
* Wed Sep 6 Chris Statzer <chris.statzer@gmail.com> 4.0.3-1
- Version bump
