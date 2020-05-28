#!/bin/bash -ex

ROOT=$1

./scripts/create_root_filesystem.sh $ROOT

cp ./iso/core.repo $ROOT/etc/yum.repos.d/
cp /etc/resolv.conf $ROOT/etc/

dnf-3 --installroot $ROOT --releasever=1 -y -x busybox install \
	browneye-release browneye-sysconfig dnf dnf-plugins-core make-ca
./scripts/chroot.sh $ROOT "/bin/dnf-3 -y -x busybox install system-minimal"
./scripts/chroot.sh $ROOT "ln -s /etc/finit.d/available/networkmanager.conf /etc/finit.d/"
