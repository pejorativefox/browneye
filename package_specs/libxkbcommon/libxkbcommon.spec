Name:       libxkbcommon
Version:    1.5.0
Release:    1
Summary:    library for handling of keyboard descriptions
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
library for handling of keyboard descriptions

%prep
%setup -q

%build
mkdir build &&
cd    build &&

meson setup ..            \
      --prefix=/usr       \
      --buildtype=release \
      -Denable-wayland=false \
      -Denable-docs=false 
ninja



%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/xkbcli
/usr/include/xkbcommon/xkbregistry.h
/usr/include/xkbcommon/xkbcommon-compat.h
/usr/include/xkbcommon/xkbcommon-compose.h
/usr/include/xkbcommon/xkbcommon-keysyms.h
/usr/include/xkbcommon/xkbcommon-names.h
/usr/include/xkbcommon/xkbcommon-x11.h
/usr/include/xkbcommon/xkbcommon.h
/usr/lib64/libxkbcommon-x11.so
/usr/lib64/libxkbcommon-x11.so.0
/usr/lib64/libxkbcommon-x11.so.0.0.0
/usr/lib64/libxkbcommon.so
/usr/lib64/libxkbcommon.so.0
/usr/lib64/libxkbcommon.so.0.0.0
/usr/lib64/pkgconfig/xkbcommon-x11.pc
/usr/lib64/pkgconfig/xkbcommon.pc
/usr/lib64/libxkbregistry.so
/usr/lib64/libxkbregistry.so.0
/usr/lib64/libxkbregistry.so.0.0.0
/usr/lib64/pkgconfig/xkbregistry.pc
/usr/libexec/xkbcommon/xkbcli-compile-keymap
/usr/libexec/xkbcommon/xkbcli-how-to-type
/usr/libexec/xkbcommon/xkbcli-interactive-evdev
/usr/libexec/xkbcommon/xkbcli-interactive-x11
/usr/libexec/xkbcommon/xkbcli-list
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.5.0-1
- Version bump

