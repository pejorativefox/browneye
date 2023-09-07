Name:       python-pyparsing
Version:    2.4.5
Release:    1
Summary:    A Python Parsing Module
License:    GPL
Source0:    pyparsing-%{version}.tar.gz
Prefix:     /usr

%description
A Python Parsing Module

%prep
%setup -n pyparsing-pyparsing_%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%files
/usr/lib64/python3.11/site-packages/

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 2.4.5
- Initial rpm package
