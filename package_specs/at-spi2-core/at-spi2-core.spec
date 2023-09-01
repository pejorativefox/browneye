Name:       at-spi2-core
Version:    2.49.90
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(atspi-2)

%description
TODO

%prep
%setup

%build
mkdir build-atk
pushd build-atk

meson --prefix=/usr ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-atk
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/xdg/autostart/at-spi-dbus-bus.desktop
/etc/xdg/Xwayland-session.d/00-at-spi
/usr/include/
/usr/lib/
/usr/libexec/
/usr/share/

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM


