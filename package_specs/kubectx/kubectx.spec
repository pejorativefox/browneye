Name:       kubectx
Version:    0.7.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz



%description
TODO

%prep
#%setup -a 0

%install
ls
pushd %{name}-%{version}
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin
mkdir -pv %{buildroot}/etc/bash_completion.d/
cp kubectx kubens %{buildroot}/usr/bin
cp completion/*.bash %{buildroot}/etc/bash_completion.d/
popd

%files
/etc/bash_completion.d/kubectx.bash
/etc/bash_completion.d/kubens.bash
/usr/bin/kubectx
/usr/bin/kubens

%changelog
# let's skip this for now
