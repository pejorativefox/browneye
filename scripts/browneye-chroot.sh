#!/bin/bash
LFS=$1


mount -v --bind /dev $LFS/dev
mount -vt devpts devpts $LFS/dev/pts -o gid=5,mode=620
mount -vt proc proc $LFS/proc
mount -vt sysfs sysfs $LFS/sys
mount -vt tmpfs tmpfs $LFS/run

if [ -h $LFS/dev/shm ]; then
  mkdir -pv $LFS/$(readlink $LFS/dev/shm)
fi

chroot "$LFS" /usr/bin/bash --login +h

sudo umount $LFS/run
sudo umount $LFS/sys
sudo umount $LFS/proc
sudo umount $LFS/dev/pts
sudo umount $LFS/dev

