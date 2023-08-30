Name:       xfce4-appfinder
Version:    4.19.0
Release:    1
Summary:    An application finder for Xfce
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
An application finder for Xfce

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
/usr/share/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.19.0
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.0
- Initial RPM

