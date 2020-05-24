Name:       dnf-plugins-core
Version:    4.0.15
Release:    1
Summary:    Core DNF Plugins 
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Core DNF pluigins providing additional dnf functionality.

%prep
%setup

%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DPYTHON_DESIRED:FILEPATH=/bin/python 
%make_build
make doc-man
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 4.0.15-1
- Initial RPM

