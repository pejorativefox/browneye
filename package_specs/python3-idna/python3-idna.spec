Name:       python3-idna
Version:    2.9
Release:    1
Summary:    Internationalized Domain Names in Applications (IDNA)
License:    BSD
Source0:    idna-%{version}.tar.gz
Prefix:     /usr

%description
python module for Internationalized Domain Names in Applications (IDNA)

%prep
%setup -n idna-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/idna-2.9-py3.7.egg-info/
/usr/lib/python3.7/site-packages/idna/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 2.9-1
- Initial rpm package
