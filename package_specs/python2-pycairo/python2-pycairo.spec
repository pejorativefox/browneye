Name:       python2-pycairo
Version:    1.18.2
Release:    1
Summary:    Python cairo bindings.
License:    LGPL
Source0:    pycairo-%{version}.tar.gz
Prefix:     /usr

%description
Python cairo bindings.

%prep
%setup -n pycairo-%{version}

%build

%install
rm -rf %{buildroot}
python2 setup.py install --root %{buildroot}

%files
/usr/include/pycairo/pycairo.h
/usr/lib/pkgconfig/pycairo.pc
/usr/lib/python2.7/site-packages/

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 42.0.2
- Initial rpm package
