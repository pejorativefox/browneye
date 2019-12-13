Name:       python3-six
Version:    1.13.0
Release:    1
Summary:    Python 2 and 3 compatibility library
License:    GPL
Source0:    six-%{version}.tar.gz
Prefix:     /usr

%description
Python 2 and 3 compatibility library

%prep
%setup -n six-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/*

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 1.13.0
- Initial rpm package
