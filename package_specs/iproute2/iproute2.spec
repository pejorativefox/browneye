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
/usr/share/man/man3/libnetlink.3.gz
/usr/share/man/man7/tc-hfsc.7.gz
/usr/share/man/man8/bridge.8.gz
/usr/share/man/man8/ctstat.8.gz
/usr/share/man/man8/devlink-dev.8.gz
/usr/share/man/man8/devlink-monitor.8.gz
/usr/share/man/man8/devlink-port.8.gz
/usr/share/man/man8/devlink-region.8.gz
/usr/share/man/man8/devlink-resource.8.gz
/usr/share/man/man8/devlink-sb.8.gz
/usr/share/man/man8/devlink.8.gz
/usr/share/man/man8/genl.8.gz
/usr/share/man/man8/ifcfg.8.gz
/usr/share/man/man8/ifstat.8.gz
/usr/share/man/man8/ip-address.8.gz
/usr/share/man/man8/ip-addrlabel.8.gz
/usr/share/man/man8/ip-fou.8.gz
/usr/share/man/man8/ip-gue.8.gz
/usr/share/man/man8/ip-l2tp.8.gz
/usr/share/man/man8/ip-link.8.gz
/usr/share/man/man8/ip-macsec.8.gz
/usr/share/man/man8/ip-maddress.8.gz
/usr/share/man/man8/ip-monitor.8.gz
/usr/share/man/man8/ip-mroute.8.gz
/usr/share/man/man8/ip-neighbour.8.gz
/usr/share/man/man8/ip-netconf.8.gz
/usr/share/man/man8/ip-netns.8.gz
/usr/share/man/man8/ip-ntable.8.gz
/usr/share/man/man8/ip-route.8.gz
/usr/share/man/man8/ip-rule.8.gz
/usr/share/man/man8/ip-sr.8.gz
/usr/share/man/man8/ip-tcp_metrics.8.gz
/usr/share/man/man8/ip-token.8.gz
/usr/share/man/man8/ip-tunnel.8.gz
/usr/share/man/man8/ip-vrf.8.gz
/usr/share/man/man8/ip-xfrm.8.gz
/usr/share/man/man8/ip.8.gz
/usr/share/man/man8/lnstat.8.gz
/usr/share/man/man8/nstat.8.gz
/usr/share/man/man8/rdma-dev.8.gz
/usr/share/man/man8/rdma-link.8.gz
/usr/share/man/man8/rdma-resource.8.gz
/usr/share/man/man8/rdma.8.gz
/usr/share/man/man8/routef.8.gz
/usr/share/man/man8/routel.8.gz
/usr/share/man/man8/rtacct.8.gz
/usr/share/man/man8/rtmon.8.gz
/usr/share/man/man8/rtpr.8.gz
/usr/share/man/man8/rtstat.8.gz
/usr/share/man/man8/ss.8.gz
/usr/share/man/man8/tc-actions.8.gz
/usr/share/man/man8/tc-basic.8.gz
/usr/share/man/man8/tc-bfifo.8.gz
/usr/share/man/man8/tc-bpf.8.gz
/usr/share/man/man8/tc-cake.8.gz
/usr/share/man/man8/tc-cbq-details.8.gz
/usr/share/man/man8/tc-cbq.8.gz
/usr/share/man/man8/tc-cbs.8.gz
/usr/share/man/man8/tc-cgroup.8.gz
/usr/share/man/man8/tc-choke.8.gz
/usr/share/man/man8/tc-codel.8.gz
/usr/share/man/man8/tc-connmark.8.gz
/usr/share/man/man8/tc-csum.8.gz
/usr/share/man/man8/tc-drr.8.gz
/usr/share/man/man8/tc-ematch.8.gz
/usr/share/man/man8/tc-etf.8.gz
/usr/share/man/man8/tc-flow.8.gz
/usr/share/man/man8/tc-flower.8.gz
/usr/share/man/man8/tc-fq.8.gz
/usr/share/man/man8/tc-fq_codel.8.gz
/usr/share/man/man8/tc-fw.8.gz
/usr/share/man/man8/tc-hfsc.8.gz
/usr/share/man/man8/tc-htb.8.gz
/usr/share/man/man8/tc-ife.8.gz
/usr/share/man/man8/tc-matchall.8.gz
/usr/share/man/man8/tc-mirred.8.gz
/usr/share/man/man8/tc-mqprio.8.gz
/usr/share/man/man8/tc-nat.8.gz
/usr/share/man/man8/tc-netem.8.gz
/usr/share/man/man8/tc-pedit.8.gz
/usr/share/man/man8/tc-pfifo.8.gz
/usr/share/man/man8/tc-pfifo_fast.8.gz
/usr/share/man/man8/tc-pie.8.gz
/usr/share/man/man8/tc-police.8.gz
/usr/share/man/man8/tc-prio.8.gz
/usr/share/man/man8/tc-red.8.gz
/usr/share/man/man8/tc-route.8.gz
/usr/share/man/man8/tc-sample.8.gz
/usr/share/man/man8/tc-sfb.8.gz
/usr/share/man/man8/tc-sfq.8.gz
/usr/share/man/man8/tc-simple.8.gz
/usr/share/man/man8/tc-skbedit.8.gz
/usr/share/man/man8/tc-skbmod.8.gz
/usr/share/man/man8/tc-skbprio.8.gz
/usr/share/man/man8/tc-stab.8.gz
/usr/share/man/man8/tc-taprio.8.gz
/usr/share/man/man8/tc-tbf.8.gz
/usr/share/man/man8/tc-tcindex.8.gz
/usr/share/man/man8/tc-tunnel_key.8.gz
/usr/share/man/man8/tc-u32.8.gz
/usr/share/man/man8/tc-vlan.8.gz
/usr/share/man/man8/tc-xt.8.gz
/usr/share/man/man8/tc.8.gz
/usr/share/man/man8/tipc-bearer.8.gz
/usr/share/man/man8/tipc-link.8.gz
/usr/share/man/man8/tipc-media.8.gz
/usr/share/man/man8/tipc-nametable.8.gz
/usr/share/man/man8/tipc-node.8.gz
/usr/share/man/man8/tipc-peer.8.gz
/usr/share/man/man8/tipc-socket.8.gz
/usr/share/man/man8/tipc.8.gz

%changelog
# let's skip this for now
