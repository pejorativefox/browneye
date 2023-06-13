#/bin/bash

ROOT="`pwd`/build/iso_build"
SQUASH_ROOT=$ROOT/squash_root
CD_ROOT=$ROOT/cd_root

echo $ROOT
echo $SQUASH_ROOT
echo $CD_ROOT

mkdir -pv $SQUASH_ROOT

./scripts/install.sh $SQUASH_ROOT

mkdir -pv $CD_ROOT/isolinux/kernel
cp /share/syslinux/isolinux.bin $CD_ROOT/isolinux
# modules
cp /share/syslinux/ldlinux.c32 $CD_ROOT/isolinux
cp /share/syslinux/vesamenu.c32 $CD_ROOT/isolinux
cp /share/syslinux/libcom32.c32 $CD_ROOT/isolinux
cp /share/syslinux/libutil.c32 $CD_ROOT/isolinux


cp /share/syslinux/memdisk $CD_ROOT/isolinux/kernel
cp ./iso/isolinux.cfg $CD_ROOT/isolinux

mkdir -pv $CD_ROOT/boot
mkdir -pv $CD_ROOT/LiveOS
mksquashfs $SQUASH_ROOT $CD_ROOT/LiveOS/squashfs.img

dracut --no-hostonly --add "dmsquash-live pollcdrom" $CD_ROOT/boot/initrd.img
cp /boot/vmlinuz-5.6.14 $CD_ROOT/boot/vmlinuz

genisoimage -o ./build/browneye.iso -V BrowneyeLive \
            -b isolinux/isolinux.bin -c isolinux/boot.cat \
	    -no-emul-boot -boot-load-size 4 -boot-info-table -debug $CD_ROOT

isohybrid ./build/browneye.iso
