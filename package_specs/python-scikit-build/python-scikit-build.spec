Name:       python-scikit-build
Version:    0.13.0
Release:    1
Summary:    Improved build system generator for CPython C, C++, Cython and Fortran extensions 
License:    GPL
Source0:    scikit-build-%{version}.tar.gz
Prefix:     /usr

%description
Improved build system generator for CPython C, C++, Cython and Fortran extensions 

%prep
%setup -n scikit-build-%{version}

%build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%files
/usr/lib64/python3.11/site-packages/

%changelog
* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 0.13.0
- Version bump

* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 0.10.0
- Initial rpm package
