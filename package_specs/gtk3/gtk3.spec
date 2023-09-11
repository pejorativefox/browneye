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
%setup -q

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

%files -f ../../SOURCES/gtk3.filelist

%changelog
# let's skip this for now

