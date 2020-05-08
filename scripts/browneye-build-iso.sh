#/bin/bash

ROOT="`pwd`/iso_build"
SQUASH_ROOT=$ROOT/squash_root
CD_ROOT=$ROOT/cd_root

echo $ROOT
echo $SQUASH_ROOT
echo $CD_ROOT

mkdir -pv $SQUASH_ROOT
pushd $SQUASH_ROOT
mkdir -pv {dev,proc,sys,lib,home,tmp,root,boot}

ln -sv lib lib64
ln -sv . usr

mknod -m 600 dev/console c 5 1
mknod -m 666 dev/null c 1 3

# /tmp
chmod -v 777 tmp
chmod -v +t tmp

# /var 
mkdir -pv var
mkdir -pv var/{log,mail,spool}
mkdir -pv var/{opt,cache,lib/{color,misc,locate},local}

# /run
mkdir -pv run
ln -sv ../run var/run
touch run/utmp
mkdir -pv run/lock
ln -sv ../run/lock var/lock

# yup setup
mkdir -pv etc/yum.repos.d
cp /etc/yum.repos.d/core.repo etc/yum.repos.d/

popd

dnf-3 --installroot $SQUASH_ROOT --releasever=1 -y  install \
	bash rpm dnf


mkdir -pv $CD_ROOT/isolinux/kernel
cp /share/syslinux/isolinux.bin $CD_ROOT/isolinux
cp /share/syslinux/ldlinux.c32 $CD_ROOT/isolinux
cp /share/syslinux/memdisk $CD_ROOT/isolinux/kernel

mksquashfs $SQUASH_ROOT $CD_ROOT/brown.sqsh

genisoimage -o output.iso \
            -b isolinux/isolinux.bin -c isolinux/boot.cat \
	    -no-emul-boot -boot-load-size 4 -boot-info-table -debug $CD_ROOT
