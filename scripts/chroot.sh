#!/bin/bash -ex
ROOT=$1


mount -v --bind /dev $ROOT/dev
mount -vt devpts devpts $ROOT/dev/pts -o gid=5,mode=620
mount -vt proc proc $ROOT/proc
mount -vt sysfs sysfs $ROOT/sys
mount -vt tmpfs tmpfs $ROOT/run

if [ -h $ROOT/dev/shm ]; then
  mkdir -pv $ROOT/$(readlink $ROOT/dev/shm)
fi

COMMAND="/usr/bin/bash --login +h"


if [ -z "$2" ]
  then
    echo "No argument supplied"
  else
    COMMAND=$2
fi
echo ">>> $COMMAND"

chroot $ROOT $COMMAND

umount $ROOT/run
umount $ROOT/sys
umount $ROOT/proc
umount $ROOT/dev/pts
umount $ROOT/dev

