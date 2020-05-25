Name:       python3-sphinxcontrib-devhelp
Version:    1.0.2
Release:    1
Summary:    sphinx extension for devhelp
License:    BSD
Source0:    sphinxcontrib-devhelp-%{version}.tar.gz
Prefix:     /usr

%description
sphinx extension which outputs Devhelp document.

%prep
%setup -n sphinxcontrib-devhelp-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/sphinxcontrib/devhelp/
/usr/lib/python3.7/site-packages/sphinxcontrib_devhelp-1.0.2-py3.7-nspkg.pth
/usr/lib/python3.7/site-packages/sphinxcontrib_devhelp-1.0.2-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.0.2
- Initial rpm package
