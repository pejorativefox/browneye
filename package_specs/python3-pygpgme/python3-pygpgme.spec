Name:       python3-pygpgme
Version:    0.3.1
Release:    1
Summary:    A Python wrapper for the GPGME library.
License:    GPL
Source0:    pygpgme-%{version}.tar.gz
Prefix:     /usr

%description
A Python wrapper for the GPGME library.

%prep
%setup -n pygpgme-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/*

%changelog
* Fri May 22 2020 Chris Statzer <chris.statzer@qq.com> 0.3.1
- Small version upgrade, old package no longer available

* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 0.3
- Initial rpm package
