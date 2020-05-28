Name:       python3-urllib3
Version:    1.25.9
Release:    1
Summary:    http library
License:    MIT
Source0:    urllib3-%{version}.tar.gz
Prefix:     /usr

%description
HTTP library with thread-safe connection pooling, file post, and more.

%prep
%setup -n urllib3-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/urllib3/
/usr/lib/python3.7/site-packages/urllib3-1.25.9-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.25.9-1
- Initial rpm package
