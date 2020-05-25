Name:       python3-pytz
Version:    2020.1
Release:    1
Summary:    World timezone definitions, modern and historical
License:    MIT
Source0:    pytz-%{version}.tar.gz
Prefix:     /usr

%description
World timezone definitions, modern and historical

%prep
%setup -n pytz-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/pytz/
/usr/lib/python3.7/site-packages/pytz-2020.1-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2020.1-1
- Initial rpm package
