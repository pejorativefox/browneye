Name:       libnl
Version:    3.4.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/genl-ctrl-list
/usr/bin/idiag-socket-details
/usr/bin/nf-ct-add
/usr/bin/nf-ct-list
/usr/bin/nf-exp-add
/usr/bin/nf-exp-delete
/usr/bin/nf-exp-list
/usr/bin/nf-log
/usr/bin/nf-monitor
/usr/bin/nf-queue
/usr/bin/nl-addr-add
/usr/bin/nl-addr-delete
/usr/bin/nl-addr-list
/usr/bin/nl-class-add
/usr/bin/nl-class-delete
/usr/bin/nl-class-list
/usr/bin/nl-classid-lookup
/usr/bin/nl-cls-add
/usr/bin/nl-cls-delete
/usr/bin/nl-cls-list
/usr/bin/nl-fib-lookup
/usr/bin/nl-link-enslave
/usr/bin/nl-link-ifindex2name
/usr/bin/nl-link-list
/usr/bin/nl-link-name2ifindex
/usr/bin/nl-link-release
/usr/bin/nl-link-set
/usr/bin/nl-link-stats
/usr/bin/nl-list-caches
/usr/bin/nl-list-sockets
/usr/bin/nl-monitor
/usr/bin/nl-neigh-add
/usr/bin/nl-neigh-delete
/usr/bin/nl-neigh-list
/usr/bin/nl-neightbl-list
/usr/bin/nl-pktloc-lookup
/usr/bin/nl-qdisc-add
/usr/bin/nl-qdisc-delete
/usr/bin/nl-qdisc-list
/usr/bin/nl-route-add
/usr/bin/nl-route-delete
/usr/bin/nl-route-get
/usr/bin/nl-route-list
/usr/bin/nl-rule-list
/usr/bin/nl-tctree-list
/usr/bin/nl-util-addr
/usr/etc/libnl/classid
/usr/etc/libnl/pktloc
/usr/include/libnl3/
/usr/lib64/libnl-3.so
/usr/lib64/libnl-3.so.200
/usr/lib64/libnl-3.so.200.26.0
/usr/lib64/libnl-cli-3.so
/usr/lib64/libnl-cli-3.so.200
/usr/lib64/libnl-cli-3.so.200.26.0
/usr/lib64/libnl-genl-3.so
/usr/lib64/libnl-genl-3.so.200
/usr/lib64/libnl-genl-3.so.200.26.0
/usr/lib64/libnl-idiag-3.so
/usr/lib64/libnl-idiag-3.so.200
/usr/lib64/libnl-idiag-3.so.200.26.0
/usr/lib64/libnl-nf-3.so
/usr/lib64/libnl-nf-3.so.200
/usr/lib64/libnl-nf-3.so.200.26.0
/usr/lib64/libnl-route-3.so
/usr/lib64/libnl-route-3.so.200
/usr/lib64/libnl-route-3.so.200.26.0
/usr/lib64/libnl-xfrm-3.so
/usr/lib64/libnl-xfrm-3.so.200
/usr/lib64/libnl-xfrm-3.so.200.26.0
/usr/lib64/libnl/cli/cls/basic.so
/usr/lib64/libnl/cli/cls/cgroup.so
/usr/lib64/libnl/cli/qdisc/bfifo.so
/usr/lib64/libnl/cli/qdisc/blackhole.so
/usr/lib64/libnl/cli/qdisc/fq_codel.so
/usr/lib64/libnl/cli/qdisc/hfsc.so
/usr/lib64/libnl/cli/qdisc/htb.so
/usr/lib64/libnl/cli/qdisc/ingress.so
/usr/lib64/libnl/cli/qdisc/pfifo.so
/usr/lib64/libnl/cli/qdisc/plug.so
/usr/lib64/pkgconfig/libnl-3.0.pc
/usr/lib64/pkgconfig/libnl-cli-3.0.pc
/usr/lib64/pkgconfig/libnl-genl-3.0.pc
/usr/lib64/pkgconfig/libnl-idiag-3.0.pc
/usr/lib64/pkgconfig/libnl-nf-3.0.pc
/usr/lib64/pkgconfig/libnl-route-3.0.pc
/usr/lib64/pkgconfig/libnl-xfrm-3.0.pc
/usr/share/man/man8/genl-ctrl-list.8.gz
/usr/share/man/man8/nl-classid-lookup.8.gz
/usr/share/man/man8/nl-pktloc-lookup.8.gz
/usr/share/man/man8/nl-qdisc-add.8.gz
/usr/share/man/man8/nl-qdisc-delete.8.gz
/usr/share/man/man8/nl-qdisc-list.8.gz

%changelog
# let's skip this for now

