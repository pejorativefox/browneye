Name:       python3-snowballstemmer
Version:    1.9.0
Release:    1
Summary:    Snowball compiler and stemming algorithms
License:    Custom
Source0:    snowballstemmer-%{version}.tar.gz
Prefix:     /usr

%description
Snowball is a small string processing language designed for creating stemming algorithms for use in Information Retrieval. 

%prep
%setup -n snowballstemmer-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/snowballstemmer-1.9.0-py3.7.egg-info
/usr/lib/python3.7/site-packages/snowballstemmer/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.9.0-1
- Initial rpm package
