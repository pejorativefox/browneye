Name:       python-markupsafe
Version:    2.1.3
Release:    1
Summary:    Safely add untrusted strings to HTML/XML markup.
License:    BSD
Source0:    MarkupSafe-%{version}.tar.gz
Prefix:     /usr

%description
Safely add untrusted strings to HTML/XML markup.

%prep
%setup -n MarkupSafe-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.11/site-packages/MarkupSafe-2.1.3-py3.11.egg-info/PKG-INFO
/usr/lib/python3.11/site-packages/MarkupSafe-2.1.3-py3.11.egg-info/SOURCES.txt
/usr/lib/python3.11/site-packages/MarkupSafe-2.1.3-py3.11.egg-info/dependency_links.txt
/usr/lib/python3.11/site-packages/MarkupSafe-2.1.3-py3.11.egg-info/top_level.txt
/usr/lib/python3.11/site-packages/markupsafe/__init__.py
/usr/lib/python3.11/site-packages/markupsafe/__pycache__/__init__.cpython-311.pyc
/usr/lib/python3.11/site-packages/markupsafe/__pycache__/_native.cpython-311.pyc
/usr/lib/python3.11/site-packages/markupsafe/_native.py
/usr/lib/python3.11/site-packages/markupsafe/_speedups.c
/usr/lib/python3.11/site-packages/markupsafe/_speedups.cpython-311-x86_64-linux-gnu.so
/usr/lib/python3.11/site-packages/markupsafe/_speedups.pyi
/usr/lib/python3.11/site-packages/markupsafe/py.typed

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump

* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.1.1-1
- Initial rpm package
