Name:       libwnck
Version:    3.32.0
Release:    1
Summary:    Library to manage X windows and workspaces (via pagers, tasklists, etc.)
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Library to manage X windows and workspaces (via pagers, tasklists, etc.)

%prep
%setup

%build
mkdir build
pushd build
meson --prefix=/usr ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/wnck-urgency-monitor
/usr/bin/wnckprop
/usr/include/libwnck-3.0/libwnck/application.h
/usr/include/libwnck-3.0/libwnck/class-group.h
/usr/include/libwnck-3.0/libwnck/libwnck.h
/usr/include/libwnck-3.0/libwnck/pager.h
/usr/include/libwnck-3.0/libwnck/screen.h
/usr/include/libwnck-3.0/libwnck/selector.h
/usr/include/libwnck-3.0/libwnck/tasklist.h
/usr/include/libwnck-3.0/libwnck/util.h
/usr/include/libwnck-3.0/libwnck/version.h
/usr/include/libwnck-3.0/libwnck/window-action-menu.h
/usr/include/libwnck-3.0/libwnck/window.h
/usr/include/libwnck-3.0/libwnck/wnck-enum-types.h
/usr/include/libwnck-3.0/libwnck/workspace.h
/usr/lib/girepository-1.0/Wnck-3.0.typelib
/usr/lib/libwnck-3.so
/usr/lib/libwnck-3.so.0
/usr/lib/libwnck-3.so.0.3.0
/usr/lib/pkgconfig/libwnck-3.0.pc
/usr/share/gir-1.0/Wnck-3.0.gir
/usr/share/locale/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.32.0
- Initial RPM

