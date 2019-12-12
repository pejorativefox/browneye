Name:       docker
Version:    18.06.3
Release:    1
Summary:    Docker container runtime
License:    GPL
Source0:    %{name}-%{version}-ce.tgz
Prefix:     /usr

%description


%prep
%setup -n %{name}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin
cp * %{buildroot}/usr/bin

%files
/usr/bin/docker
/usr/bin/docker-containerd
/usr/bin/docker-containerd-ctr
/usr/bin/docker-containerd-shim
/usr/bin/docker-init
/usr/bin/docker-proxy
/usr/bin/docker-runc
/usr/bin/dockerd

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM

