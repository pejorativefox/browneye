Name:       python3-sphinxcontrib-jsmath
Version:    1.0.1
Release:    1
Summary:    sphinx math extension
License:    BSD
Source0:    sphinxcontrib-jsmath-%{version}.tar.gz
Prefix:     /usr

%description
A sphinx extension which renders display math in HTML via JavaScript

%prep
%setup -n sphinxcontrib-jsmath-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/sphinxcontrib/jsmath/
/usr/lib/python3.7/site-packages/sphinxcontrib_jsmath-1.0.1-py3.7-nspkg.pth
/usr/lib/python3.7/site-packages/sphinxcontrib_jsmath-1.0.1-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.0.1
- Initial rpm package
