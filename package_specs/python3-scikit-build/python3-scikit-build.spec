Name:       python3-scikit-build
Version:    0.10.0
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

%files
/usr/lib/python3.7/site-packages/*

%changelog
* Tue Dec 11 2019 Chris Statzer <chris.statzer@qq.com> 0.10.0
- Initial rpm package
