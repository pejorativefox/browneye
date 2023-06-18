Name:       python3-sphinx
Version:    2.2.2
Release:    1
Summary:    Sphinx documentation builder
License:    MIT
Source0:    sphinx-%{version}.tar.gz
Prefix:     /usr

Requires: python3-alabaster, python3-babel, python3-certifi, python3-chardet
Requires: python3-dateutil, python3-docutils, python3-idna, python3-imagesize
Requires: python3-jinja, python3-markupsafe, python3-pygments, python3-pytz
Requires: python3-requests, python3-snowballstemmer, python3-urllib3

Requires: python3-sphinxcontrib-applehelp, python3-sphinxcontrib-devhelp, python3-sphinxcontrib-htmlhelp, python3-sphinxcontrib-jsmath, python3-sphinxcontrib-qthelp, python3-sphinxcontrib-serializinghtml

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
/usr/lib/python3.7/site-packages/*

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 2.2.2
- Initial rpm package
