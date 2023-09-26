Name:       libinput
Version:    1.12.6
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

BuildRequires: mtdev
Buildrequires: libevdev

%description
TODO

%prep
%setup -a 0

%build
mkdir build
pushd build
meson --prefix=/usr \
      -Dudev-dir=/lib64/udev  \
      -Ddebug-gui=false     \
      -Dtests=false         \
      -Ddocumentation=false \
      -Dlibwacom=false      \
      ..
ninja
popd


%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install 
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/lib64/udev/libinput-device-group
/lib64/udev/libinput-model-quirks
/lib64/udev/rules.d/80-libinput-device-groups.rules
/lib64/udev/rules.d/90-libinput-model-quirks.rules
/usr/bin/libinput
/usr/include/libinput.h
/usr/lib64/libinput.so
/usr/lib64/libinput.so.10
/usr/lib64/libinput.so.10.13.0
/usr/lib64/pkgconfig/libinput.pc
/usr/libexec/libinput/libinput-debug-events
/usr/libexec/libinput/libinput-list-devices
/usr/libexec/libinput/libinput-measure
/usr/libexec/libinput/libinput-measure-fuzz
/usr/libexec/libinput/libinput-measure-touch-size
/usr/libexec/libinput/libinput-measure-touchpad-pressure
/usr/libexec/libinput/libinput-measure-touchpad-tap
/usr/libexec/libinput/libinput-quirks
/usr/libexec/libinput/libinput-record
/usr/libexec/libinput/libinput-replay
/usr/share/libinput/10-generic-keyboard.quirks
/usr/share/libinput/10-generic-lid.quirks
/usr/share/libinput/10-generic-trackball.quirks
/usr/share/libinput/30-vendor-aiptek.quirks
/usr/share/libinput/30-vendor-alps.quirks
/usr/share/libinput/30-vendor-contour.quirks
/usr/share/libinput/30-vendor-cyapa.quirks
/usr/share/libinput/30-vendor-elantech.quirks
/usr/share/libinput/30-vendor-huion.quirks
/usr/share/libinput/30-vendor-ibm.quirks
/usr/share/libinput/30-vendor-kensington.quirks
/usr/share/libinput/30-vendor-logitech.quirks
/usr/share/libinput/30-vendor-microsoft.quirks
/usr/share/libinput/30-vendor-razer.quirks
/usr/share/libinput/30-vendor-synaptics.quirks
/usr/share/libinput/30-vendor-vmware.quirks
/usr/share/libinput/30-vendor-wacom.quirks
/usr/share/libinput/50-system-acer.quirks
/usr/share/libinput/50-system-apple.quirks
/usr/share/libinput/50-system-asus.quirks
/usr/share/libinput/50-system-chicony.quirks
/usr/share/libinput/50-system-cyborg.quirks
/usr/share/libinput/50-system-dell.quirks
/usr/share/libinput/50-system-google.quirks
/usr/share/libinput/50-system-hp.quirks
/usr/share/libinput/50-system-lenovo.quirks
/usr/share/libinput/50-system-system76.quirks
/usr/share/man/man1/libinput-debug-events.1.gz
/usr/share/man/man1/libinput-list-devices.1.gz
/usr/share/man/man1/libinput-measure-fuzz.1.gz
/usr/share/man/man1/libinput-measure-touch-size.1.gz
/usr/share/man/man1/libinput-measure-touchpad-pressure.1.gz
/usr/share/man/man1/libinput-measure-touchpad-tap.1.gz
/usr/share/man/man1/libinput-measure.1.gz
/usr/share/man/man1/libinput-quirks-list.1.gz
/usr/share/man/man1/libinput-quirks-validate.1.gz
/usr/share/man/man1/libinput-quirks.1.gz
/usr/share/man/man1/libinput-record.1.gz
/usr/share/man/man1/libinput-replay.1.gz
/usr/share/man/man1/libinput.1.gz

%changelog
# let's skip this for now

