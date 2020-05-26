Name:       python3-markupsafe
Version:    1.1.1
Release:    1
Summary:    Safely add untrusted strings to HTML/XML markup.
License:    BSD
Source0:    MarkupSafe-%{version}.tar.gz
Prefix:     /usr

%description
Safely add untrusted strings to HTML/XML markup.

%prep
%setup -n MarkupSafe-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/MarkupSafe-1.1.1-py3.7.egg-info/
/usr/lib/python3.7/site-packages/markupsafe/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 1.1.1-1
- Initial rpm package
