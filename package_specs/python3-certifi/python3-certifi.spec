Name:       python3-certifi
Version:    2020.4.5.1
Release:    1
Summary:    Python package for providing Mozilla's CA Bundle.
License:    Mozilla
Source0:    certifi-%{version}.tar.gz
Prefix:     /usr

%description
Python package for providing Mozilla's CA Bundle.

%prep
%setup -n certifi-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/certifi-2020.4.5.1-py3.7.egg-info/
/usr/lib/python3.7/site-packages/certifi/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2020.4.5.1-1
- Initial rpm package
