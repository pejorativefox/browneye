Name:       podman-bin
Version:    4.5.1
Release:    1
Summary:    A tool for managing OCI containers and pods
License:    Apache2
Source0:    podman-linux-amd64.tar.gz
Prefix:     /usr

%description
Podman (the POD MANager) is a tool for managing containers and images, volumes mounted into those containers, and pods made from groups of containers.

%prep
%setup -n podman-linux-amd64

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/libexec
cp -r ./usr/local/* %{buildroot}/usr/
cp -r etc %{buildroot}
mv %{buildroot}/usr/lib/podman %{buildroot}/usr/libexec/

%files
/etc/cni/net.d/87-podman-bridge.conflist
/etc/containers/containers.conf
/etc/containers/policy.json
/etc/containers/registries.conf
/etc/containers/storage.conf
/usr/bin/fuse-overlayfs
/usr/bin/fusermount3
/usr/bin/podman
/usr/bin/runc
/usr/bin/slirp4netns
/usr/lib/cni/bridge
/usr/lib/cni/firewall
/usr/lib/cni/host-local
/usr/lib/cni/loopback
/usr/lib/cni/portmap
/usr/lib/cni/tuning
/usr/libexec/podman/catatonit
/usr/libexec/podman/conmon
/usr/libexec/podman/rootlessport

%changelog
* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 4.5.1
- Initial RPM

