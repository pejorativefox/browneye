Name:       python-pygobject
Version:    3.44.1
Release:    1
Summary:    Python gobject bindings.
License:    LGPL
Source0:    PyGObject-%{version}.tar.gz
Prefix:     /usr

%description
Python gobject bindings.

%prep
%setup -n PyGObject-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/include/pygobject-3.0/pygobject.h
/usr/lib64/pkgconfig/pygobject-3.0.pc
/usr/lib64/python3.11/site-packages/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 3.44.1-1
- Version bump

* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 3.34.0-1
- Initial rpm package
