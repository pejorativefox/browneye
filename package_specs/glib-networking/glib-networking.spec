Name:       glib-networking
Version:    2.56.1
Release:    1
Summary:    Network related gio modules for GLib. 
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

BuildRequires: gsettings-desktop-schemas
BuildRequires: gnutls

%description
Network related gio modules for GLib. 

%prep
%setup

%build
mkdir build
pushd build
meson --prefix=/usr            \
      -Dlibproxy_support=false \
      -Dca_certificates_path=/etc/ssl/ca-bundle.crt ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/share/locale/*
/usr/lib/gio/modules/libgiognomeproxy.so
/usr/lib/gio/modules/libgiognutls.so

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.56.1
- Initial RPM

