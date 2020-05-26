Name:       python3-sphinxcontrib-qthelp
Version:    1.0.3
Release:    1
Summary:    sphinx module for qthelp files
License:    BSD
Source0:    sphinxcontrib-qthelp-%{version}.tar.gz
Prefix:     /usr

%description
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.

%prep
%setup -n sphinxcontrib-qthelp-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/sphinxcontrib/
/usr/lib/python3.7/site-packages/sphinxcontrib_qthelp-1.0.3-py3.7-nspkg.pth
/usr/lib/python3.7/site-packages/sphinxcontrib_qthelp-1.0.3-py3.7.egg-info/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.0.3
- Initial rpm package
