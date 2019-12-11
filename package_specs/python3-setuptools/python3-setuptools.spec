Name:       python3-setuptools
Version:    42.0.2
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
python3 bootstrap.py
python3 setup.py install --root %{buildroot}

%files
/usr/bin/easy_install
/usr/bin/easy_install-3.7
/usr/lib/python3.7/site-packages/*

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 42.0.2
- Initial rpm package
