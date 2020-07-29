Name:       gotop
Version:    3.0.0
Release:    1
Summary:    A terminal based graphical activity monitor inspired by gtop and vtop 
License:    GPL
Source0:    %{name}_%{version}_linux_amd64.tgz
Prefix:     /usr

%description
A terminal based graphical activity monitor inspired by gtop and vtop 

%prep
%setup -c %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/bin/
cp gotop %{buildroot}/bin/

%files
/bin/gotop

%changelog
* Fri Jun 12 2020 Chris Statzer <chris.statzer@qq.com> 3.0.0
- Initial RPM

