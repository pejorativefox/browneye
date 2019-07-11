#!/bin/bash

set +h
set -e
umask 022

export LC_ALL=POSIX
export PATH=/tools/bin:/bin:/usr/bin
export LFS_TGT=$(uname -m)-lfs-linux-gnu

# root path
export LFS=/home/daspork/browneye/root
sudo rm -rf ${LFS}
mkdir -pv ${LFS}


# make tools/cross-tools directories
sudo rm -rf /tools
install -dv ${LFS}/tools
sudo ln -sv ${LFS}/tools /

# makeflags
export MAKEFLAGS='-j 8'

# clean and create the build directory
rm -rf ${LFS}/build
mkdir -pv ${LFS}/build
export LFS_BUILD=${LFS}/build

# Un-tar sources
# sources path
mkdir -pv ${LFS}/sources
pushd ${LFS}/sources
tar xf ../../lfs-packages-8.4.tar
popd
export LFS_SOURCES=${LFS}/sources/8.4


# 5.4 BINUTILS
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/binutils-2.32.tar.xz
mkdir -pv binutils-build
pushd  ${LFS_BUILD}/binutils-build
../binutils-2.32/configure --prefix=/tools \
             --with-sysroot=$LFS        \
             --with-lib-path=/tools/lib \
             --target=$LFS_TGT          \
             --disable-nls              \
             --disable-werror
make
case $(uname -m) in
  x86_64) mkdir -v /tools/lib && ln -sv lib /tools/lib64 ;;
esac
make install
popd
rm -rf binutils-build binutils-2.32
popd


# 5.5 GCC pass 1
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/gcc-8.2.0.tar.xz
pushd ${LFS_BUILD}/gcc-8.2.0

tar -xf ${LFS_SOURCES}/mpfr-4.0.2.tar.xz
mv -v mpfr-4.0.2 mpfr
tar -xf ${LFS_SOURCES}/gmp-6.1.2.tar.xz
mv -v gmp-6.1.2 gmp
tar -xf ${LFS_SOURCES}/mpc-1.1.0.tar.gz
mv -v mpc-1.1.0 mpc

for file in gcc/config/{linux,i386/linux{,64}}.h
do
  cp -uv $file{,.orig}
  sed -e 's@/lib\(64\)\?\(32\)\?/ld@/tools&@g' \
      -e 's@/usr@/tools@g' $file.orig > $file
  echo '
#undef STANDARD_STARTFILE_PREFIX_1
#undef STANDARD_STARTFILE_PREFIX_2
#define STANDARD_STARTFILE_PREFIX_1 "/tools/lib/"
#define STANDARD_STARTFILE_PREFIX_2 ""' >> $file
  touch $file.orig
done

case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
 ;;
esac

mkdir -pv build
pushd build
../configure                                       \
    --target=$LFS_TGT                              \
    --prefix=/tools                                \
    --with-glibc-version=2.11                      \
    --with-sysroot=$LFS                            \
    --with-newlib                                  \
    --without-headers                              \
    --with-local-prefix=/tools                     \
    --with-native-system-header-dir=/tools/include \
    --disable-nls                                  \
    --disable-shared                               \
    --disable-multilib                             \
    --disable-decimal-float                        \
    --disable-threads                              \
    --disable-libatomic                            \
    --disable-libgomp                              \
    --disable-libmpx                               \
    --disable-libquadmath                          \
    --disable-libssp                               \
    --disable-libvtv                               \
    --disable-libstdcxx                            \
    --enable-languages=c,c++

make
make install
popd
popd
rm -rf gcc-8.2.0
popd


