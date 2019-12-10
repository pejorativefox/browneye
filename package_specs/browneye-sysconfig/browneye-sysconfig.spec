Name:       browneye-sysconfig
Version:    0.01
Release:    1
Summary:    Initial configuration for Browneye Linux.
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Package of configuration files for Browneye Linux.

%prep
%setup

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/etc
cp -r etc/* %{buildroot}/etc/

%files
/etc/finit.conf
/etc/fstab
/etc/hosts
/etc/start.d/README
/etc/sysconfig/README

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.01
- Initial package.
