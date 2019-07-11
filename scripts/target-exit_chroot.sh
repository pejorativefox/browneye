#!/bin/bash

LFS=/home/daspork/browneye/root/mnt/target

sudo umount $LFS/run
sudo umount $LFS/sys
sudo umount $LFS/proc
sudo umount $LFS/dev/pts
sudo umount $LFS/dev
