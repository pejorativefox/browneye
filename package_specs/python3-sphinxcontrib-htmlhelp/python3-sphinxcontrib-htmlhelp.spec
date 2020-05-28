Name:       python3-sphinxcontrib-htmlhelp
Version:    1.0.3
Release:    1
Summary:    sphinx extension which renders HTML help files
License:    BSD
Source0:    sphinxcontrib-htmlhelp-%{version}.tar.gz
Prefix:     /usr

%description
sphinx extension which renders HTML help files

%prep
%setup -n sphinxcontrib-htmlhelp-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/sphinxcontrib/htmlhelp/
/usr/lib/python3.7/site-packages/sphinxcontrib_htmlhelp-1.0.3-py3.7-nspkg.pth
/usr/lib/python3.7/site-packages/sphinxcontrib_htmlhelp-1.0.3-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.0.3
- Initial rpm package
