Name:       python3-alabaster
Version:    0.7.12
Release:    1
Summary:    Sphinx theme
License:    Custom
Source0:    alabaster-%{version}.tar.gz
Prefix:     /usr

%description
Lightweight, configurable Sphinx theme. Now the Sphinx default!

%prep
%setup -n alabaster-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/alabaster-0.7.12-py3.7.egg-info/
/usr/lib/python3.7/site-packages/alabaster/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 0.7.12-1
- Initial rpm package
