Name:       glib
Version:    2.66.0
Release:    2
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides:   pkgconfig(glib-2.0)
Provides:   pkgconfig(gobject-2.0)
Provides:   pkgconfig(gmodule-2.0)
Provides:   pkgconfig(gmodule-no-export-2.0)
Provides:   pkgconfig(gio-unix-2.0)
Provides:   pkgconfig(gio-2.0)
Provides:   pkgconfig(gthread-2.0)

%description
TODO

%prep
%setup -a 0

%build
mkdir build-glib
pushd build-glib

meson --prefix=/usr   \
      -Dman=false      \
      -Dselinux=disabled \
      ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-glib
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/gapplication
/usr/bin/gdbus
/usr/bin/gdbus-codegen
/usr/bin/gio
/usr/bin/gio-querymodules
/usr/bin/glib-compile-resources
/usr/bin/glib-compile-schemas
/usr/bin/glib-genmarshal
/usr/bin/glib-gettextize
/usr/bin/glib-mkenums
/usr/bin/gobject-query
/usr/bin/gresource
/usr/bin/gsettings
/usr/bin/gtester
/usr/bin/gtester-report
/usr/include/gio-unix-2.0/gio/gdesktopappinfo.h
/usr/include/gio-unix-2.0/gio/gfiledescriptorbased.h
/usr/include/gio-unix-2.0/gio/gunixconnection.h
/usr/include/gio-unix-2.0/gio/gunixcredentialsmessage.h
/usr/include/gio-unix-2.0/gio/gunixfdlist.h
/usr/include/gio-unix-2.0/gio/gunixfdmessage.h
/usr/include/gio-unix-2.0/gio/gunixinputstream.h
/usr/include/gio-unix-2.0/gio/gunixmounts.h
/usr/include/gio-unix-2.0/gio/gunixoutputstream.h
/usr/include/gio-unix-2.0/gio/gunixsocketaddress.h
/usr/include/glib-2.0/
/usr/lib/glib-2.0/include/glibconfig.h
/usr/lib/libgio-2.0.so
/usr/lib/libgio-2.0.so.0
/usr/lib/libgio-2.0.so.0.6600.0
/usr/lib/libglib-2.0.so
/usr/lib/libglib-2.0.so.0
/usr/lib/libglib-2.0.so.0.6600.0
/usr/lib/libgmodule-2.0.so
/usr/lib/libgmodule-2.0.so.0
/usr/lib/libgmodule-2.0.so.0.6600.0
/usr/lib/libgobject-2.0.so
/usr/lib/libgobject-2.0.so.0
/usr/lib/libgobject-2.0.so.0.6600.0
/usr/lib/libgthread-2.0.so
/usr/lib/libgthread-2.0.so.0
/usr/lib/libgthread-2.0.so.0.6600.0
/usr/lib/pkgconfig/gio-2.0.pc
/usr/lib/pkgconfig/gio-unix-2.0.pc
/usr/lib/pkgconfig/glib-2.0.pc
/usr/lib/pkgconfig/gmodule-2.0.pc
/usr/lib/pkgconfig/gmodule-export-2.0.pc
/usr/lib/pkgconfig/gmodule-no-export-2.0.pc
/usr/lib/pkgconfig/gobject-2.0.pc
/usr/lib/pkgconfig/gthread-2.0.pc
/usr/share/aclocal/glib-2.0.m4
/usr/share/aclocal/glib-gettext.m4
/usr/share/aclocal/gsettings.m4
/usr/share/bash-completion/completions/
/usr/share/gdb/auto-load/usr/lib/libglib-2.0.so.0.6600.0-gdb.py
/usr/share/gdb/auto-load/usr/lib/libgobject-2.0.so.0.6600.0-gdb.py
/usr/share/gettext/its/gschema.its
/usr/share/gettext/its/gschema.loc
/usr/share/glib-2.0/
/usr/share/locale/

%changelog
* Fri Sep 11 2020 Chris Statzer <chris.statzer@qq.com> 2.66.0
- Update to newest glib

