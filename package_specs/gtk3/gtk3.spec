Name:       gtk+
Version:    3.24.38
Release:    2
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(gdk-3.0), pkgconfig(gtk+-3.0)

%description
TODO

%prep
%setup

%build
mkdir build &&
cd    build &&
meson setup --prefix=/usr           \
            --buildtype=release     \
             -Dman=false             \
             -Dbroadway_backend=true \
             -Dwayland_backend=false \
             -Dgtk_doc=false         \
             ..                      
ninja

%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

glib-compile-schemas %{buildroot}/usr/share/glib-2.0/schemas
rm -vf %{buildroot}%{_infodir}/dir*

%post
gtk-query-immodules-3.0 --update-cache

%files
/etc/gtk-3.0/im-multipress.conf
/usr/bin/broadwayd
/usr/bin/gtk-builder-tool
/usr/bin/gtk-encode-symbolic-svg
/usr/bin/gtk-launch
/usr/bin/gtk-query-immodules-3.0
/usr/bin/gtk-query-settings
/usr/bin/gtk-update-icon-cache
/usr/bin/gtk3-demo
/usr/bin/gtk3-demo-application
/usr/bin/gtk3-icon-browser
/usr/bin/gtk3-widget-factory
/usr/include/
/usr/lib/
/usr/share/

%changelog
# let's skip this for now

