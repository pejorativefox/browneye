Name:       python3-chardet
Version:    3.0.4
Release:    1
Summary:    Universal encoding detector for Python 2 and 3
License:    LGPL
Source0:    chardet-%{version}.tar.gz
Prefix:     /usr

%description
Universal encoding detector for Python 2 and 3

%prep
%setup -n chardet-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/chardet-3.0.4-py3.7.egg-info/
/usr/lib/python3.7/site-packages/chardet/
/usr/bin/chardetect

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 3.0.4
- Initial rpm package
