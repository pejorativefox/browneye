Name:       python2-urlgrabber
Version:    4.0.0
Release:    1
Summary:    urlgrabber is a pure python package that drastically simplifies the fetching of files. 
License:    LGPL
Source0:    urlgrabber-%{version}.tar.gz
Prefix:     /usr

%description
urlgrabber is a pure python package that drastically simplifies the fetching of files. 

%prep
%setup -n urlgrabber-%{version}

%build

%install
rm -rf %{buildroot}
python2 setup.py install --root %{buildroot}

%files
/usr/bin/urlgrabber
/usr/lib/python2.7/site-packages/urlgrabber-4.0.0-py2.7.egg-info/PKG-INFO
/usr/lib/python2.7/site-packages/urlgrabber-4.0.0-py2.7.egg-info/SOURCES.txt
/usr/lib/python2.7/site-packages/urlgrabber-4.0.0-py2.7.egg-info/dependency_links.txt
/usr/lib/python2.7/site-packages/urlgrabber-4.0.0-py2.7.egg-info/requires.txt
/usr/lib/python2.7/site-packages/urlgrabber-4.0.0-py2.7.egg-info/top_level.txt
/usr/lib/python2.7/site-packages/urlgrabber/__init__.py
/usr/lib/python2.7/site-packages/urlgrabber/__init__.pyc
/usr/lib/python2.7/site-packages/urlgrabber/byterange.py
/usr/lib/python2.7/site-packages/urlgrabber/byterange.pyc
/usr/lib/python2.7/site-packages/urlgrabber/grabber.py
/usr/lib/python2.7/site-packages/urlgrabber/grabber.pyc
/usr/lib/python2.7/site-packages/urlgrabber/mirror.py
/usr/lib/python2.7/site-packages/urlgrabber/mirror.pyc
/usr/lib/python2.7/site-packages/urlgrabber/progress.py
/usr/lib/python2.7/site-packages/urlgrabber/progress.pyc
/usr/libexec/urlgrabber-ext-down
/usr/share/doc/urlgrabber-4.0.0/ChangeLog
/usr/share/doc/urlgrabber-4.0.0/LICENSE
/usr/share/doc/urlgrabber-4.0.0/README
/usr/share/doc/urlgrabber-4.0.0/TODO

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.0.0
- Initial rpm package
