
# Libsolv
puts its cmake module in wrong path
ln -s /share/cmake/Modules/FindLibSolv.cmake /share/cmake-3.13/Modules/

# permissions

# mpv
https://pi3d.github.io/html/FAQ.html#glx-dri2-not-supported-or-failed-to-authenticate

# Kernel
WARNING: iwlwifi is useless without IWLDVM or IWLMVM
linux-firmware

# makeca
post install script
rename conf.dist

#missing packages
manpages

# missing env
SHELL

# missing paths
/opt/rust/bin
/sbin
/var/lib/dbus

#docs

# missing links
/bin/cc

# python
pyc files in packages
install of 2.x clobbes /usr/bin/python
pygobject is needed for network manager build

# gtk pixbuf
gdk-pixbuf-query-loaders --update-cache
gdk-pixbuf post install command: gdk-pixbuf-query-loaders > /usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders.cache
maybe the same

#gtk+ 2
 If you installed the package on to your system using a “DESTDIR” method, an important file was not installed and must be copied and/or generated. Generate it using the following command as the root user:
gtk-query-immodules-2.0 --update-cache

# gtk+ 3
this is missing in post install for gtk+
gtk-query-immodules-3.0 --update-cache

#kernel modules install
/bin/depmod -> /sbin/depmod

# fstab
/dev/<root_dev>	/            ext      noatime             0     0
proc           	/proc        proc     nosuid,noexec,nodev 0     0
sysfs          	/sys         sysfs    nosuid,noexec,nodev 0     0
devpts         	/dev/pts     devpts   gid=5,mode=620      0     0
tmpfs          	/run         tmpfs    defaults            0     0
devtmpfs       	/dev         devtmpfs mode=0755,nosuid    0     0


# fonts
install -v -d -m755 /usr/share/fonts                               &&
ln -svfn /usr/share/fonts/X11/OTF /usr/share/fonts/X11-OTF &&
ln -svfn /usr/share/fonts/X11/TTF /usr/share/fonts/X11-TTF



# dbus
bootscripts install needed
useradd -c "D-Bus Message Daemon User" -d /var/run/dbus \
        -u 18 -g messagebus -s /bin/false messagebus


chown -v root:messagebus /usr/libexec/dbus-daemon-launch-helper &&
chmod -v      4750       /usr/libexec/dbus-daemon-launch-helper

/run/dbus missing


# qemu shit
qemu-img create -f <fmt> <image filename> <size of disk>

qemu-nbd -c /dev/nbd0 /tmp/LFS.img

dd if=/dev/zero of=browneye.rimg count=10240000 bs=1024

mount -o rw,loop,offset=1048576 browneye.rimg /home/daspork/browneye/root/mnt/loop

losetup --offset 1048576 /dev/loop2 browneye.rimg

mount /dev/loop2 /home/daspork/browneye/root/mnt/loop


qemu -hda plug_SD-karte.img -m 256


qemu-system-x86_64 -kernel /home/daspork/browneye/root/kernel\
  -append "root=/dev/sda1" -initrd /boot/initramfs-linux.img \
  -m 2048 --enable-kvm -cpu host -drive format=raw,file=browneye.rimg

qemu-system-x86_64 -m 2048 --enable-kvm -cpu host -drive format=raw,file=browneye.rimg

