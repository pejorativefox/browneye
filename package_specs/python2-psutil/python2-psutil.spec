Name:       python2-psutil
Version:    5.6.7
Release:    1
Summary:    Cross-platform lib for process and system monitoring in Python
License:    GPL
Source0:    psutil-release-%{version}.tar.gz
Prefix:     /usr

%description
Cross-platform lib for process and system monitoring in Python

%prep
%setup -n psutil-release-%{version}

%build

%install
rm -rf %{buildroot}
python2 setup.py install --root %{buildroot}

%files
/usr/lib/python2.7/site-packages/*

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 5.6.7
- Initial rpm package
