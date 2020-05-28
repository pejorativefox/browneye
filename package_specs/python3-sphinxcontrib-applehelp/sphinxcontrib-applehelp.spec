Name:       python3-sphinxcontrib-applehelp
Version:    1.0.2
Release:    1
Summary:    sphinx extension for apple help
License:    BSD
Source0:    sphinxcontrib-applehelp-%{version}.tar.gz
Prefix:     /usr

%description
sphinx extension which outputs Apple help books

%prep
%setup -n sphinxcontrib-applehelp-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/sphinxcontrib/applehelp/
/usr/lib/python3.7/site-packages/sphinxcontrib_applehelp-1.0.2-py3.7-nspkg.pth
/usr/lib/python3.7/site-packages/sphinxcontrib_applehelp-1.0.2-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.0.2-1
- Initial rpm package
