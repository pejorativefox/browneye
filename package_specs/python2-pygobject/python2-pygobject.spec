Name:       python2-pygobject
Version:    3.34.0
Release:    1
Summary:    Python gobject bindings.
License:    LGPL
Source0:    pygobject-%{version}.tar.xz
Prefix:     /usr

%description
Python gobject bindings.

%prep
%setup -n pygobject-%{version}

%build

%install
rm -rf %{buildroot}
python2 setup.py install --root %{buildroot}

%files
/usr/include/pygobject-3.0/pygobject.h
/usr/lib/pkgconfig/pygobject-3.0.pc
/usr/lib/python2.7/site-packages/

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 42.0.2
- Initial rpm package
