Name:       python3-libcomps
Version:    0.1.15
Release:    1
Summary:    Libcomps is alternative for yum.comps library.
License:    GPL
Source0:    libcomps-%{version}.post1.tar.gz
Prefix:     /usr

%description
Libcomps is alternative for yum.comps library.

%prep
%setup -n libcomps-%{version}.post1

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
/usr/lib/python3.7/site-packages/*

%changelog
* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 0.1.15
- Version bump

* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 0.1.14
- Initial rpm package
