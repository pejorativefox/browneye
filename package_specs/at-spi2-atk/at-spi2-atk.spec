Name:       at-spi2-atk
Version:    2.30.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


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
/usr/include/at-spi2-atk/2.0/atk-bridge.h
/usr/lib/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
/usr/lib/gtk-2.0/modules/libatk-bridge.so
/usr/lib/libatk-bridge-2.0.so
/usr/lib/libatk-bridge-2.0.so.0
/usr/lib/libatk-bridge-2.0.so.0.0.0
/usr/lib/pkgconfig/atk-bridge-2.0.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.30.0
- Initial RPM

