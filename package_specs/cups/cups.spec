Name:       cups
Version:    2.3.3
Release:    1
Summary:    Open source printing system
License:    Apache
Source0:    %{name}-%{version}-source.tar.gz
Prefix:     /usr

%description
CUPS is a standards-based, open source printing system developed by Apple Inc.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
make install-exec DESTDIR=$RPM_BUILD_ROOT
make install-libs DESTDIR=$RPM_BUILD_ROOT

%files
/usr/bin/cancel
/usr/bin/cupstestppd
/usr/bin/ippeveprinter
/usr/bin/ipptool
/usr/bin/lp
/usr/bin/lpoptions
/usr/bin/lpq
/usr/bin/lpr
/usr/bin/lprm
/usr/bin/lpstat
/usr/bin/ppdc
/usr/bin/ppdhtml
/usr/bin/ppdi
/usr/bin/ppdmerge
/usr/bin/ppdpo
/usr/lib/cups/backend/http
/usr/lib/cups/backend/https
/usr/lib/cups/backend/ipp
/usr/lib/cups/backend/ipps
/usr/lib/cups/backend/lpd
/usr/lib/cups/backend/snmp
/usr/lib/cups/backend/socket
/usr/lib/cups/backend/usb
/usr/lib/cups/cgi-bin/admin.cgi
/usr/lib/cups/cgi-bin/classes.cgi
/usr/lib/cups/cgi-bin/help.cgi
/usr/lib/cups/cgi-bin/jobs.cgi
/usr/lib/cups/cgi-bin/printers.cgi
/usr/lib/cups/command/ippevepcl
/usr/lib/cups/command/ippeveps
/usr/lib/cups/daemon/cups-deviced
/usr/lib/cups/daemon/cups-driverd
/usr/lib/cups/daemon/cups-exec
/usr/lib/cups/daemon/cups-lpd
/usr/lib/cups/filter/commandtops
/usr/lib/cups/filter/gziptoany
/usr/lib/cups/filter/pstops
/usr/lib/cups/filter/rastertoepson
/usr/lib/cups/filter/rastertohp
/usr/lib/cups/filter/rastertolabel
/usr/lib/cups/filter/rastertopwg
/usr/lib/cups/monitor/bcp
/usr/lib/cups/monitor/tbcp
/usr/lib/cups/notifier/dbus
/usr/lib/cups/notifier/mailto
/usr/lib/cups/notifier/rss
/usr/lib64/libcups.so
/usr/lib64/libcups.so.2
/usr/lib64/libcupsimage.so
/usr/lib64/libcupsimage.so.2
/usr/sbin/cupsaccept
/usr/sbin/cupsctl
/usr/sbin/cupsd
/usr/sbin/cupsdisable
/usr/sbin/cupsenable
/usr/sbin/cupsfilter
/usr/sbin/cupsreject
/usr/sbin/lpadmin
/usr/sbin/lpc
/usr/sbin/lpinfo
/usr/sbin/lpmove

%changelog
* Fri Sep 04 2020 Chris Statzer <chris.statzer@qq.com> 2.3.3
- Initial RPM

