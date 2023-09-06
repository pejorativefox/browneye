Name:       python-pip
Version:    23.2.1
Release:    1
Summary:    The Python package installer. 
License:    MIT
Source0:    pip-%{version}.tar.gz
Prefix:     /usr

%description
The Python package installer.

%prep
%setup -n pip-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%files
/usr/bin/pip
/usr/bin/pip3
/usr/bin/pip3.11
/usr/lib64/python3.11/site-packages/pip-23.2.1-py3.11.egg-info/
/usr/lib64/python3.11/site-packages/pip/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 23.2.1
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.0.0
- Initial rpm package
