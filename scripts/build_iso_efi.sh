#/bin/bash

ROOT="`pwd`/build/iso_build"
SQUASH_ROOT=$ROOT/squash_root
CD_ROOT=$ROOT/cd_root

echo $ROOT
echo $SQUASH_ROOT
echo $CD_ROOT

mkdir -pv $SQUASH_ROOT

./scripts/install.sh $SQUASH_ROOT

mkdir -pv $CD_ROOT/EFI/BOOT/
mkdir -pv $CD_ROOT/boot/grub/x86_64-efi

cp /usr/lib64/grub/x86_64-efi/*.mod $CD_ROOT/boot/grub/x86_64-efi
cp iso/grub-stub.cfg $CD_ROOT/boot/grub

grub-mkimage -o $CD_ROOT/EFI/BOOT/bootx64.efi \
	     -c iso/grub-stub.cfg \
	     -p '(memdisk)/boot/grub' \
             -O x86_64-efi \
             search iso9660 configfile normal memdisk tar fat

dd if=/dev/zero of=$CD_ROOT/EFI/BOOT/efiboot.img bs=512 count=2880
mkfs.fat -F 12 -n 'EFIBOOTISO' $CD_ROOT/EFI/BOOT/efiboot.img

mmd -i $CD_ROOT/EFI/BOOT/efiboot.img ::EFI
mmd -i $CD_ROOT/EFI/BOOT/efiboot.img ::EFI/BOOT


mcopy -i $CD_ROOT/EFI/BOOT/efiboot.img $CD_ROOT/EFI/BOOT/bootx64.efi ::EFI/BOOT/bootx64.efi
mcopy -i $CD_ROOT/EFI/BOOT/efiboot.img iso/grub-stub.cfg ::EFI/BOOT/grub-stub.cfg

mkdir -pv $CD_ROOT/boot
mkdir -pv $CD_ROOT/LiveOS
mksquashfs $SQUASH_ROOT $CD_ROOT/LiveOS/squashfs.img

dracut --no-hostonly --add "dmsquash-live pollcdrom" $CD_ROOT/boot/initrd.img

cp /boot/vmlinuz-5.6.14 $CD_ROOT/boot/vmlinuz
cp iso/grub.cfg $CD_ROOT/boot/grub

xorriso -as mkisofs \
	-V 'BROWNEYE' \
        -e /EFI/BOOT/efiboot.img \
	-no-emul-boot \
	-o ./build/browneye.iso $CD_ROOT
