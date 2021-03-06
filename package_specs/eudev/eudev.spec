Name:       eudev
Version:    3.2.7
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
%configure  --prefix=/usr           \
            --bindir=/sbin          \
            --sbindir=/sbin         \
            --libdir=/usr/lib       \
            --sysconfdir=/etc       \
            --libexecdir=/lib       \
            --with-rootprefix=      \
            --with-rootlibdir=/lib  \
            --enable-manpages       \
            --disable-static        \
            --config-cache
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/lib64/udev/rules.d
mkdir -pv %{buildroot}/etc/udev/rules.d


%files
/etc/udev/rules.d/
/lib64/udev/rules.d/
/etc/udev/hwdb.d/20-OUI.hwdb
/etc/udev/hwdb.d/20-acpi-vendor.hwdb
/etc/udev/hwdb.d/20-bluetooth-vendor-product.hwdb
/etc/udev/hwdb.d/20-net-ifname.hwdb
/etc/udev/hwdb.d/20-pci-classes.hwdb
/etc/udev/hwdb.d/20-pci-vendor-model.hwdb
/etc/udev/hwdb.d/20-sdio-classes.hwdb
/etc/udev/hwdb.d/20-sdio-vendor-model.hwdb
/etc/udev/hwdb.d/20-usb-classes.hwdb
/etc/udev/hwdb.d/20-usb-vendor-model.hwdb
/etc/udev/hwdb.d/20-vmbus-class.hwdb
/etc/udev/hwdb.d/60-evdev.hwdb
/etc/udev/hwdb.d/60-keyboard.hwdb
/etc/udev/hwdb.d/60-sensor.hwdb
/etc/udev/hwdb.d/70-mouse.hwdb
/etc/udev/hwdb.d/70-pointingstick.hwdb
/etc/udev/hwdb.d/70-touchpad.hwdb
/etc/udev/udev.conf
/lib/libudev.so.1
/lib/libudev.so.1.6.3
/lib/udev/ata_id
/lib/udev/cdrom_id
/lib/udev/collect
/lib/udev/mtd_probe
/lib/udev/rules.d/50-udev-default.rules
/lib/udev/rules.d/60-block.rules
/lib/udev/rules.d/60-cdrom_id.rules
/lib/udev/rules.d/60-drm.rules
/lib/udev/rules.d/60-evdev.rules
/lib/udev/rules.d/60-input-id.rules
/lib/udev/rules.d/60-persistent-alsa.rules
/lib/udev/rules.d/60-persistent-input.rules
/lib/udev/rules.d/60-persistent-storage-tape.rules
/lib/udev/rules.d/60-persistent-storage.rules
/lib/udev/rules.d/60-persistent-v4l.rules
/lib/udev/rules.d/60-sensor.rules
/lib/udev/rules.d/60-serial.rules
/lib/udev/rules.d/64-btrfs.rules
/lib/udev/rules.d/70-joystick.rules
/lib/udev/rules.d/70-mouse.rules
/lib/udev/rules.d/70-touchpad.rules
/lib/udev/rules.d/75-net-description.rules
/lib/udev/rules.d/75-probe_mtd.rules
/lib/udev/rules.d/78-sound-card.rules
/lib/udev/rules.d/80-drivers.rules
/lib/udev/rules.d/80-net-name-slot.rules
/lib/udev/scsi_id
/lib/udev/v4l_id
/sbin/udevadm
/sbin/udevd
/usr/include/libudev.h
/usr/include/udev.h
/usr/lib/libudev.la
/usr/lib/libudev.so
/usr/lib/pkgconfig/libudev.pc
/usr/share/man/man5/udev.conf.5.gz
/usr/share/man/man7/udev.7.gz
/usr/share/man/man8/udevadm.8.gz
/usr/share/man/man8/udevd.8.gz
/usr/share/pkgconfig/udev.pc


%changelog
# let's skip this for now
