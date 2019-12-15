Name:       vte
Version:    0.58.3
Release:    1
Summary:    Virtual Terminal Emulator library.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Virtual Terminal Emulator library.

%prep
%setup

%build
mkdir build
pushd build
meson   --prefix=/usr     \
	--sysconfdir=/etc \
        -Dfribidi=false   \
        -Dvapi=false
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/etc/profile.d/vte.sh
/usr/bin/vte-2.91
/usr/include/vte-2.91/vte/*
/usr/lib/girepository-1.0/Vte-2.91.typelib
/usr/lib/libvte-2.91.so
/usr/lib/libvte-2.91.so.0
/usr/lib/libvte-2.91.so.0.5800.3
/usr/lib/pkgconfig/vte-2.91.pc
/usr/share/gir-1.0/Vte-2.91.gir
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.59.0
- Added this sample to help with adding new packages.

