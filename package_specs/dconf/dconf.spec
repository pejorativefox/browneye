Name:       dconf
Version:    0.28.0
Release:    1
Summary:    Dconf backend for gsettings.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Dconf backend for gsettings.

%prep
%setup

%build
mkdir build
pushd build
meson --prefix=/usr --sysconfdir=/etc ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/dconf
/usr/include/dconf/client/dconf-client.h
/usr/include/dconf/common/dconf-changeset.h
/usr/include/dconf/common/dconf-enums.h
/usr/include/dconf/common/dconf-paths.h
/usr/include/dconf/dconf.h
/usr/lib64/gio/modules/libdconfsettings.so
/usr/lib64/libdconf.so
/usr/lib64/libdconf.so.1
/usr/lib64/libdconf.so.1.0.0
/usr/lib64/pkgconfig/dconf.pc
/usr/libexec/dconf-service
/usr/share/bash-completion/completions/dconf
/usr/share/dbus-1/services/ca.desrt.dconf.service
/usr/share/vala/vapi/dconf.deps
/usr/share/vala/vapi/dconf.vapi

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.28.0
- Initial RPM

