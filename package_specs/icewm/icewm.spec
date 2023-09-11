Name:       icewm
Version:    3.4.1
Release:    1
Summary:    A small win9x like window manager
License:    GPL2
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

BuildRequires: imlib2
BuildRequires: pulseaudio

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
/usr/share/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 3.4.1
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.6.5
- Initial RPM

