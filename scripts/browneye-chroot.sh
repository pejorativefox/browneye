#!/bin/bash
ROOT=$1


mount -v --bind /dev $ROOT/dev
mount -vt devpts devpts $ROOT/dev/pts -o gid=5,mode=620
mount -vt proc proc $ROOT/proc
mount -vt sysfs sysfs $ROOT/sys
mount -vt tmpfs tmpfs $ROOT/run

if [ -h $ROOT/dev/shm ]; then
  mkdir -pv $ROOT/$(readlink $ROOT/dev/shm)
fi

chroot "$ROOT" /usr/bin/bash --login +h

sudo umount $ROOT/run
sudo umount $ROOT/sys
sudo umount $ROOT/proc
sudo umount $ROOT/dev/pts
sudo umount $ROOT/dev

