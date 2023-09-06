Name:       python-wheel
Version:    0.41.1
Release:    1
Summary:    The official binary distribution format for Python 
License:    GPL
Source0:    wheel-%{version}.tar.gz
Prefix:     /usr

%description
The official binary distribution format for Python 

%prep
%setup -n wheel-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%files
/usr/bin/wheel
/usr/lib64/python3.11/site-packages/wheel/
/usr/lib64/python3.11/site-packages/wheel-0.41.1-py3.11.egg-info

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 0.41.1
- Version bump

* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 0.33.6
- Initial rpm package
