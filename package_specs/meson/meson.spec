Name:       meson
Version:    1.2.1
Release:    1
Summary:    Meson build system
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Meson build system

%prep
%setup -q

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --root=dest
mkdir -pv %{buildroot}/usr
cp -rv dest/* %{buildroot}
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%files
/usr/bin/meson
/usr/lib64/python3.11/site-packages/meson-1.2.1-py3.11.egg-info/
/usr/lib64/python3.11/site-packages/mesonbuild/
/usr/share/man/man1/meson.1.gz
/usr/share/polkit-1/actions/com.mesonbuild.install.policy

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.2.1
- Version bump
