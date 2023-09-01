Name:       libcanberra
Version:    0.30
Release:    1
Summary:    libcanberra is an implementation of the XDG Sound Theme and Name Specifications
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
libcanberra is an implementation of the XDG Sound Theme and Name Specifications

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/canberra-boot
/usr/bin/canberra-gtk-play
/usr/include/canberra-gtk.h
/usr/include/canberra.h
/usr/lib64/
/usr/share/doc/libcanberra/README
/usr/share/gdm/autostart/LoginWindow/libcanberra-ready-sound.desktop
/usr/share/gnome/autostart/libcanberra-login-sound.desktop
/usr/share/gnome/shutdown/libcanberra-logout-sound.sh
/usr/share/gtk-doc/
/usr/share/vala/vapi/
/usr/lib64/libcanberra-0.30/libcanberra-gstreamer.so

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 0.30
- Initial RPM

