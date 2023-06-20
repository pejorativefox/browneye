Name:       python3-zipp
Version:    3.15.0
Release:    1
Summary:    A pathlib-compatible Zipfile object wrapper.
License:    MIT
Source0:    zipp-%{version}.tar.gz
Prefix:     /usr

%description
A pathlib-compatible Zipfile object wrapper.

%prep
%setup -n zipp-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/lib/python3.7/site-packages/
cp -rv zipp zipp.egg-info %{buildroot}/lib/python3.7/site-packages/

%files
/lib/python3.7/site-packages/zipp.egg-info/PKG-INFO
/lib/python3.7/site-packages/zipp.egg-info/SOURCES.txt
/lib/python3.7/site-packages/zipp.egg-info/dependency_links.txt
/lib/python3.7/site-packages/zipp.egg-info/requires.txt
/lib/python3.7/site-packages/zipp.egg-info/top_level.txt
/lib/python3.7/site-packages/zipp/__init__.py
/lib/python3.7/site-packages/zipp/py310compat.py

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.15.0
- Initial RPM

