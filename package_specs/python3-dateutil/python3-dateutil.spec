Name:       python3-dateutil
Version:    2.8.1
Release:    1
Summary:    Extensions to the standard Python datetime module
License:    BSD
Source0:    python-dateutil-%{version}.tar.gz
Prefix:     /usr

%description
Extensions to the standard Python datetime module

%prep
%setup -n python-dateutil-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/dateutil/
/usr/lib/python3.7/site-packages/python_dateutil-2.8.1-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2.8.1-1
- Initial rpm package
