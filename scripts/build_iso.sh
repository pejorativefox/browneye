#!/bin/bash -ex

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

KERNEL="$(basename $(ls -1r --sort=version ${SQUASH_ROOT}/boot/vmlinuz* | head -n 1))"
KERNEL_VER="${KERNEL#vmlinuz-}"

depmod -b "${SQUASH_ROOT}" "${KERNEL_VER}"

DRACUT_KMODDIR_OVERRIDE=1 dracut \
  --no-hostonly \
  --add "dmsquash-live pollcdrom" \
  --kernel-image "${SQUASH_ROOT}/boot/${KERNEL}" \
  --kver "${KERNEL_VER}" \
  --kmoddir "${SQUASH_ROOT}/lib/modules/${KERNEL_VER}" \
  "$CD_ROOT/boot/initrd.img"

mv -v "${SQUASH_ROOT}/boot/${KERNEL}" $CD_ROOT/boot/vmlinuz

mksquashfs $SQUASH_ROOT $CD_ROOT/LiveOS/squashfs.img

genisoimage -o ./build/browneye.iso -V BrowneyeLive \
            -b isolinux/isolinux.bin -c isolinux/boot.cat \
	    -no-emul-boot -boot-load-size 4 -boot-info-table -debug $CD_ROOT

isohybrid ./build/browneye.iso
