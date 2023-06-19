Name:       inetutils
Version:    1.9.4
Release:    1
Summary:    Collection of common network programs.
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Collection of common network programs.

%prep
%setup -q -a0

%build
%configure  --localstatedir=/var \
            --disable-logger     \
            --disable-whois      \
            --disable-rcp        \
            --disable-rexec      \
            --disable-rlogin     \
            --disable-rsh        \
            --disable-servers
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/dnsdomainname
/usr/bin/ftp
/usr/bin/hostname
/usr/bin/ifconfig
/usr/bin/ping
/usr/bin/ping6
/usr/bin/telnet
/usr/bin/tftp
/usr/bin/traceroute
/usr/share/info/inetutils.info.gz
/usr/share/man/man1/dnsdomainname.1.gz
/usr/share/man/man1/ftp.1.gz
/usr/share/man/man1/hostname.1.gz
/usr/share/man/man1/ifconfig.1.gz
/usr/share/man/man1/ping.1.gz
/usr/share/man/man1/ping6.1.gz
/usr/share/man/man1/telnet.1.gz
/usr/share/man/man1/tftp.1.gz
/usr/share/man/man1/traceroute.1.gz

%changelog
* Mon Jun 19 2023 Chris Statzer <chris.statzer@gmail.com> 1.9.4
- Removed the talk binary as it's no longer being built.
