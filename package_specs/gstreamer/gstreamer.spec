Name:       gstreamer
Version:    1.16.2
Release:    1
Summary:    Streaming multimedia framework
License:    Various
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Streaming multimedia framework

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/gst-inspect-1.0
/usr/bin/gst-launch-1.0
/usr/bin/gst-stats-1.0
/usr/bin/gst-typefind-1.0
/usr/include/gstreamer-1.0/
/usr/lib64/girepository-1.0/
/usr/lib64/gstreamer-1.0/
/usr/lib64/libgstbase-1.0.la
/usr/lib64/libgstbase-1.0.so
/usr/lib64/libgstbase-1.0.so.0
/usr/lib64/libgstbase-1.0.so.0.1602.0
/usr/lib64/libgstcheck-1.0.la
/usr/lib64/libgstcheck-1.0.so
/usr/lib64/libgstcheck-1.0.so.0
/usr/lib64/libgstcheck-1.0.so.0.1602.0
/usr/lib64/libgstcontroller-1.0.la
/usr/lib64/libgstcontroller-1.0.so
/usr/lib64/libgstcontroller-1.0.so.0
/usr/lib64/libgstcontroller-1.0.so.0.1602.0
/usr/lib64/libgstnet-1.0.la
/usr/lib64/libgstnet-1.0.so
/usr/lib64/libgstnet-1.0.so.0
/usr/lib64/libgstnet-1.0.so.0.1602.0
/usr/lib64/libgstreamer-1.0.la
/usr/lib64/libgstreamer-1.0.so
/usr/lib64/libgstreamer-1.0.so.0
/usr/lib64/libgstreamer-1.0.so.0.1602.0
/usr/lib64/pkgconfig/gstreamer-1.0.pc
/usr/lib64/pkgconfig/gstreamer-base-1.0.pc
/usr/lib64/pkgconfig/gstreamer-check-1.0.pc
/usr/lib64/pkgconfig/gstreamer-controller-1.0.pc
/usr/lib64/pkgconfig/gstreamer-net-1.0.pc
/usr/libexec/gstreamer-1.0/gst-completion-helper
/usr/libexec/gstreamer-1.0/gst-plugin-scanner
/usr/libexec/gstreamer-1.0/gst-ptp-helper
/usr/share/aclocal/gst-element-check-1.0.m4
/usr/share/bash-completion/completions/gst-inspect-1.0
/usr/share/bash-completion/completions/gst-launch-1.0
/usr/share/bash-completion/helpers/gst
/usr/share/gdb/auto-load/usr/lib64/libgstreamer-1.0.so.0.1602.0-gdb.py
/usr/share/gir-1.0/Gst-1.0.gir
/usr/share/gir-1.0/GstBase-1.0.gir
/usr/share/gir-1.0/GstCheck-1.0.gir
/usr/share/gir-1.0/GstController-1.0.gir
/usr/share/gir-1.0/GstNet-1.0.gir
/usr/share/gstreamer-1.0/gdb/glib_gobject_helper.py
/usr/share/gstreamer-1.0/gdb/gst_gdb.py
/usr/share/gtk-doc/html/gstreamer-1.0/
/usr/share/gtk-doc/html/gstreamer-libs-1.0/
/usr/share/gtk-doc/html/gstreamer-plugins-1.0/
/usr/share/locale/
/usr/share/man/man1/gst-inspect-1.0.1.gz
/usr/share/man/man1/gst-launch-1.0.1.gz
/usr/share/man/man1/gst-stats-1.0.1.gz
/usr/share/man/man1/gst-typefind-1.0.1.gz

%changelog
* Thu Sep 10 2020 Chris Statzer <chris.statzer@qq.com> 1.16.2
- Initial RPM

