Name:       python-pycairo
Version:    1.24.0
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
python3 setup.py install --root %{buildroot}

%files
/usr/include/pycairo/py3cairo.h
/usr/lib64/pkgconfig/py3cairo.pc
/usr/lib64/python3.11/site-packages/cairo/__init__.py
/usr/lib64/python3.11/site-packages/cairo/__init__.pyi
/usr/lib64/python3.11/site-packages/cairo/__pycache__/__init__.cpython-311.pyc
/usr/lib64/python3.11/site-packages/cairo/_cairo.cpython-311-x86_64-linux-gnu.so
/usr/lib64/python3.11/site-packages/cairo/include/py3cairo.h
/usr/lib64/python3.11/site-packages/cairo/py.typed
/usr/lib64/python3.11/site-packages/pycairo-1.24.0-py3.11.egg-info/PKG-INFO
/usr/lib64/python3.11/site-packages/pycairo-1.24.0-py3.11.egg-info/SOURCES.txt
/usr/lib64/python3.11/site-packages/pycairo-1.24.0-py3.11.egg-info/dependency_links.txt
/usr/lib64/python3.11/site-packages/pycairo-1.24.0-py3.11.egg-info/top_level.txt

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.18.2-1
- Version bump

* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 1.24.0-1
- Initial rpm package
