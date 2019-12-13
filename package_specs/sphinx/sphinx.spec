Name:       python3-sphinx
Version:    2.2.2
Release:    1
Summary:    Sphinx documentation builder
License:    MIT
Source0:    sphinx-%{version}.tar.gz
Prefix:     /usr

%description
Sphinx documentation builder

%prep
%setup -n sphinx-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/bin/sphinx-apidoc
/usr/bin/sphinx-autogen
/usr/bin/sphinx-build
/usr/bin/sphinx-quickstart
/usr/lib/python3.7/site-packages/Sphinx-2.2.2.dev20191213-py3.7.egg-info/PKG-INFO
/usr/lib/python3.7/site-packages/Sphinx-2.2.2.dev20191213-py3.7.egg-info/SOURCES.txt
/usr/lib/python3.7/site-packages/Sphinx-2.2.2.dev20191213-py3.7.egg-info/dependency_links.txt
/usr/lib/python3.7/site-packages/Sphinx-2.2.2.dev20191213-py3.7.egg-info/entry_points.txt
/usr/lib/python3.7/site-packages/Sphinx-2.2.2.dev20191213-py3.7.egg-info/not-zip-safe
/usr/lib/python3.7/site-packages/Sphinx-2.2.2.dev20191213-py3.7.egg-info/requires.txt
/usr/lib/python3.7/site-packages/Sphinx-2.2.2.dev20191213-py3.7.egg-info/top_level.txt
/usr/lib/python3.7/site-packages/sphinx/*

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 2.2.2
- Initial rpm package
