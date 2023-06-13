Name:       xdg-desktop-portal
Version:    1.8.0
Release:    1
Summary:    Desktop integration portal 
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Desktop integration portal 

%prep
%setup

%build
%configure --disable-geoclue --disable-pipewire
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/lib/systemd/user/xdg-*
/usr/share/pkgconfig/xdg-desktop-portal.pc
/usr/libexec/xdg-desktop-portal
/usr/libexec/xdg-document-portal
/usr/libexec/xdg-permission-store
/usr/share/dbus-1/
/usr/share/locale/

%changelog
* Wed Jan 13 2021 Chris Statzer <chris.statzer@qq.com> 1.8.0
- Initial RPM

