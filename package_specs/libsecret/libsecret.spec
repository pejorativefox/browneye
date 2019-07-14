Name:       libsecret
Version:    0.18.8
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
%configure --disable-static --disable-manpages --enable-gtk-doc-html
%make_build

%install    
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -vf %{buildroot}%{_infodir}/dir

%files
/usr/bin/secret-tool
/usr/include/libsecret-1/libsecret/secret-attributes.h
/usr/include/libsecret-1/libsecret/secret-collection.h
/usr/include/libsecret-1/libsecret/secret-enum-types.h
/usr/include/libsecret-1/libsecret/secret-item.h
/usr/include/libsecret-1/libsecret/secret-password.h
/usr/include/libsecret-1/libsecret/secret-paths.h
/usr/include/libsecret-1/libsecret/secret-prompt.h
/usr/include/libsecret-1/libsecret/secret-schema.h
/usr/include/libsecret-1/libsecret/secret-schemas.h
/usr/include/libsecret-1/libsecret/secret-service.h
/usr/include/libsecret-1/libsecret/secret-types.h
/usr/include/libsecret-1/libsecret/secret-value.h
/usr/include/libsecret-1/libsecret/secret.h
/usr/lib64/girepository-1.0/Secret-1.typelib
/usr/lib64/libsecret-1.la
/usr/lib64/libsecret-1.so
/usr/lib64/libsecret-1.so.0
/usr/lib64/libsecret-1.so.0.0.0
/usr/lib64/pkgconfig/libsecret-1.pc
/usr/lib64/pkgconfig/libsecret-unstable.pc
/usr/share/gir-1.0/Secret-1.gir
/usr/share/gtk-doc/html/libsecret-1/SecretCollection.html
/usr/share/gtk-doc/html/libsecret-1/SecretItem.html
/usr/share/gtk-doc/html/libsecret-1/SecretPrompt.html
/usr/share/gtk-doc/html/libsecret-1/SecretService.html
/usr/share/gtk-doc/html/libsecret-1/SecretValue.html
/usr/share/gtk-doc/html/libsecret-1/annotation-glossary.html
/usr/share/gtk-doc/html/libsecret-1/c-examples.html
/usr/share/gtk-doc/html/libsecret-1/c-lookup-example.html
/usr/share/gtk-doc/html/libsecret-1/c-remove-example.html
/usr/share/gtk-doc/html/libsecret-1/c-store-example.html
/usr/share/gtk-doc/html/libsecret-1/complete.html
/usr/share/gtk-doc/html/libsecret-1/examples.html
/usr/share/gtk-doc/html/libsecret-1/home.png
/usr/share/gtk-doc/html/libsecret-1/index.html
/usr/share/gtk-doc/html/libsecret-1/js-examples.html
/usr/share/gtk-doc/html/libsecret-1/js-lookup-example.html
/usr/share/gtk-doc/html/libsecret-1/js-remove-example.html
/usr/share/gtk-doc/html/libsecret-1/js-store-example.html
/usr/share/gtk-doc/html/libsecret-1/left-insensitive.png
/usr/share/gtk-doc/html/libsecret-1/left.png
/usr/share/gtk-doc/html/libsecret-1/libsecret-1.devhelp2
/usr/share/gtk-doc/html/libsecret-1/libsecret-DBus-Path-Related-Functions.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-Password-storage.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-Secret-Attributes.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-SecretError.html
/usr/share/gtk-doc/html/libsecret-1/libsecret-SecretSchema.html
/usr/share/gtk-doc/html/libsecret-1/migrating-api.html
/usr/share/gtk-doc/html/libsecret-1/migrating-introduction.html
/usr/share/gtk-doc/html/libsecret-1/migrating-items.html
/usr/share/gtk-doc/html/libsecret-1/migrating-keyrings.html
/usr/share/gtk-doc/html/libsecret-1/migrating-locking.html
/usr/share/gtk-doc/html/libsecret-1/migrating-memory.html
/usr/share/gtk-doc/html/libsecret-1/migrating-misc.html
/usr/share/gtk-doc/html/libsecret-1/migrating-removing.html
/usr/share/gtk-doc/html/libsecret-1/migrating-schemas.html
/usr/share/gtk-doc/html/libsecret-1/migrating-searching.html
/usr/share/gtk-doc/html/libsecret-1/migrating-storing.html
/usr/share/gtk-doc/html/libsecret-1/migrating.html
/usr/share/gtk-doc/html/libsecret-1/py-examples.html
/usr/share/gtk-doc/html/libsecret-1/py-lookup-example.html
/usr/share/gtk-doc/html/libsecret-1/py-remove-example.html
/usr/share/gtk-doc/html/libsecret-1/py-store-example.html
/usr/share/gtk-doc/html/libsecret-1/right-insensitive.png
/usr/share/gtk-doc/html/libsecret-1/right.png
/usr/share/gtk-doc/html/libsecret-1/simple.html
/usr/share/gtk-doc/html/libsecret-1/style.css
/usr/share/gtk-doc/html/libsecret-1/up-insensitive.png
/usr/share/gtk-doc/html/libsecret-1/up.png
/usr/share/gtk-doc/html/libsecret-1/using-c.html
/usr/share/gtk-doc/html/libsecret-1/using-js.html
/usr/share/gtk-doc/html/libsecret-1/using-python.html
/usr/share/gtk-doc/html/libsecret-1/using-vala.html
/usr/share/gtk-doc/html/libsecret-1/using.html
/usr/share/gtk-doc/html/libsecret-1/vala-examples.html
/usr/share/gtk-doc/html/libsecret-1/vala-lookup-example.html
/usr/share/gtk-doc/html/libsecret-1/vala-remove-example.html
/usr/share/gtk-doc/html/libsecret-1/vala-store-example.html
/usr/share/locale/an/LC_MESSAGES/libsecret.mo
/usr/share/locale/ar/LC_MESSAGES/libsecret.mo
/usr/share/locale/as/LC_MESSAGES/libsecret.mo
/usr/share/locale/be/LC_MESSAGES/libsecret.mo
/usr/share/locale/bg/LC_MESSAGES/libsecret.mo
/usr/share/locale/bs/LC_MESSAGES/libsecret.mo
/usr/share/locale/ca/LC_MESSAGES/libsecret.mo
/usr/share/locale/ca@valencia/LC_MESSAGES/libsecret.mo
/usr/share/locale/cs/LC_MESSAGES/libsecret.mo
/usr/share/locale/da/LC_MESSAGES/libsecret.mo
/usr/share/locale/de/LC_MESSAGES/libsecret.mo
/usr/share/locale/el/LC_MESSAGES/libsecret.mo
/usr/share/locale/en_GB/LC_MESSAGES/libsecret.mo
/usr/share/locale/eo/LC_MESSAGES/libsecret.mo
/usr/share/locale/es/LC_MESSAGES/libsecret.mo
/usr/share/locale/eu/LC_MESSAGES/libsecret.mo
/usr/share/locale/fa/LC_MESSAGES/libsecret.mo
/usr/share/locale/fr/LC_MESSAGES/libsecret.mo
/usr/share/locale/fur/LC_MESSAGES/libsecret.mo
/usr/share/locale/gl/LC_MESSAGES/libsecret.mo
/usr/share/locale/he/LC_MESSAGES/libsecret.mo
/usr/share/locale/hr/LC_MESSAGES/libsecret.mo
/usr/share/locale/hu/LC_MESSAGES/libsecret.mo
/usr/share/locale/id/LC_MESSAGES/libsecret.mo
/usr/share/locale/it/LC_MESSAGES/libsecret.mo
/usr/share/locale/ja/LC_MESSAGES/libsecret.mo
/usr/share/locale/kk/LC_MESSAGES/libsecret.mo
/usr/share/locale/ko/LC_MESSAGES/libsecret.mo
/usr/share/locale/lt/LC_MESSAGES/libsecret.mo
/usr/share/locale/lv/LC_MESSAGES/libsecret.mo
/usr/share/locale/ml/LC_MESSAGES/libsecret.mo
/usr/share/locale/nb/LC_MESSAGES/libsecret.mo
/usr/share/locale/ne/LC_MESSAGES/libsecret.mo
/usr/share/locale/nl/LC_MESSAGES/libsecret.mo
/usr/share/locale/oc/LC_MESSAGES/libsecret.mo
/usr/share/locale/pa/LC_MESSAGES/libsecret.mo
/usr/share/locale/pl/LC_MESSAGES/libsecret.mo
/usr/share/locale/pt/LC_MESSAGES/libsecret.mo
/usr/share/locale/pt_BR/LC_MESSAGES/libsecret.mo
/usr/share/locale/ro/LC_MESSAGES/libsecret.mo
/usr/share/locale/ru/LC_MESSAGES/libsecret.mo
/usr/share/locale/sk/LC_MESSAGES/libsecret.mo
/usr/share/locale/sl/LC_MESSAGES/libsecret.mo
/usr/share/locale/sr/LC_MESSAGES/libsecret.mo
/usr/share/locale/sr@latin/LC_MESSAGES/libsecret.mo
/usr/share/locale/sv/LC_MESSAGES/libsecret.mo
/usr/share/locale/tg/LC_MESSAGES/libsecret.mo
/usr/share/locale/tr/LC_MESSAGES/libsecret.mo
/usr/share/locale/uk/LC_MESSAGES/libsecret.mo
/usr/share/locale/zh_CN/LC_MESSAGES/libsecret.mo
/usr/share/locale/zh_HK/LC_MESSAGES/libsecret.mo
/usr/share/locale/zh_TW/LC_MESSAGES/libsecret.mo

%changelog
# let's skip this for now

