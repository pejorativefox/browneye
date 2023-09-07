Name:       python-packaging
Version:    19.2
Release:    1
Summary:    Core utilities for Python packages
License:    GPL
Source0:    packaging-%{version}.tar.gz
Prefix:     /usr

%description
Core utilities for Python packages

%prep
%setup -n packaging-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%files
/usr/lib64/python3.11/site-packages/

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 19.2
- Initial rpm package
