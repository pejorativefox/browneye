Name:       meson
Version:    0.52.1
Release:    1
Summary:    Meson build system
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Meson build system

%prep
%setup

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --root=dest
mkdir -pv %{buildroot}/usr
cp -rv dest/* %{buildroot}


%files
/usr/bin/meson
/usr/lib/python3.7/site-packages/meson-0.52.1-py3.7.egg-info/PKG-INFO
/usr/lib/python3.7/site-packages/meson-0.52.1-py3.7.egg-info/SOURCES.txt
/usr/lib/python3.7/site-packages/meson-0.52.1-py3.7.egg-info/dependency_links.txt
/usr/lib/python3.7/site-packages/meson-0.52.1-py3.7.egg-info/entry_points.txt
/usr/lib/python3.7/site-packages/meson-0.52.1-py3.7.egg-info/requires.txt
/usr/lib/python3.7/site-packages/meson-0.52.1-py3.7.egg-info/top_level.txt
/usr/lib/python3.7/site-packages/mesonbuild/*
/usr/share/man/man1/meson.1.gz
/usr/share/polkit-1/actions/com.mesonbuild.install.policy

%changelog
# let's skip this for now
