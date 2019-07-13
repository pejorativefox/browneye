Name:       dhcp
Version:    4.4.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
export CFLAGS="$CFLAGS -Wall -fno-strict-aliasing                 \
        -D_PATH_DHCLIENT_SCRIPT='\"/sbin/dhclient-script\"'       \
        -D_PATH_DHCPD_CONF='\"/etc/dhcp/dhcpd.conf\"'             \
        -D_PATH_DHCLIENT_CONF='\"/etc/dhcp/dhclient.conf\"'"

%configure  --prefix=/usr                                           \
            --sysconfdir=/etc/dhcp                                  \
            --localstatedir=/var                                    \
            --with-srv-lease-file=/var/lib/dhcpd/dhcpd.leases       \
            --with-srv6-lease-file=/var/lib/dhcpd/dhcpd6.leases     \
            --with-cli-lease-file=/var/lib/dhclient/dhclient.leases \
            --with-cli6-lease-file=/var/lib/dhclient/dhclient6.leases
%make_build -j1

make -C client install DESTDIR=%{buildroot}

%install    
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
#TODO: from blfs scritps make install-service-dhclient DESTDIR=%{buildroot}
mkdir -pv %{buildroot}/var/lib/dhclient

mkdir -pv %{buildroot}/etc/dhcp
cat > %{buildroot}/etc/dhcp/dhclient.conf << "EOF"
# Begin /etc/dhcp/dhclient.conf
#
# Basic dhclient.conf(5)

#prepend domain-name-servers 127.0.0.1;
request subnet-mask, broadcast-address, time-offset, routers,
        domain-name, domain-name-servers, domain-search, host-name,
        netbios-name-servers, netbios-scope, interface-mtu,
        ntp-servers;
require subnet-mask, domain-name-servers;
#timeout 60;
#retry 60;
#reboot 10;
#select-timeout 5;
#initial-interval 2;

# End /etc/dhcp/dhclient.conf
EOF

mkdir -pv %{buildroot}/etc/sysconfig/
cat > %{buildroot}/etc/sysconfig/ifconfig.eth0 << "EOF"
ONBOOT="yes"
IFACE="eth0"
SERVICE="dhclient"
DHCP_START=""
DHCP_STOP=""

# Set PRINTIP="yes" to have the script print
# the DHCP assigned IP address
PRINTIP="no"

# Set PRINTALL="yes" to print the DHCP assigned values for
# IP, SM, DG, and 1st NS. This requires PRINTIP="yes".
PRINTALL="no"
EOF

rm -vf %{buildroot}%{_infodir}/dir*


%files
/etc/dhcp/dhclient.conf
/etc/sysconfig/ifconfig.eth0
/var/lib/dhclient
/etc/dhcp/dhclient.conf.example
/etc/dhcp/dhcpd.conf.example
/usr/bin/omshell
/usr/include/dhcpctl/dhcpctl.h
/usr/include/omapip/alloc.h
/usr/include/omapip/buffer.h
/usr/include/omapip/convert.h
/usr/include/omapip/hash.h
/usr/include/omapip/isclib.h
/usr/include/omapip/omapip.h
/usr/include/omapip/omapip_p.h
/usr/include/omapip/result.h
/usr/include/omapip/trace.h
/usr/lib64/libdhcp.a
/usr/lib64/libdhcpctl.a
/usr/lib64/libomapi.a
/usr/sbin/dhclient
/usr/sbin/dhcpd
/usr/sbin/dhcrelay
/usr/share/man/man1/omshell.1.gz
/usr/share/man/man3/dhcpctl.3.gz
/usr/share/man/man3/omapi.3.gz
/usr/share/man/man5/dhclient.conf.5.gz
/usr/share/man/man5/dhclient.leases.5.gz
/usr/share/man/man5/dhcp-eval.5.gz
/usr/share/man/man5/dhcp-options.5.gz
/usr/share/man/man5/dhcpd.conf.5.gz
/usr/share/man/man5/dhcpd.leases.5.gz
/usr/share/man/man8/dhclient-script.8.gz
/usr/share/man/man8/dhclient.8.gz
/usr/share/man/man8/dhcpd.8.gz
/usr/share/man/man8/dhcrelay.8.gz


%changelog
# let's skip this for now
