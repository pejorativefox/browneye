Name:       iproute2
Version:    6.4.0
Release:    1
Summary:    kernel networking tool
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
iproute2 is a collection of userspace utilities for controlling and monitoring various aspects of networking in the Linux kernel

%prep
%setup -q

%build
sed -i /ARPD/d Makefile
rm -fv man/man8/arpd.8
%make_build NETNS_RUN_DIR=/run/netns

%install
rm -rf %{buildroot}
%make_install SBINDIR=/usr/sbin
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
/usr/sbin/bridge
/usr/sbin/ctstat
/usr/sbin/genl
/usr/sbin/ifstat
/usr/sbin/ip
/usr/sbin/lnstat
/usr/sbin/nstat
/usr/sbin/routel
/usr/sbin/rtacct
/usr/sbin/rtmon
/usr/sbin/rtstat
/usr/sbin/ss
/usr/sbin/tc
/usr/lib/tc/experimental.dist
/usr/lib/tc/normal.dist
/usr/lib/tc/pareto.dist
/usr/lib/tc/paretonormal.dist
/usr/share/bash-completion/completions/devlink
/usr/include/iproute2/bpf_elf.h
/usr/share/bash-completion/completions/tc
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 6.4.0-1
- Version bump
