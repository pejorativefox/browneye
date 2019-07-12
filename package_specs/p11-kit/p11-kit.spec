Name:       p11-kit
Version:    0.23.15
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
sed '20,$ d' -i trust/trust-extract-compat.in &&
cat >> trust/trust-extract-compat.in << "EOF"
# Copy existing anchor modifications to /etc/ssl/local
/usr/libexec/make-ca/copy-trust-modifications

# Generate a new trust store
/usr/sbin/make-ca -f -g
EOF

%configure --sysconfdir=/etc \
           --with-trust-paths=/etc/pki/anchors
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
ln -s /usr/libexec/p11-kit/trust-extract-compat \
      %{buildroot}/usr/bin/update-ca-certificates
      
%files
/etc/pkcs11/pkcs11.conf.example
/usr/bin/p11-kit
/usr/bin/trust
/usr/bin/update-ca-certificates
/usr/include/p11-kit-1/p11-kit/deprecated.h
/usr/include/p11-kit-1/p11-kit/iter.h
/usr/include/p11-kit-1/p11-kit/p11-kit.h
/usr/include/p11-kit-1/p11-kit/pin.h
/usr/include/p11-kit-1/p11-kit/pkcs11.h
/usr/include/p11-kit-1/p11-kit/pkcs11x.h
/usr/include/p11-kit-1/p11-kit/remote.h
/usr/include/p11-kit-1/p11-kit/uri.h
/usr/lib64/libp11-kit.la
/usr/lib64/libp11-kit.so
/usr/lib64/libp11-kit.so.0
/usr/lib64/libp11-kit.so.0.3.0
/usr/lib64/p11-kit-proxy.so
/usr/lib64/pkcs11/p11-kit-client.la
/usr/lib64/pkcs11/p11-kit-client.so
/usr/lib64/pkcs11/p11-kit-trust.la
/usr/lib64/pkcs11/p11-kit-trust.so
/usr/lib64/pkgconfig/p11-kit-1.pc
/usr/libexec/p11-kit/p11-kit-remote
/usr/libexec/p11-kit/p11-kit-server
/usr/libexec/p11-kit/trust-extract-compat
/usr/share/gtk-doc/html/p11-kit/config-example.html
/usr/share/gtk-doc/html/p11-kit/config-files.html
/usr/share/gtk-doc/html/p11-kit/config.html
/usr/share/gtk-doc/html/p11-kit/devel-building-style.html
/usr/share/gtk-doc/html/p11-kit/devel-building.html
/usr/share/gtk-doc/html/p11-kit/devel-commands.html
/usr/share/gtk-doc/html/p11-kit/devel-debugging.html
/usr/share/gtk-doc/html/p11-kit/devel-paths.html
/usr/share/gtk-doc/html/p11-kit/devel-testing.html
/usr/share/gtk-doc/html/p11-kit/devel.html
/usr/share/gtk-doc/html/p11-kit/gtk-doc.css
/usr/share/gtk-doc/html/p11-kit/home.png
/usr/share/gtk-doc/html/p11-kit/index.html
/usr/share/gtk-doc/html/p11-kit/left-insensitive.png
/usr/share/gtk-doc/html/p11-kit/left.png
/usr/share/gtk-doc/html/p11-kit/p11-kit-Deprecated.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-Future.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-Modules.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-PIN-Callbacks.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-URIs.html
/usr/share/gtk-doc/html/p11-kit/p11-kit-Utilities.html
/usr/share/gtk-doc/html/p11-kit/p11-kit.devhelp2
/usr/share/gtk-doc/html/p11-kit/p11-kit.html
/usr/share/gtk-doc/html/p11-kit/pkcs11-conf.html
/usr/share/gtk-doc/html/p11-kit/reference.html
/usr/share/gtk-doc/html/p11-kit/remoting.html
/usr/share/gtk-doc/html/p11-kit/right-insensitive.png
/usr/share/gtk-doc/html/p11-kit/right.png
/usr/share/gtk-doc/html/p11-kit/sharing-managed.html
/usr/share/gtk-doc/html/p11-kit/sharing.html
/usr/share/gtk-doc/html/p11-kit/style.css
/usr/share/gtk-doc/html/p11-kit/tools.html
/usr/share/gtk-doc/html/p11-kit/trust-disable.html
/usr/share/gtk-doc/html/p11-kit/trust-glib-networking.html
/usr/share/gtk-doc/html/p11-kit/trust-module.html
/usr/share/gtk-doc/html/p11-kit/trust-nss.html
/usr/share/gtk-doc/html/p11-kit/trust.html
/usr/share/gtk-doc/html/p11-kit/up-insensitive.png
/usr/share/gtk-doc/html/p11-kit/up.png
/usr/share/p11-kit/modules/p11-kit-trust.module

%changelog
# let's skip this for now
