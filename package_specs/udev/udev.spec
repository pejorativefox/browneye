Name:       udev
Version:    254
Release:    1
Summary:    Systemd udev
License:    LGPL
Source0:    systemd-254.tar.gz
Prefix:     /usr

%description
The Udev package contains programs for dynamic creation of device nodes.

%prep
%setup -q -n systemd-254

%build
sed -i -e 's/GROUP="render"/GROUP="video"/' \
       -e 's/GROUP="sgx", //' rules.d/50-udev-default.rules.in
sed '/systemd-sysctl/s/^/#/' -i rules.d/99-systemd.rules.in

mkdir build
pushd build
meson setup \
      --prefix=/usr                 \
      --buildtype=release           \
      -Dmode=release                \
      -Ddev-kvm-mode=0660           \
      -Dlink-udev-shared=false      \
      ..

ninja udevadm systemd-hwdb \
      $(grep -o -E "^build (src/libudev|src/udev|rules.d|hwdb.d)[^:]*" \
        build.ninja | awk '{ print $2 }')                              \
      $(realpath libudev.so --relative-to .)

rm rules.d/90-vconsole.rules

popd

%install
pushd build
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/bin
mkdir -pv %{buildroot}/usr/sbin
mkdir -pv %{buildroot}/usr/include
install -vm755 -d {%{buildroot}/usr/lib64,%{buildroot}/etc}/udev/{hwdb,rules}.d
install -vm755 -d %{buildroot}/usr/{lib64,share}/pkgconfig
install -vm755 udevadm                     %{buildroot}/usr/bin/
install -vm755 systemd-hwdb                %{buildroot}/usr/bin/udev-hwdb
ln      -svfn  ../bin/udevadm              %{buildroot}/usr/sbin/udevd
cp      -av    libudev.so{,*[0-9]}         %{buildroot}/usr/lib64/
install -vm644 ../src/libudev/libudev.h    %{buildroot}/usr/include/
install -vm644 src/libudev/*.pc            %{buildroot}/usr/lib64/pkgconfig/
install -vm644 src/udev/*.pc               %{buildroot}/usr/share/pkgconfig/
install -vm644 ../src/udev/udev.conf       %{buildroot}/etc/udev/
install -vm644 rules.d/* ../rules.d/{*.rules,README} %{buildroot}/usr/lib64/udev/rules.d/
install -vm644 hwdb.d/*  ../hwdb.d/{*.hwdb,README}   %{buildroot}/usr/lib64/udev/hwdb.d/
install -vm755 $(find src/udev -type f | grep -F -v ".") %{buildroot}/usr/lib64/udev
popd

%files
/etc/udev/udev.conf
/usr/bin/udev-hwdb
/usr/bin/udevadm
/usr/include/libudev.h
/usr/lib64/libudev.so
/usr/lib64/libudev.so.1
/usr/lib64/libudev.so.1.7.7
/usr/lib64/pkgconfig/libudev.pc
/usr/lib64/udev/ata_id
/usr/lib64/udev/cdrom_id
/usr/lib64/udev/dmi_memory_id
/usr/lib64/udev/fido_id
/usr/lib64/udev/iocost
/usr/lib64/udev/mtd_probe
/usr/lib64/udev/scsi_id
/usr/lib64/udev/v4l_id
/usr/sbin/udevd
/usr/share/pkgconfig/udev.pc
/usr/lib64/udev/hwdb.d/
/usr/lib64/udev/rules.d/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 254
- Initial RPM

