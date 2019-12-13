Name:       python3-wheel
Version:    0.33.6
Release:    1
Summary:    The official binary distribution format for Python 
License:    GPL
Source0:    wheel-%{version}.tar.gz
Prefix:     /usr

%description
The official binary distribution format for Python 

%prep
%setup -n wheel-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/bin/wheel
/usr/lib/python3.7/site-packages/*

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 0.33.6
- Initial rpm package
