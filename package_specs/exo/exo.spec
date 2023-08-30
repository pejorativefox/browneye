Name:       exo
Version:    4.18.0
Release:    1
Summary:    Application library for Xfce
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Application library for Xfce

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
/usr/include/
/usr/lib64/
/usr/share/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.18.0
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.12.8
- Initial RPM

