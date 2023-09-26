Name:       gcr
Version:    3.28.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
TODO

%prep
%setup -a 0

%build
sed -i -r 's:"(/desktop):"/org/gnome\1:' schema/*.xml &&
%configure --enable-vala=no
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir

%files
/usr/bin/gcr-viewer
/usr/include/gck-1/
/usr/include/gcr-3/
/usr/lib64/girepository-1.0/Gck-1.typelib
/usr/lib64/girepository-1.0/Gcr-3.typelib
/usr/lib64/girepository-1.0/GcrUi-3.typelib
/usr/lib64/libgck-1.so
/usr/lib64/libgck-1.so.0
/usr/lib64/libgck-1.so.0.0.0
/usr/lib64/libgcr-3.so
/usr/lib64/libgcr-3.so.1
/usr/lib64/libgcr-3.so.1.0.0
/usr/lib64/libgcr-base-3.so
/usr/lib64/libgcr-base-3.so.1
/usr/lib64/libgcr-base-3.so.1.0.0
/usr/lib64/libgcr-ui-3.so
/usr/lib64/libgcr-ui-3.so.1
/usr/lib64/libgcr-ui-3.so.1.0.0
/usr/lib64/pkgconfig/gck-1.pc
/usr/lib64/pkgconfig/gcr-3.pc
/usr/lib64/pkgconfig/gcr-base-3.pc
/usr/lib64/pkgconfig/gcr-ui-3.pc
/usr/libexec/gcr-prompter
/usr/libexec/gcr-ssh-askpass
/usr/share/GConf/gsettings/org.gnome.crypto.pgp.convert
/usr/share/GConf/gsettings/org.gnome.crypto.pgp_keyservers.convert
/usr/share/applications/gcr-prompter.desktop
/usr/share/applications/gcr-viewer.desktop
/usr/share/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
/usr/share/dbus-1/services/org.gnome.keyring.SystemPrompter.service
/usr/share/gir-1.0/Gck-1.gir
/usr/share/gir-1.0/Gcr-3.gir
/usr/share/gir-1.0/GcrUi-3.gir
/usr/share/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml
/usr/share/gtk-doc/html/gck/
/usr/share/gtk-doc/html/gcr-3/
/usr/share/icons/hicolor/
/usr/share/locale/
/usr/share/mime/packages/gcr-crypto-types.xml

%changelog
# let's skip this for now

