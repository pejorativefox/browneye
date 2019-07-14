Name:       lgi
Version:    0.9.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz

%description
TODO

%prep
%setup -a 0

%build
sed -i 's/LUA_VERSION=5.1/LUA_VERSION=5.3/g' lgi/Makefile
%make_build

%install    
rm -rf %{buildroot}
make install PREFIX=/usr DESTDIR=%{buildroot}
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/lib/lua/5.3/lgi/corelgilua51.so
/usr/share/lua/5.3/lgi.lua
/usr/share/lua/5.3/lgi/class.lua
/usr/share/lua/5.3/lgi/component.lua
/usr/share/lua/5.3/lgi/core.lua
/usr/share/lua/5.3/lgi/enum.lua
/usr/share/lua/5.3/lgi/ffi.lua
/usr/share/lua/5.3/lgi/init.lua
/usr/share/lua/5.3/lgi/log.lua
/usr/share/lua/5.3/lgi/namespace.lua
/usr/share/lua/5.3/lgi/override/Clutter.lua
/usr/share/lua/5.3/lgi/override/GLib-Bytes.lua
/usr/share/lua/5.3/lgi/override/GLib-Error.lua
/usr/share/lua/5.3/lgi/override/GLib-Markup.lua
/usr/share/lua/5.3/lgi/override/GLib-Source.lua
/usr/share/lua/5.3/lgi/override/GLib-Timer.lua
/usr/share/lua/5.3/lgi/override/GLib-Variant.lua
/usr/share/lua/5.3/lgi/override/GLib.lua
/usr/share/lua/5.3/lgi/override/GObject-Closure.lua
/usr/share/lua/5.3/lgi/override/GObject-Object.lua
/usr/share/lua/5.3/lgi/override/GObject-Type.lua
/usr/share/lua/5.3/lgi/override/GObject-Value.lua
/usr/share/lua/5.3/lgi/override/Gdk.lua
/usr/share/lua/5.3/lgi/override/Gio-DBus.lua
/usr/share/lua/5.3/lgi/override/Gio.lua
/usr/share/lua/5.3/lgi/override/GooCanvas.lua
/usr/share/lua/5.3/lgi/override/Gst.lua
/usr/share/lua/5.3/lgi/override/Gtk.lua
/usr/share/lua/5.3/lgi/override/Pango.lua
/usr/share/lua/5.3/lgi/override/PangoCairo.lua
/usr/share/lua/5.3/lgi/override/cairo.lua
/usr/share/lua/5.3/lgi/package.lua
/usr/share/lua/5.3/lgi/record.lua
/usr/share/lua/5.3/lgi/version.lua


%changelog
# let's skip this for now

