#/bin/bash

ROOT="`pwd`/build/root_fs"

mkdir -pv $ROOT
./scripts/create_root_filesystem.sh $ROOT

cp ./iso/core.repo $ROOT/etc/yum.repos.d/
cp /etc/resolv.conf $ROOT/etc/

dnf-3 --installroot $ROOT --releasever=1 -y -x busybox install \
        browneye-release browneye-sysconfig dnf dnf-plugins-core make-ca
#./scripts/chroot.sh $ROOT "/bin/dnf-3 -y -x busybox install system-minimal"
#./scripts/chroot.sh $ROOT "ln -s /etc/finit.d/available/networkmanager.conf /etc/finit.d/"

./scripts/chroot.sh $ROOT "/bin/dnf-3 -y install \
	gcc patch binutils linux-headers make \
	diffutils tar gzip sed gawk flex bison \
	tar gzip gcc binutils findutils"

pushd $ROOT
tar cf ../browneye-rootfs.tar *
popd

gzip build/browneye-rootfs.tar
