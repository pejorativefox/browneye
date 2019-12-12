Name:       iptables
Version:    1.8.0
Release:    1
Summary:    Firewall tool
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Firewall tool

%prep
%setup

%build
sed -i -e '/libebt_/s/^/#/' \
       -e '/libarpt_/s/^/#/' extensions/GNUmakefile.in

%configure  --prefix=/usr      \
            --sbindir=/sbin    \
            --disable-nftables \
            --enable-libipq    \
            --with-xtlibdir=/lib/xtables
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/lib/xtables/libip6t_DNAT.so
/lib/xtables/libip6t_DNPT.so
/lib/xtables/libip6t_HL.so
/lib/xtables/libip6t_LOG.so
/lib/xtables/libip6t_MASQUERADE.so
/lib/xtables/libip6t_NETMAP.so
/lib/xtables/libip6t_REDIRECT.so
/lib/xtables/libip6t_REJECT.so
/lib/xtables/libip6t_SNAT.so
/lib/xtables/libip6t_SNPT.so
/lib/xtables/libip6t_ah.so
/lib/xtables/libip6t_dst.so
/lib/xtables/libip6t_eui64.so
/lib/xtables/libip6t_frag.so
/lib/xtables/libip6t_hbh.so
/lib/xtables/libip6t_hl.so
/lib/xtables/libip6t_icmp6.so
/lib/xtables/libip6t_ipv6header.so
/lib/xtables/libip6t_mh.so
/lib/xtables/libip6t_rt.so
/lib/xtables/libip6t_srh.so
/lib/xtables/libipt_CLUSTERIP.so
/lib/xtables/libipt_DNAT.so
/lib/xtables/libipt_ECN.so
/lib/xtables/libipt_LOG.so
/lib/xtables/libipt_MASQUERADE.so
/lib/xtables/libipt_NETMAP.so
/lib/xtables/libipt_REDIRECT.so
/lib/xtables/libipt_REJECT.so
/lib/xtables/libipt_SNAT.so
/lib/xtables/libipt_TTL.so
/lib/xtables/libipt_ULOG.so
/lib/xtables/libipt_ah.so
/lib/xtables/libipt_icmp.so
/lib/xtables/libipt_realm.so
/lib/xtables/libipt_ttl.so
/lib/xtables/libxt_AUDIT.so
/lib/xtables/libxt_CHECKSUM.so
/lib/xtables/libxt_CLASSIFY.so
/lib/xtables/libxt_CONNMARK.so
/lib/xtables/libxt_CONNSECMARK.so
/lib/xtables/libxt_CT.so
/lib/xtables/libxt_DSCP.so
/lib/xtables/libxt_HMARK.so
/lib/xtables/libxt_IDLETIMER.so
/lib/xtables/libxt_LED.so
/lib/xtables/libxt_MARK.so
/lib/xtables/libxt_NFLOG.so
/lib/xtables/libxt_NFQUEUE.so
/lib/xtables/libxt_NOTRACK.so
/lib/xtables/libxt_RATEEST.so
/lib/xtables/libxt_SECMARK.so
/lib/xtables/libxt_SET.so
/lib/xtables/libxt_SYNPROXY.so
/lib/xtables/libxt_TCPMSS.so
/lib/xtables/libxt_TCPOPTSTRIP.so
/lib/xtables/libxt_TEE.so
/lib/xtables/libxt_TOS.so
/lib/xtables/libxt_TPROXY.so
/lib/xtables/libxt_TRACE.so
/lib/xtables/libxt_addrtype.so
/lib/xtables/libxt_bpf.so
/lib/xtables/libxt_cgroup.so
/lib/xtables/libxt_cluster.so
/lib/xtables/libxt_comment.so
/lib/xtables/libxt_connbytes.so
/lib/xtables/libxt_connlimit.so
/lib/xtables/libxt_connmark.so
/lib/xtables/libxt_conntrack.so
/lib/xtables/libxt_cpu.so
/lib/xtables/libxt_dccp.so
/lib/xtables/libxt_devgroup.so
/lib/xtables/libxt_dscp.so
/lib/xtables/libxt_ecn.so
/lib/xtables/libxt_esp.so
/lib/xtables/libxt_hashlimit.so
/lib/xtables/libxt_helper.so
/lib/xtables/libxt_ipcomp.so
/lib/xtables/libxt_iprange.so
/lib/xtables/libxt_ipvs.so
/lib/xtables/libxt_length.so
/lib/xtables/libxt_limit.so
/lib/xtables/libxt_mac.so
/lib/xtables/libxt_mangle.so
/lib/xtables/libxt_mark.so
/lib/xtables/libxt_multiport.so
/lib/xtables/libxt_nfacct.so
/lib/xtables/libxt_osf.so
/lib/xtables/libxt_owner.so
/lib/xtables/libxt_physdev.so
/lib/xtables/libxt_pkttype.so
/lib/xtables/libxt_policy.so
/lib/xtables/libxt_quota.so
/lib/xtables/libxt_rateest.so
/lib/xtables/libxt_recent.so
/lib/xtables/libxt_rpfilter.so
/lib/xtables/libxt_sctp.so
/lib/xtables/libxt_set.so
/lib/xtables/libxt_socket.so
/lib/xtables/libxt_standard.so
/lib/xtables/libxt_state.so
/lib/xtables/libxt_statistic.so
/lib/xtables/libxt_string.so
/lib/xtables/libxt_tcp.so
/lib/xtables/libxt_tcpmss.so
/lib/xtables/libxt_time.so
/lib/xtables/libxt_tos.so
/lib/xtables/libxt_u32.so
/lib/xtables/libxt_udp.so
/sbin/ip6tables
/sbin/ip6tables-legacy
/sbin/ip6tables-legacy-restore
/sbin/ip6tables-legacy-save
/sbin/ip6tables-restore
/sbin/ip6tables-save
/sbin/iptables
/sbin/iptables-legacy
/sbin/iptables-legacy-restore
/sbin/iptables-legacy-save
/sbin/iptables-restore
/sbin/iptables-save
/sbin/xtables-legacy-multi
/usr/bin/iptables-xml
/usr/include/libipq.h
/usr/include/libiptc/ipt_kernel_headers.h
/usr/include/libiptc/libip6tc.h
/usr/include/libiptc/libiptc.h
/usr/include/libiptc/libxtc.h
/usr/include/libiptc/xtcshared.h
/usr/include/xtables-version.h
/usr/include/xtables.h
/usr/lib64/libip4tc.la
/usr/lib64/libip4tc.so
/usr/lib64/libip4tc.so.0
/usr/lib64/libip4tc.so.0.1.0
/usr/lib64/libip6tc.la
/usr/lib64/libip6tc.so
/usr/lib64/libip6tc.so.0
/usr/lib64/libip6tc.so.0.1.0
/usr/lib64/libipq.la
/usr/lib64/libipq.so
/usr/lib64/libipq.so.0
/usr/lib64/libipq.so.0.0.0
/usr/lib64/libiptc.la
/usr/lib64/libiptc.so
/usr/lib64/libiptc.so.0
/usr/lib64/libiptc.so.0.0.0
/usr/lib64/libxtables.la
/usr/lib64/libxtables.so
/usr/lib64/libxtables.so.12
/usr/lib64/libxtables.so.12.0.0
/usr/lib64/pkgconfig/libip4tc.pc
/usr/lib64/pkgconfig/libip6tc.pc
/usr/lib64/pkgconfig/libipq.pc
/usr/lib64/pkgconfig/libiptc.pc
/usr/lib64/pkgconfig/xtables.pc
/usr/share/man/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.8.0
- Initial RPM

