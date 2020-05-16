Name:       docker
Version:    18.06.3
Release:    3
Summary:    Docker container runtime
License:    GPL
Source0:    %{name}-%{version}-ce.tgz
Source1:    dockerd.conf
Source2:    dockerd.service
Prefix:     /usr

%description


%prep
%setup -n %{name}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin
cp * %{buildroot}/usr/bin

mkdir -pv %{buildroot}/etc/finit.d/available
mkdir -pv %{buildroot}/etc/service.d


cp %{SOURCE1} %{buildroot}/etc/finit.d/available
cp %{SOURCE2} %{buildroot}/etc/service.d/

%files
/usr/bin/docker
/usr/bin/docker-containerd
/usr/bin/docker-containerd-ctr
/usr/bin/docker-containerd-shim
/usr/bin/docker-init
/usr/bin/docker-proxy
/usr/bin/docker-runc
/usr/bin/dockerd
/etc/finit.d/available/dockerd.conf
/etc/service.d/dockerd.service

%changelog
* Thu May 13 2020 Chris Statzer <chris.statzer@qq.com> 3.30.1-3
- Added proper finit init scripts 

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM

