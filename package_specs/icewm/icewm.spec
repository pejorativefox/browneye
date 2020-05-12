Name:       icewm
Version:    1.6.5
Release:    1
Summary:    A small win9x like window manager
License:    GPL2
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
A small win9x like window manager

%prep
%setup

%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd 

%files
/usr/bin/icehelp
/usr/bin/icesh
/usr/bin/icesound
/usr/bin/icewm
/usr/bin/icewm-menu-fdo
/usr/bin/icewm-menu-xrandr
/usr/bin/icewm-session
/usr/bin/icewm-set-gnomewm
/usr/bin/icewmbg
/usr/bin/icewmhint
/usr/share/man/*
/usr/share/icewm/*
/usr/share/locale/*
/usr/share/xsessions/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM

