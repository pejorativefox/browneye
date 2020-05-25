Name:       python3-
Version:    
Release:    1
Summary:    
License:    
Source0:    -%{version}.tar.gz
Prefix:     /usr

%description


%prep
%setup -n -%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 42.0.2
- Initial rpm package
