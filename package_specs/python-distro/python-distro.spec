Name:       python-distro
Version:    1.8.0
Release:    1
Summary:    An OS platform information API
License:    Apache
Source0:    distro-%{version}.tar.gz
Prefix:     /usr

%description
distro provides information about the OS distribution it runs on, such as a reliable machine-readable ID, or version information.

%prep
%setup -n distro-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/lib64/python3.11/site-packages/distro
cp src/distro/* %{buildroot}/usr/lib64/python3.11/site-packages/distro

%files
/usr/lib64/python3.11/site-packages/distro/

%changelog
* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 1.8.0
- Initial rpm package
