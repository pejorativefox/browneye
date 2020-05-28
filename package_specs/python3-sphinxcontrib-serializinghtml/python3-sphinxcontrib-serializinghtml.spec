Name:       python3-sphinxcontrib-serializinghtml
Version:    1.1.4
Release:    1
Summary:    sphinx extension for html
License:    BSD
Source0:    sphinxcontrib-serializinghtml-%{version}.tar.gz
Prefix:     /usr

%description
sphinx extension which outputs "serialized" HTML files (json and pickle).

%prep
%setup -n sphinxcontrib-serializinghtml-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/sphinxcontrib/serializinghtml/
/usr/lib/python3.7/site-packages/sphinxcontrib_serializinghtml-1.1.4-py3.7-nspkg.pth
/usr/lib/python3.7/site-packages/sphinxcontrib_serializinghtml-1.1.4-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.1.4
- Initial rpm package
