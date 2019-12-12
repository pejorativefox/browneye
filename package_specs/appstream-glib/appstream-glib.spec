Name:       appstream-glib
Version:    0.7.16
Release:    1
Summary:    Glib AppStream metadata support.
License:    GPL
Source0:    appstream-glib-appstream_glib_0_7_16.tar.gz
Prefix:     /usr

%description
Glib AppStream metadata support.


%prep
%setup -n appstream-glib-appstream_glib_0_7_16

%build
mkdir build
pushd build
meson --prefix=/usr -Dgtk_doc=false -Dman=false ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/share/locale/*
/usr/include/libappstream-glib/*
/usr/lib64/asb-plugins-5/*
/usr/bin/appstream-builder
/usr/bin/appstream-compose
/usr/bin/appstream-util
/usr/lib64/girepository-1.0/AppStreamGlib-1.0.typelib
/usr/lib64/libappstream-glib.so
/usr/lib64/libappstream-glib.so.8
/usr/lib64/libappstream-glib.so.8.0.10
/usr/lib64/pkgconfig/appstream-glib.pc
/usr/share/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.7.16
- Initial RPM

