Name:       python-setuptools
Version:    68.1.2
Release:    1
Summary:    Python setuptools build system.
License:    LGPL
Source0:    setuptools-%{version}.tar.gz
Prefix:     /usr

%description
Python setuptools build system. 

%prep
%setup -n setuptools-%{version}

%build

%install
rm -rf %{buildroot}
#python3 bootstrap.py
python3 setup.py install --root %{buildroot}
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%files
/usr/lib64/python3.11/site-packages/setuptools/
/usr/lib64/python3.11/site-packages/pkg_resources/
/usr/lib64/python3.11/site-packages/_distutils_hack/
/usr/lib64/python3.11/site-packages/setuptools-68.1.2-py3.11.egg-info/
/usr/lib64/python3.11/site-packages/distutils-precedence.pth

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 42.0.2
- Initial rpm package
