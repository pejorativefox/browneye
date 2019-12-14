Name:       thunar-volman
Version:    0.9.5
Release:    1
Summary:    Automatic management of removeable devices in Thunar
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Automatic management of removeable devices in Thunar

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/thunar-volman
/usr/bin/thunar-volman-settings
/usr/share/applications/thunar-volman-settings.desktop
/usr/share/icons/hicolor/48x48/apps/tvm-burn-cd.png
/usr/share/icons/hicolor/48x48/apps/tvm-dev-pocketpc.png
/usr/share/icons/hicolor/scalable/apps/tvm-burn-cd.svg
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.9.5
- Initial RPM

