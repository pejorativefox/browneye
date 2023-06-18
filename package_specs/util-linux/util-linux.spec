Name:       util-linux
Version:    2.33.1
Release:    2
Summary:    util-linux is a random collection of Linux utilities
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
util-linux is a random collection of Linux utilities

%prep
%setup -q -a0

%build
%configure  ADJTIME_PATH=/var/lib/hwclock/adjtime   \
            --docdir=/usr/share/doc/util-linux-2.33.1 \
            --disable-chfn-chsh  \
            --disable-login      \
            --disable-nologin    \
            --disable-su         \
            --disable-setpriv    \
            --disable-runuser    \
            --disable-pylibmount \
            --disable-static     \
            --without-python     \
            --without-systemd    \
            --without-systemdsystemunitdir \
            --disable-makeinstall-chown
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/cal
/usr/bin/chmem
/usr/bin/choom
/usr/bin/chrt
/usr/bin/col
/usr/bin/colcrt
/usr/bin/colrm
/usr/bin/column
/usr/bin/dmesg
/usr/bin/eject
/usr/bin/fallocate
/usr/bin/fincore
/usr/bin/findmnt
/usr/bin/flock
/usr/bin/getopt
/usr/bin/hexdump
/usr/bin/i386
/usr/bin/ionice
/usr/bin/ipcmk
/usr/bin/ipcrm
/usr/bin/ipcs
/usr/bin/isosize
/usr/bin/kill
/usr/bin/last
/usr/bin/lastb
/usr/bin/linux32
/usr/bin/linux64
/usr/bin/logger
/usr/bin/look
/usr/bin/lsblk
/usr/bin/lscpu
/usr/bin/lsipc
/usr/bin/lslocks
/usr/bin/lslogins
/usr/bin/lsmem
/usr/bin/lsns
/usr/bin/mcookie
/usr/bin/mesg
/usr/bin/more
/usr/bin/mount
/usr/bin/mountpoint
/usr/bin/namei
/usr/bin/nsenter
/usr/bin/prlimit
/usr/bin/rename
/usr/bin/renice
/usr/bin/rev
/usr/bin/script
/usr/bin/scriptreplay
/usr/bin/setarch
/usr/bin/setsid
/usr/bin/setterm
/usr/bin/taskset
/usr/bin/ul
/usr/bin/umount
/usr/bin/uname26
/usr/bin/unshare
/usr/bin/utmpdump
/usr/bin/uuidgen
/usr/bin/uuidparse
/usr/bin/wall
/usr/bin/wdctl
/usr/bin/whereis
/usr/bin/x86_64
/usr/include/blkid/blkid.h
/usr/include/libfdisk/libfdisk.h
/usr/include/libmount/libmount.h
/usr/include/libsmartcols/libsmartcols.h
/usr/include/uuid/uuid.h
/usr/lib64/libblkid.la
/usr/lib64/libblkid.so
/usr/lib64/libblkid.so.1
/usr/lib64/libblkid.so.1.1.0
/usr/lib64/libfdisk.la
/usr/lib64/libfdisk.so
/usr/lib64/libfdisk.so.1
/usr/lib64/libfdisk.so.1.1.0
/usr/lib64/libmount.la
/usr/lib64/libmount.so
/usr/lib64/libmount.so.1
/usr/lib64/libmount.so.1.1.0
/usr/lib64/libsmartcols.la
/usr/lib64/libsmartcols.so
/usr/lib64/libsmartcols.so.1
/usr/lib64/libsmartcols.so.1.1.0
/usr/lib64/libuuid.la
/usr/lib64/libuuid.so
/usr/lib64/libuuid.so.1
/usr/lib64/libuuid.so.1.3.0
/usr/lib64/pkgconfig/blkid.pc
/usr/lib64/pkgconfig/fdisk.pc
/usr/lib64/pkgconfig/mount.pc
/usr/lib64/pkgconfig/smartcols.pc
/usr/lib64/pkgconfig/uuid.pc
/usr/sbin/addpart
/usr/sbin/agetty
/usr/sbin/blkdiscard
/usr/sbin/blkid
/usr/sbin/blkzone
/usr/sbin/blockdev
/usr/sbin/cfdisk
/usr/sbin/chcpu
/usr/sbin/ctrlaltdel
/usr/sbin/delpart
/usr/sbin/fdformat
/usr/sbin/fdisk
/usr/sbin/findfs
/usr/sbin/fsck
/usr/sbin/fsck.cramfs
/usr/sbin/fsck.minix
/usr/sbin/fsfreeze
/usr/sbin/fstrim
/usr/sbin/hwclock
/usr/sbin/ldattach
/usr/sbin/losetup
/usr/sbin/mkfs
/usr/sbin/mkfs.bfs
/usr/sbin/mkfs.cramfs
/usr/sbin/mkfs.minix
/usr/sbin/mkswap
/usr/sbin/partx
/usr/sbin/pivot_root
/usr/sbin/readprofile
/usr/sbin/resizepart
/usr/sbin/rfkill
/usr/sbin/rtcwake
/usr/sbin/sfdisk
/usr/sbin/sulogin
/usr/sbin/swaplabel
/usr/sbin/swapoff
/usr/sbin/swapon
/usr/sbin/switch_root
/usr/sbin/uuidd
/usr/sbin/wipefs
/usr/sbin/zramctl
/usr/share/doc/util-linux-2.33.1/getopt/getopt-parse.bash
/usr/share/doc/util-linux-2.33.1/getopt/getopt-parse.tcsh
/usr/share/locale/
/usr/share/bash-completion/
/usr/share/man/

%changelog
* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 2.33.1-2
- /sbin/raw is no longer built automatically with kernerls past 5.4 as raw.h was removed from kernel headers
