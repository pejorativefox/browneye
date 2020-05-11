
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

# python
pyc files in packages
install of 2.x clobbes /usr/bin/python
pygobject is needed for network manager build

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

