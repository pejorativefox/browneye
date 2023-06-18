Name:       tumbler
Version:    0.2.7
Release:    1
Summary:    D-Bus service for applications to request thumbnails
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
D-Bus service for applications to request thumbnails

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/etc/xdg/tumbler/tumbler.rc
/usr/include/tumbler-1/tumbler/*
/usr/lib64/libtumbler-1.la
/usr/lib64/libtumbler-1.so
/usr/lib64/libtumbler-1.so.0
/usr/lib64/libtumbler-1.so.0.0.0
/usr/lib64/pkgconfig/tumbler-1.pc
/usr/lib64/tumbler-1/plugins/cache/tumbler-cache-plugin.so
/usr/lib64/tumbler-1/plugins/cache/tumbler-xdg-cache.la
/usr/lib64/tumbler-1/plugins/cache/tumbler-xdg-cache.so
/usr/lib64/tumbler-1/plugins/tumbler-cover-thumbnailer.la
/usr/lib64/tumbler-1/plugins/tumbler-cover-thumbnailer.so
/usr/lib64/tumbler-1/plugins/tumbler-desktop-thumbnailer.la
/usr/lib64/tumbler-1/plugins/tumbler-desktop-thumbnailer.so
/usr/lib64/tumbler-1/plugins/tumbler-font-thumbnailer.la
/usr/lib64/tumbler-1/plugins/tumbler-font-thumbnailer.so
/usr/lib64/tumbler-1/plugins/tumbler-jpeg-thumbnailer.la
/usr/lib64/tumbler-1/plugins/tumbler-jpeg-thumbnailer.so
/usr/lib64/tumbler-1/plugins/tumbler-pixbuf-thumbnailer.la
/usr/lib64/tumbler-1/plugins/tumbler-pixbuf-thumbnailer.so
/usr/lib64/tumbler-1/plugins/tumbler-gst-thumbnailer.la
/usr/lib64/tumbler-1/plugins/tumbler-gst-thumbnailer.so
/usr/lib64/tumbler-1/tumblerd
/usr/share/dbus-1/services/org.xfce.Tumbler.Cache1.service
/usr/share/dbus-1/services/org.xfce.Tumbler.Manager1.service
/usr/share/dbus-1/services/org.xfce.Tumbler.Thumbnailer1.service
/usr/share/gtk-doc/html/tumbler/*
/usr/share/locale/*
/usr/lib64/tumbler-1/plugins/tumbler-poppler-thumbnailer.la
/usr/lib64/tumbler-1/plugins/tumbler-poppler-thumbnailer.so

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.2.7
- Initial RPM

