Name:       python2-pip
Version:    19.3.1
Release:    1
Summary:    The Python package installer. 
License:    MIT
Source0:    pip-%{version}.tar.gz
Prefix:     /usr

%description
The Python package installer.

%prep
%setup -n pip-%{version}

%build

%install
rm -rf %{buildroot}
python2 setup.py install --root %{buildroot}

%files
/usr/bin/pip
/usr/bin/pip2
/usr/bin/pip2.7
/usr/lib/python2.7/site-packages/

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.0.0
- Initial rpm package
