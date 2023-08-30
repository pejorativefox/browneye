Name:       xfce4-power-manager
Version:    4.19.1
Release:    1
Summary:    Power manager for Xfce desktop
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Power manager for Xfce desktop

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/
/usr/etc/
/usr/lib64/
/usr/sbin/
/usr/share/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.19.1
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.6.5
- Initial RPM

