Name:       xfce4-appfinder
Version:    4.14.0
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
/usr/bin/xfce4-appfinder
/usr/bin/xfrun4
/usr/share/applications/xfce4-appfinder.desktop
/usr/share/applications/xfce4-run.desktop
/usr/share/locale/*
/usr/share/metainfo/org.xfce.xfce4-appfinder.appdata.xml

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.0
- Initial RPM

