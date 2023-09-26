Name:       libnotify
Version:    0.7.8
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
TODO

%prep
%setup -a 0

%build
mkdir -pv build
pushd build
meson --prefix=/usr -Dgtk_doc=false .. &&
ninja
popd

%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/notify-send
/usr/include/libnotify/notification.h
/usr/include/libnotify/notify-enum-types.h
/usr/include/libnotify/notify-features.h
/usr/include/libnotify/notify.h
/usr/lib64/girepository-1.0/Notify-0.7.typelib
/usr/lib64/libnotify.so
/usr/lib64/libnotify.so.4
/usr/lib64/libnotify.so.4.0.0
/usr/lib64/pkgconfig/libnotify.pc
/usr/share/gir-1.0/Notify-0.7.gir

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.7.8-1
- Version bump

