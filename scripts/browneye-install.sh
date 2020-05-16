#/bin/bash

ROOT=$1

pushd $ROOT

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

mkdir -pv etc/yum.repos.d
cp /etc/yum.repos.d/core.repo etc/yum.repos.d/

popd

dnf-3 --installroot $ROOT --releasever=1 -y -x busybox install browneye-release browneye-sysconfig coreutils
dnf-3 --installroot $ROOT --releasever=1 -y -x busybox install dnf shadow linux-pam

./scripts/browneye-chroot.sh $ROOT "/bin/dnf-3 -y -x busybox install NetworkManager polkit linux-kernel linux-modules finit p11-kit make-ca grep sed gawk e2fsprogs sysklogd"
