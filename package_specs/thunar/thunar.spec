Name:       thunar
Version:    4.18.6
Release:    1
Summary:    Modern file manager for Xfce
License:    GPL2
Source0:   %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Modern file manager for Xfce

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
/usr/etc/xdg/Thunar/
/usr/include/
/usr/lib/systemd/user/thunar.service
/usr/lib64/
/usr/share/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.18.6
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.8.9
- Initial RPM

