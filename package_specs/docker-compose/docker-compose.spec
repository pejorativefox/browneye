Name:       docker-compose
Version:    1.27.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    docker-compose-1.27.0-rc1

%description
Compose is a tool for defining and running multi-container Docker applications.

%prep

%build

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/bin
cp %{SOURCE0} %{buildroot}/bin/docker-compose

%files
/bin/docker-compose

%changelog
* Wed Jan 13 2021 Chris Statzer <chris.statzer@qq.com> 1.27.0
- initial package

