Name:       python3-babel
Version:    2.8.0
Release:    1
Summary:    Python Internationalization Library
License:    Custom
Source0:    babel-%{version}.tar.gz
Prefix:     /usr

%description
Babel is an integrated collection of utilities that assist in internationalizing and localizing Python applications, with an emphasis on web-based applications.

%prep
%setup -n babel-%{version}

%build

%install
rm -rf %{buildroot}
python setup.py import_cldr
python3 setup.py install --root %{buildroot}

%files
/usr/bin/pybabel
/usr/lib/python3.7/site-packages/Babel-2.8.0-py3.7.egg-info/
/usr/lib/python3.7/site-packages/babel/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2.8.0
- Initial rpm package
