Name:       net-tools
Version:    1.60
Release:    1
Summary:    Various networking tools
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr
Patch:      net-tools-1.60-gcc34-3.patch
Patch2:      net-tools-1.60-kernel_headers-2.patch
%description
The Net-tools package is a collection of programs for controlling the network subsystem of the Linux kernel. 

%prep
%setup
%patch -p1 
%patch2 -p1

%build
yes "" | make config &&
sed -i -e 's|HAVE_IP_TOOLS 0|HAVE_IP_TOOLS 1|g' \
       -e 's|HAVE_MII 0|HAVE_MII 1|g' config.h &&
sed -i -e 's|# HAVE_IP_TOOLS=0|HAVE_IP_TOOLS=1|g' \
       -e 's|# HAVE_MII=0|HAVE_MII=1|g' config.make

sed -i -e 's|HAVE_HWSTRIP=1|HAVE_HWSTRIP=0|g' \
       -e 's|HAVE_HWTR=1|HAVE_HWTR=0|g' config.make 

sed -i -e 's|HAVE_HWSTRIP 1|HAVE_HWSTRIP 0|g' \
       -e 's|HAVE_HWTR 1|HAVE_HWTR 0|g' config.h

sed -i -e 's|#include <netinet/ip.h>|//#include <netinet/ip.h>|g' iptunnel.c
make

%install
rm -rf %{buildroot}
make BASEDIR=%{buildroot} install

mv %{buildroot}/bin/hostname %{buildroot}/bin/hostname-nt
mv %{buildroot}/bin/dnsdomainname %{buildroot}/bin/dnsdomainname-nt
rm -rf %{buildroot}/usr/share/man

%files
/bin/dnsdomainname-nt
/bin/domainname
/bin/hostname-nt
/bin/netstat
/bin/nisdomainname
/bin/ypdomainname
/sbin/arp
/sbin/ifconfig
/sbin/ipmaddr
/sbin/iptunnel
/sbin/mii-tool
/sbin/nameif
/sbin/plipconfig
/sbin/rarp
/sbin/route
/sbin/slattach

%changelog
* Wed Aug 19 2020 Chris Statzer <chris.statzer@qq.com> 1.60
- Initial RPM

