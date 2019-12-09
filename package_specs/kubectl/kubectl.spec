#https://storage.googleapis.com/kubernetes-release/release/v1.12.10/bin/linux/amd64/kubectl
#http://dspk.xyz/kubectl-1.16.3.tar.gz
Name:       kubectl
Version:    1.16.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz



%description
TODO

%prep
%setup -a 0

%install
ls
pushd %{name}-%{version}
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin
cp kubectl %{buildroot}/usr/bin
popd

%files
/usr/bin/kubectl

%changelog
# let's skip this for now
