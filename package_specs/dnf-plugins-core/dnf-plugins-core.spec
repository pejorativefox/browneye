Name:       dnf-plugins-core
Version:    4.4.2
Release:    1
Summary:    Core DNF Plugins 
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

BuildRequires: dnf, python-sphinx

%description
Core DNF pluigins providing additional dnf functionality.

%prep
%setup

%build
sed -i 's/sphinx-build-3/sphinx-build/g' doc/CMakeLists.txt
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr \
         -DPYTHON_DESIRED=3 \
         -DSPHINX_BUILD_NAME=sphinx-build
%make_build
make doc-man
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd
rm %{buildroot}/etc/dnf/plugins/local.conf

%files
/etc/dnf/plugins
/usr/lib/python3.7/site-packages/dnfpluginscore/__init__.py
/usr/lib/python3.7/site-packages/dnf-plugins/
/usr/libexec/dnf-utils-3
/usr/share/locale/
/usr/share/man/

%changelog
* Sun May 24 2020 Chris Statzer <chris.statzer@qq.com> 4.0.15-1
- Initial RPM

