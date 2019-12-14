Name:       iproute2
Version:    4.20.0
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
sed -i /ARPD/d Makefile
rm -fv man/man8/arpd.8
sed -i 's/.m_ipt.o//' tc/Makefile
%make_build

%install
rm -rf %{buildroot}
%make_install DOCDIR=/usr/share/doc/iproute2-4.20.0
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/iproute2/bpf_pinning
/etc/iproute2/ematch_map
/etc/iproute2/group
/etc/iproute2/nl_protos
/etc/iproute2/rt_dsfield
/etc/iproute2/rt_protos
/etc/iproute2/rt_realms
/etc/iproute2/rt_scopes
/etc/iproute2/rt_tables
/sbin/arpd
/sbin/bridge
/sbin/ctstat
/sbin/genl
/sbin/ifcfg
/sbin/ifstat
/sbin/ip
/sbin/lnstat
/sbin/nstat
/sbin/routef
/sbin/routel
/sbin/rtacct
/sbin/rtmon
/sbin/rtpr
/sbin/rtstat
/sbin/ss
/sbin/tc
/usr/include/iproute2/bpf_elf.h
/usr/lib/tc/experimental.dist
/usr/lib/tc/normal.dist
/usr/lib/tc/pareto.dist
/usr/lib/tc/paretonormal.dist
/usr/lib/tc/m_ipt.so
/usr/lib/tc/m_xt.so
/usr/share/bash-completion/completions/tc
/usr/share/doc/iproute2-4.20.0/examples/README.cbq
/usr/share/doc/iproute2-4.20.0/examples/README.iproute2+tc
/usr/share/doc/iproute2-4.20.0/examples/SYN-DoS.rate.limit
/usr/share/doc/iproute2-4.20.0/examples/cbqinit.eth1
/usr/share/doc/iproute2-4.20.0/examples/diffserv/Edge1
/usr/share/doc/iproute2-4.20.0/examples/diffserv/Edge2
/usr/share/doc/iproute2-4.20.0/examples/diffserv/Edge31-ca-u32
/usr/share/doc/iproute2-4.20.0/examples/diffserv/Edge31-cb-chains
/usr/share/doc/iproute2-4.20.0/examples/diffserv/Edge32-ca-u32
/usr/share/doc/iproute2-4.20.0/examples/diffserv/Edge32-cb-chains
/usr/share/doc/iproute2-4.20.0/examples/diffserv/Edge32-cb-u32
/usr/share/doc/iproute2-4.20.0/examples/diffserv/README
/usr/share/doc/iproute2-4.20.0/examples/diffserv/afcbq
/usr/share/doc/iproute2-4.20.0/examples/diffserv/ef-prio
/usr/share/doc/iproute2-4.20.0/examples/diffserv/efcbq
/usr/share/doc/iproute2-4.20.0/examples/diffserv/regression-testing
/usr/share/doc/iproute2-4.20.0/examples/gaiconf
/usr/share/man/*

%changelog
# let's skip this for now
