Name:       python2-pycurl
Version:    7.43.0.2
Release:    1
Summary:    urlgrabber is a pure python package that drastically simplifies the fetching of files. 
License:    LGPL
Source0:    pycurl-%{version}.tar.gz
Prefix:     /usr

%description
urlgrabber is a pure python package that drastically simplifies the fetching of files. 

%prep
%setup -n pycurl-%{version}

%build

%install
rm -rf %{buildroot}
python2 setup.py install --with-openssl --root %{buildroot}

%files
/usr/lib/python2.7/site-packages/curl/__init__.py
/usr/lib/python2.7/site-packages/curl/__init__.pyc
/usr/lib/python2.7/site-packages/pycurl-7.43.0.2-py2.7.egg-info
/usr/lib/python2.7/site-packages/pycurl.so
/usr/share/doc/pycurl/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.0.0
- Initial rpm package
