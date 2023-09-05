Name:       python-flit-core
Version:    3.9.0
Release:    1
Summary:    Python packaging utility (core)
License:    BSD
Source0:    flit_core-%{version}.tar.gz
Prefix:     /usr

%description
Flit is a simple way to put Python packages and modules on PyPI. 

%prep
%setup -n flit_core-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/lib64/python3.11/site-packages/
cp -rv flit_core %{buildroot}/usr/lib64/python3.11/site-packages/

%files
/usr/lib64/python3.11/site-packages/flit_core/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Initial RPM

