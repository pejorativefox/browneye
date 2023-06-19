Name:       python3-importlib_metadata
Version:    6.7.0
Release:    1
Summary:    Library to access the metadata for a Python package.
License:    apache
Source0:    importlib_metadata-%{version}.tar.gz
Prefix:     /usr

%description
Library to access the metadata for a Python package.

%prep
%setup -n importlib_metadata-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/lib/python3.7/site-packages/
cp -rv importlib_metadata importlib_metadata.egg-info %{buildroot}/lib/python3.7/site-packages/

%files
/lib/python3.7/site-packages/importlib_metadata.egg-info/
/lib/python3.7/site-packages/importlib_metadata/

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 6.7.0
- Initial RPM