# 5.6 Kernel Headers
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/linux-4.20.12.tar.xz
pushd  ${LFS_BUILD}/linux-4.20.12
make mrproper
make INSTALL_HDR_PATH=dest headers_install
cp -rv dest/include/* /tools/include
popd
popd


# 5.7 Glibc
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/glibc-2.29.tar.xz
pushd  ${LFS_BUILD}/glibc-2.29
mkdir build
pushd ${LFS_BUILD}/glibc-2.29/build
../configure                             \
      --prefix=/tools                    \
      --host=$LFS_TGT                    \
      --build=$(../scripts/config.guess) \
      --enable-kernel=3.2                \
      --with-headers=/tools/include
make
make install
popd
popd
rm -rf glibc-2.29
popd


# 5.8 Libstdc++
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/gcc-8.2.0.tar.xz
pushd  ${LFS_BUILD}/gcc-8.2.0
mkdir -pv build
pushd build
../libstdc++-v3/configure           \
    --host=$LFS_TGT                 \
    --prefix=/tools                 \
    --disable-multilib              \
    --disable-nls                   \
    --disable-libstdcxx-threads     \
    --disable-libstdcxx-pch         \
    --with-gxx-include-dir=/tools/$LFS_TGT/include/c++/8.2.0
make
make install
popd
popd
rm -rf gcc-8.2.0
popd


# 5.9 Binutils pass 2
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/binutils-2.32.tar.xz
mkdir -pv binutils-build
pushd  ${LFS_BUILD}/binutils-build
CC=$LFS_TGT-gcc                \
AR=$LFS_TGT-ar                 \
RANLIB=$LFS_TGT-ranlib         \
../binutils-2.32/configure     \
    --prefix=/tools            \
    --disable-nls              \
    --disable-werror           \
    --with-lib-path=/tools/lib \
    --with-sysroot
make
make install
make -C ld clean
make -C ld LIB_PATH=/usr/lib:/lib
cp -v ld/ld-new /tools/bin
popd
rm -rf binutils-build binutils-2.32
popd


# 5.10. GCC-8.2.0 - Pass 2
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/gcc-8.2.0.tar.xz
pushd ${LFS_BUILD}/gcc-8.2.0

cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
  `dirname $($LFS_TGT-gcc -print-libgcc-file-name)`/include-fixed/limits.h

for file in gcc/config/{linux,i386/linux{,64}}.h
do
  cp -uv $file{,.orig}
  sed -e 's@/lib\(64\)\?\(32\)\?/ld@/tools&@g' \
      -e 's@/usr@/tools@g' $file.orig > $file
  echo '
#undef STANDARD_STARTFILE_PREFIX_1
#undef STANDARD_STARTFILE_PREFIX_2
#define STANDARD_STARTFILE_PREFIX_1 "/tools/lib/"
#define STANDARD_STARTFILE_PREFIX_2 ""' >> $file
  touch $file.orig
done

case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
  ;;
esac

tar -xf ${LFS_SOURCES}/mpfr-4.0.2.tar.xz
mv -v mpfr-4.0.2 mpfr
tar -xf ${LFS_SOURCES}/gmp-6.1.2.tar.xz
mv -v gmp-6.1.2 gmp
tar -xf ${LFS_SOURCES}/mpc-1.1.0.tar.gz
mv -v mpc-1.1.0 mpc

mkdir -pv build
pushd build
CC=$LFS_TGT-gcc                                    \
CXX=$LFS_TGT-g++                                   \
AR=$LFS_TGT-ar                                     \
RANLIB=$LFS_TGT-ranlib                             \
../configure                                       \
    --prefix=/tools                                \
    --with-local-prefix=/tools                     \
    --with-native-system-header-dir=/tools/include \
    --enable-languages=c,c++                       \
    --disable-libstdcxx-pch                        \
    --disable-multilib                             \
    --disable-bootstrap                            \
    --disable-libgomp

make
make install
ln -sv gcc /tools/bin/cc
popd
popd
rm -rf gcc-8.2.0
popd


# 5.11.1. Installation of Tcl
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/tcl8.6.9-src.tar.gz
pushd  ${LFS_BUILD}/tcl8.6.9
pushd unix
./configure --prefix=/tools
make
# TZ=UTC make test
make install
chmod -v u+w /tools/lib/libtcl8.6.so
make install-private-headers
ln -sv tclsh8.6 /tools/bin/tclsh
popd
popd
rm -rf tcl8.6.9
popd


# 5.12. Expect-5.45.4
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/expect5.45.4.tar.gz
pushd  ${LFS_BUILD}/expect5.45.4
cp -v configure{,.orig}
sed 's:/usr/local/bin:/bin:' configure.orig > configure
./configure --prefix=/tools       \
            --with-tcl=/tools/lib \
            --with-tclinclude=/tools/include
make
make test
make SCRIPTS="" install
popd
rm -rf expect5.45.4
popd


# 5.13. DejaGNU-1.6.2
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/dejagnu-1.6.2.tar.gz
pushd  ${LFS_BUILD}/dejagnu-1.6.2
./configure --prefix=/tools
make install
make check
popd
rm -rf dejagnu-1.6.2
popd


# 5.14.1. Installation of M4
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/m4-1.4.18.tar.xz
pushd  ${LFS_BUILD}/m4-1.4.18
sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' lib/*.c
echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio-impl.h
./configure --prefix=/tools
make
make check
make install
popd
rm -rf m4-1.4.18
popd


# BUSYBOX!!!! OPTIONAL
# pushd ${LFS_BUILD}
# tar xf /home/daspork/browneye/cache/busybox-1.28.3.tar.bz2
# pushd  ${LFS_BUILD}/busybox-1.28.3
# make CROSS_COMPILE="${LFS_TGT}-" defconfig
# make CROSS_COMPILE="${LFS_TGT}-"
# make CROSS_COMPILE="${LFS_TGT}-" CONFIG_PREFIX="/tools" install
# cp -v examples/depmod.pl /tools/bin
# chmod 755 /tools/bin/depmod.pl
# popd
# popd

# 5.15. Ncurses-6.1
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/ncurses-6.1.tar.gz
pushd  ${LFS_BUILD}/ncurses-6.1
sed -i s/mawk// configure
./configure --prefix=/tools \
            --with-shared   \
            --without-debug \
            --without-ada   \
            --enable-widec  \
            --enable-overwrite
make
make install
ln -s libncursesw.so /tools/lib/libncurses.so
popd
rm -rf ncurses-6.1
popd


# 5.16. Bash-5.0
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/bash-5.0.tar.gz
pushd  ${LFS_BUILD}/bash-5.0
./configure --prefix=/tools --without-bash-malloc
make
make tests
make install
ln -sv bash /tools/bin/sh
popd
rm -rf bash-5.0
popd


# 5.17. Bison-3.3.2
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/bison-3.3.2.tar.xz
pushd  ${LFS_BUILD}/bison-3.3.2
./configure --prefix=/tools
make
# make check
make install
popd
rm -rf bison-3.3.2
popd


# 5.18. Bzip2-1.0.6
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/bzip2-1.0.6.tar.gz
pushd  ${LFS_BUILD}/bzip2-1.0.6
make
make PREFIX=/tools install
popd
rm -rf bzip2-1.0.6
popd


# 5.19. Coreutils-8.30
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/coreutils-8.30.tar.xz
pushd  ${LFS_BUILD}/coreutils-8.30
./configure --prefix=/tools --enable-install-program=hostname
make
make RUN_EXPENSIVE_TESTS=yes check
make install
popd
rm -rf coreutils-8.30
popd


# 5.20. Diffutils-3.7
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/diffutils-3.7.tar.xz
pushd  ${LFS_BUILD}/diffutils-3.7
./configure --prefix=/tools
make
make check
make install
popd
rm -rf diffutils-3.7
popd


# 5.21. File-5.36
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/file-5.36.tar.gz
pushd  ${LFS_BUILD}/file-5.36
./configure --prefix=/tools
make
make check
make install
popd
rm -rf file-5.36
popd


# 5.22. Findutils-4.6.0
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/findutils-4.6.0.tar.gz
pushd  ${LFS_BUILD}/findutils-4.6.0
sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' gl/lib/*.c
sed -i '/unistd/a #include <sys/sysmacros.h>' gl/lib/mountlist.c
echo "#define _IO_IN_BACKUP 0x100" >> gl/lib/stdio-impl.h
./configure --prefix=/tools
make
make check
make install
popd
rm -rf findutils-4.6.0
popd


# 5.23. Gawk-4.2.1
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/gawk-4.2.1.tar.xz
pushd  ${LFS_BUILD}/gawk-4.2.1
./configure --prefix=/tools
make
# make check
make install
popd
rm -rf gawk-4.2.1
popd


# 5.24. Gettext-0.19.8.1
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/gettext-0.19.8.1.tar.xz
pushd  ${LFS_BUILD}/gettext-0.19.8.1
pushd gettext-tools
EMACS="no" ./configure --prefix=/tools --disable-shared
make -C gnulib-lib
make -C intl pluralx.c
make -C src msgfmt
make -C src msgmerge
make -C src xgettext
cp -v src/{msgfmt,msgmerge,xgettext} /tools/bin
popd
popd
rm -rf gettext-0.19.8.1
popd


# 5.25. Grep-3.3
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/grep-3.3.tar.xz
pushd  ${LFS_BUILD}/grep-3.3
./configure --prefix=/tools
make
make check
make install
popd
rm -rf grep-3.3
popd


# 5.26. Gzip-1.10
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/gzip-1.10.tar.xz
pushd  ${LFS_BUILD}/gzip-1.10
./configure --prefix=/tools
make
make check
make install
popd
rm -rf gzip-1.10
popd


# 5.27. Make-4.2.1
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/make-4.2.1.tar.bz2
pushd  ${LFS_BUILD}/make-4.2.1
sed -i '211,217 d; 219,229 d; 232 d' glob/glob.c
./configure --prefix=/tools --without-guile
make
# make check
make install
popd
rm -rf make-4.2.1
popd


# 5.28. Patch-2.7.6
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/patch-2.7.6.tar.xz
pushd  ${LFS_BUILD}/patch-2.7.6
./configure --prefix=/tools
make
make check
make install
popd
rm -rf patch-2.7.6
popd


# 5.29. Perl-5.28.1
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/perl-5.28.1.tar.xz
pushd  ${LFS_BUILD}/perl-5.28.1
sh Configure -des -Dprefix=/tools -Dlibs=-lm -Uloclibpth -Ulocincpth
make
cp -v perl cpan/podlators/scripts/pod2man /tools/bin
mkdir -pv /tools/lib/perl5/5.28.1
cp -Rv lib/* /tools/lib/perl5/5.28.1
popd
rm -rf perl-5.28.1
popd


# 5.30. Python-3.7.2
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/Python-3.7.2.tar.xz
pushd  ${LFS_BUILD}/Python-3.7.2
sed -i '/def add_multiarch_paths/a \        return' setup.py
./configure --prefix=/tools --without-ensurepip
make
make install
popd
rm -rf patch-2.7.6
popd


# 5.31. Sed-4.7
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/sed-4.7.tar.xz
pushd  ${LFS_BUILD}/sed-4.7
./configure --prefix=/tools
make
make check
make install
popd
rm -rf sed-4.7
popd


# 5.32. Tar-1.31
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/tar-1.31.tar.xz
pushd  ${LFS_BUILD}/tar-1.31
./configure --prefix=/tools
make
# make check
make install
popd
rm -rf tar-1.31
popd


# 5.33. Texinfo-6.5
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/texinfo-6.5.tar.xz
pushd  ${LFS_BUILD}/texinfo-6.5
./configure --prefix=/tools
make
# make check
make install
popd
rm -rf texinfo-6.5
popd


# 5.34. Xz-5.2.4
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/xz-5.2.4.tar.xz
pushd  ${LFS_BUILD}/xz-5.2.4
./configure --prefix=/tools
make
make check
make install
popd
rm -rf xz-5.2.4
popd


# 5.36. Changing Ownership
sudo chown -R root:root $LFS/tools


# 6.2 Prepare VKFS
mkdir -pv $LFS/{dev,proc,sys,run}
sudo mknod -m 600 $LFS/dev/console c 5 1
sudo mknod -m 666 $LFS/dev/null c 1 3
