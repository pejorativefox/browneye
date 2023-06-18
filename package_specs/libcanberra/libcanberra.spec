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
/usr/lib64/gnome-settings-daemon-3.0/gtk-modules/canberra-gtk-module.desktop
/usr/lib64/gtk-2.0/modules/libcanberra-gtk-module.la
/usr/lib64/gtk-2.0/modules/libcanberra-gtk-module.so
/usr/lib64/gtk-3.0/modules/libcanberra-gtk-module.so
/usr/lib64/gtk-3.0/modules/libcanberra-gtk3-module.la
/usr/lib64/gtk-3.0/modules/libcanberra-gtk3-module.so
/usr/lib64/libcanberra-0.30/libcanberra-alsa.la
/usr/lib64/libcanberra-0.30/libcanberra-alsa.so
/usr/lib64/libcanberra-0.30/libcanberra-multi.la
/usr/lib64/libcanberra-0.30/libcanberra-multi.so
/usr/lib64/libcanberra-0.30/libcanberra-null.la
/usr/lib64/libcanberra-0.30/libcanberra-null.so
/usr/lib64/libcanberra-0.30/libcanberra-oss.la
/usr/lib64/libcanberra-0.30/libcanberra-oss.so
/usr/lib64/libcanberra-0.30/libcanberra-pulse.la
/usr/lib64/libcanberra-0.30/libcanberra-pulse.so
/usr/lib64/libcanberra-gtk.la
/usr/lib64/libcanberra-gtk.so
/usr/lib64/libcanberra-gtk.so.0
/usr/lib64/libcanberra-gtk.so.0.1.9
/usr/lib64/libcanberra-gtk3.la
/usr/lib64/libcanberra-gtk3.so
/usr/lib64/libcanberra-gtk3.so.0
/usr/lib64/libcanberra-gtk3.so.0.1.9
/usr/lib64/libcanberra.la
/usr/lib64/libcanberra.so
/usr/lib64/libcanberra.so.0
/usr/lib64/libcanberra.so.0.2.5
/usr/lib64/pkgconfig/libcanberra-gtk.pc
/usr/lib64/pkgconfig/libcanberra-gtk3.pc
/usr/lib64/pkgconfig/libcanberra.pc
/usr/share/doc/libcanberra/README
/usr/share/gdm/autostart/LoginWindow/libcanberra-ready-sound.desktop
/usr/share/gnome/autostart/libcanberra-login-sound.desktop
/usr/share/gnome/shutdown/libcanberra-logout-sound.sh
/usr/share/gtk-doc/
/usr/share/vala/vapi/
/usr/lib64/libcanberra-0.30/libcanberra-gstreamer.la
/usr/lib64/libcanberra-0.30/libcanberra-gstreamer.so

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 0.30
- Initial RPM

