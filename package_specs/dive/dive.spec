Name:       dive
Version:    0.9.2
Release:    1
Summary:    A tool for exploring each layer in a docker image 
License:    MIT
Source0:    %{name}_%{version}_linux_amd64.tar.gz
Prefix:     /usr

%description
A tool for exploring each layer in a docker image 

%prep
%setup -c %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/bin
cp dive %{buildroot}/bin

%files
/bin/dive

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 0.9.2
- Initial RPM

