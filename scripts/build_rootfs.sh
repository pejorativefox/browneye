#!/bin/bash

set -ex

ROOT="`pwd`/build/root_fs"

mkdir -pv $ROOT

./scripts/install.sh $ROOT
./scripts/chroot.sh $ROOT "/bin/dnf-3 -y install build-essential"

pushd $ROOT
tar cf ../browneye-rootfs.tar *
popd

gzip build/browneye-rootfs.tar
