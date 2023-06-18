Name:       webkitgtk
Version:    2.29.91
Release:    1
Summary:    WebKit is a cross-platform web browser engine.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
WebKit is a cross-platform web browser engine.

%prep
%setup

%build
mkdir build
pushd build
cmake .. -DPORT=GTK -DUSE_LIBHYPHEN=0 -DUSE_SYSTEMD=0 
make -j2
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/local/bin/WebKitWebDriver
/usr/local/include/webkitgtk-4.0/
/usr/local/lib64/girepository-1.0/JavaScriptCore-4.0.typelib
/usr/local/lib64/girepository-1.0/WebKit2-4.0.typelib
/usr/local/lib64/girepository-1.0/WebKit2WebExtension-4.0.typelib
/usr/local/lib64/libjavascriptcoregtk-4.0.so
/usr/local/lib64/libjavascriptcoregtk-4.0.so.18
/usr/local/lib64/libjavascriptcoregtk-4.0.so.18.17.6
/usr/local/lib64/libwebkit2gtk-4.0.so
/usr/local/lib64/libwebkit2gtk-4.0.so.37
/usr/local/lib64/libwebkit2gtk-4.0.so.37.49.2
/usr/local/lib64/pkgconfig/javascriptcoregtk-4.0.pc
/usr/local/lib64/pkgconfig/webkit2gtk-4.0.pc
/usr/local/lib64/pkgconfig/webkit2gtk-web-extension-4.0.pc
/usr/local/lib64/webkit2gtk-4.0/injected-bundle/libwebkit2gtkinjectedbundle.so
/usr/local/libexec/webkit2gtk-4.0/WebKitNetworkProcess
/usr/local/libexec/webkit2gtk-4.0/WebKitWebProcess
/usr/local/libexec/webkit2gtk-4.0/jsc
/usr/local/share/gir-1.0/
/usr/local/share/locale/

%changelog
* Thu Sep 10 2020 Chris Statzer <chris.statzer@qq.com> 2.29.91
- Initial RPM

