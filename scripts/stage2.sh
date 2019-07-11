export LFS=/

# clean and create the build directory
rm -rf ${LFS}/build
mkdir -pv ${LFS}/build
export LFS_BUILD=${LFS}/build

# Un-tar sources
# sources path
export LFS_SOURCES=${LFS}/sources/8.4

# makeflags
export MAKEFLAGS='-j 8'

# # 6.5. Creating Directories
# mkdir -pv /{bin,boot,etc/{opt,sysconfig},home,lib/firmware,mnt,opt}
# mkdir -pv /{media/{floppy,cdrom},sbin,srv,var}
# install -dv -m 0750 /root
# install -dv -m 1777 /tmp /var/tmp
# mkdir -pv /usr/{,local/}{bin,include,lib,sbin,src}
# mkdir -pv /usr/{,local/}share/{color,dict,doc,info,locale,man}
# mkdir -v  /usr/{,local/}share/{misc,terminfo,zoneinfo}
# mkdir -v  /usr/libexec
# mkdir -pv /usr/{,local/}share/man/man{1..8}
#
# case $(uname -m) in
#  x86_64) mkdir -v /lib64 ;;
# esac
#
# mkdir -v /var/{log,mail,spool}
# ln -sv /run /var/run
# ln -sv /run/lock /var/lock
# mkdir -pv /var/{opt,cache,lib/{color,misc,locate},local}
#
#
# # 6.6. Creating Essential Files and Symlinks
# ln -sv /tools/bin/{bash,cat,chmod,dd,echo,ln,mkdir,pwd,rm,stty,touch} /bin
# ln -sv /tools/bin/{env,install,perl,printf}         /usr/bin
# ln -sv /tools/lib/libgcc_s.so{,.1}                  /usr/lib
# ln -sv /tools/lib/libstdc++.{a,so{,.6}}             /usr/lib
#
# install -vdm755 /usr/lib/pkgconfig
#
# ln -sv bash /bin/sh
#
# ln -sv /proc/self/mounts /etc/mtab
#
# cat > /etc/passwd << "EOF"
# root:x:0:0:root:/root:/bin/bash
# bin:x:1:1:bin:/dev/null:/bin/false
# daemon:x:6:6:Daemon User:/dev/null:/bin/false
# messagebus:x:18:18:D-Bus Message Daemon User:/var/run/dbus:/bin/false
# nobody:x:99:99:Unprivileged User:/dev/null:/bin/false
# EOF
#
# cat > /etc/group << "EOF"
# root:x:0:
# bin:x:1:daemon
# sys:x:2:
# kmem:x:3:
# tape:x:4:
# tty:x:5:
# daemon:x:6:
# floppy:x:7:
# disk:x:8:
# lp:x:9:
# dialout:x:10:
# audio:x:11:
# video:x:12:
# utmp:x:13:
# usb:x:14:
# cdrom:x:15:
# adm:x:16:
# messagebus:x:18:
# input:x:24:
# mail:x:34:
# kvm:x:61:
# wheel:x:97:
# nogroup:x:99:
# users:x:999:
# EOF
#
# # maybe problem area
# # exec /tools/bin/bash --login +h
#
# touch /var/log/{btmp,lastlog,faillog,wtmp}
# chgrp -v utmp /var/log/lastlog
# chmod -v 664  /var/log/lastlog
# chmod -v 600  /var/log/btmp
#
#
# # 6.7. Linux-4.20.12 API Headers
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/linux-4.20.12.tar.xz
# pushd  ${LFS_BUILD}/linux-4.20.12
# make mrproper
# make INSTALL_HDR_PATH=dest headers_install
# find dest/include \( -name .install -o -name ..install.cmd \) -delete
# cp -rv dest/include/* /usr/include
# popd
# rm -rf linux-4.20.12
# popd
#
#
# # 6.8. Man-pages-4.16
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/man-pages-4.16.tar.xz
# pushd  ${LFS_BUILD}/man-pages-4.16
# make install
# popd
# rm -rf man-pages-4.16
# popd
#
#
# # 6.9. Glibc-2.29
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/glibc-2.29.tar.xz
# pushd  ${LFS_BUILD}/glibc-2.29
# patch -Np1 -i /sources/8.4/glibc-2.29-fhs-1.patch
# ln -sfv /tools/lib/gcc /usr/lib
# case $(uname -m) in
#     i?86)    GCC_INCDIR=/usr/lib/gcc/$(uname -m)-pc-linux-gnu/8.2.0/include
#             ln -sfv ld-linux.so.2 /lib/ld-lsb.so.3
#     ;;
#     x86_64) GCC_INCDIR=/usr/lib/gcc/x86_64-pc-linux-gnu/8.2.0/include
#             ln -sfv ../lib/ld-linux-x86-64.so.2 /lib64
#             ln -sfv ../lib/ld-linux-x86-64.so.2 /lib64/ld-lsb-x86-64.so.3
#     ;;
# esac
# rm -f /usr/include/limits.h
# mkdir -v build
# pushd build
# CC="gcc -isystem $GCC_INCDIR -isystem /usr/include" \
# ../configure --prefix=/usr                          \
#              --disable-werror                       \
#              --enable-kernel=3.2                    \
#              --enable-stack-protector=strong        \
#              libc_cv_slibdir=/lib
# unset GCC_INCDIR
# make
# case $(uname -m) in
#   i?86)   ln -sfnv $PWD/elf/ld-linux.so.2        /lib ;;
#   x86_64) ln -sfnv $PWD/elf/ld-linux-x86-64.so.2 /lib ;;
# esac
# make check
# touch /etc/ld.so.conf
# sed '/test-installation/s@$(PERL)@echo not running@' -i ../Makefile
# make install
# cp -v ../nscd/nscd.conf /etc/nscd.conf
# mkdir -pv /var/cache/nscd
# mkdir -pv /usr/lib/locale
# localedef -i POSIX -f UTF-8 C.UTF-8 2> /dev/null || true
# localedef -i cs_CZ -f UTF-8 cs_CZ.UTF-8
# localedef -i de_DE -f ISO-8859-1 de_DE
# localedef -i de_DE@euro -f ISO-8859-15 de_DE@euro
# localedef -i de_DE -f UTF-8 de_DE.UTF-8
# localedef -i el_GR -f ISO-8859-7 el_GR
# localedef -i en_GB -f UTF-8 en_GB.UTF-8
# localedef -i en_HK -f ISO-8859-1 en_HK
# localedef -i en_PH -f ISO-8859-1 en_PH
# localedef -i en_US -f ISO-8859-1 en_US
# localedef -i en_US -f UTF-8 en_US.UTF-8
# localedef -i es_MX -f ISO-8859-1 es_MX
# localedef -i fa_IR -f UTF-8 fa_IR
# localedef -i fr_FR -f ISO-8859-1 fr_FR
# localedef -i fr_FR@euro -f ISO-8859-15 fr_FR@euro
# localedef -i fr_FR -f UTF-8 fr_FR.UTF-8
# localedef -i it_IT -f ISO-8859-1 it_IT
# localedef -i it_IT -f UTF-8 it_IT.UTF-8
# localedef -i ja_JP -f EUC-JP ja_JP
# localedef -i ja_JP -f SHIFT_JIS ja_JP.SIJS 2> /dev/null || true
# localedef -i ja_JP -f UTF-8 ja_JP.UTF-8
# localedef -i ru_RU -f KOI8-R ru_RU.KOI8-R
# localedef -i ru_RU -f UTF-8 ru_RU.UTF-8
# localedef -i tr_TR -f UTF-8 tr_TR.UTF-8
# localedef -i zh_CN -f GB18030 zh_CN.GB18030
# localedef -i zh_HK -f BIG5-HKSCS zh_HK.BIG5-HKSCS
# make localedata/install-locales
#
# cat > /etc/nsswitch.conf << "EOF"
# # Begin /etc/nsswitch.conf
#
# passwd: files
# group: files
# shadow: files
#
# hosts: files dns
# networks: files
#
# protocols: files
# services: files
# ethers: files
# rpc: files
#
# # End /etc/nsswitch.conf
# EOF
#
# tar xf ${LFS_SOURCES}/tzdata2018i.tar.gz
#
# ZONEINFO=/usr/share/zoneinfo
# mkdir -pv $ZONEINFO/{posix,right}
#
# for tz in etcetera southamerica northamerica europe africa antarctica  \
#           asia australasia backward pacificnew systemv; do
#     zic -L /dev/null   -d $ZONEINFO       ${tz}
#     zic -L /dev/null   -d $ZONEINFO/posix ${tz}
#     zic -L leapseconds -d $ZONEINFO/right ${tz}
# done
#
# cp -v zone.tab zone1970.tab iso3166.tab $ZONEINFO
# zic -d $ZONEINFO -p America/New_York
# unset ZONEINFO
#
# cp -v /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime
#
# cat > /etc/ld.so.conf << "EOF"
# # Begin /etc/ld.so.conf
# /usr/local/lib
# /opt/lib
#
# EOF
#
# cat >> /etc/ld.so.conf << "EOF"
# # Add an include directory
# include /etc/ld.so.conf.d/*.conf
#
# EOF
# mkdir -pv /etc/ld.so.conf.d
#
# popd
# popd
# rm -rf glibc-2.29
# popd
#
#
# # 6.10. Adjusting the Toolchain
# mv -v /tools/bin/{ld,ld-old}
# mv -v /tools/$(uname -m)-pc-linux-gnu/bin/{ld,ld-old}
# mv -v /tools/bin/{ld-new,ld}
# ln -sv /tools/bin/ld /tools/$(uname -m)-pc-linux-gnu/bin/ld
#
# gcc -dumpspecs | sed -e 's@/tools@@g'                   \
#     -e '/\*startfile_prefix_spec:/{n;s@.*@/usr/lib/ @}' \
#     -e '/\*cpp:/{n;s@$@ -isystem /usr/include@}' >      \
#     `dirname $(gcc --print-libgcc-file-name)`/specs
#
#
#
# # 6.11. Zlib-1.2.11
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/zlib-1.2.11.tar.xz
# pushd  ${LFS_BUILD}/zlib-1.2.11
# ./configure --prefix=/usr
# make
# make check
# make install
# mv -v /usr/lib/libz.so.* /lib
# ln -sfv ../../lib/$(readlink /usr/lib/libz.so) /usr/lib/libz.so
# popd
# rm -rf zlib-1.2.11
# popd
#
#
# # 6.12. File-5.36
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/file-5.36.tar.gz
# pushd  ${LFS_BUILD}/file-5.36
# ./configure --prefix=/usr
# make
# make check
# make install
# popd
# rm -rf file-5.36
# popd
#
#
# # 6.13. Readline-8.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/readline-8.0.tar.gz
# pushd  ${LFS_BUILD}/readline-8.0
# sed -i '/MV.*old/d' Makefile.in
# sed -i '/{OLDSUFF}/c:' support/shlib-install
# ./configure --prefix=/usr    \
#             --disable-static \
#             --docdir=/usr/share/doc/readline-8.0
# make SHLIB_LIBS="-L/tools/lib -lncursesw"
# make SHLIB_LIBS="-L/tools/lib -lncursesw" install
# mv -v /usr/lib/lib{readline,history}.so.* /lib
# chmod -v u+w /lib/lib{readline,history}.so.*
# ln -sfv ../../lib/$(readlink /usr/lib/libreadline.so) /usr/lib/libreadline.so
# ln -sfv ../../lib/$(readlink /usr/lib/libhistory.so ) /usr/lib/libhistory.so
# install -v -m644 doc/*.{ps,pdf,html,dvi} /usr/share/doc/readline-8.0
# popd
# rm -rf readline-8.0
# popd
#
#
# # 6.14. M4-1.4.18
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/m4-1.4.18.tar.xz
# pushd  ${LFS_BUILD}/m4-1.4.18
# sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' lib/*.c
# echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio-impl.h
# ./configure --prefix=/usr
# make
# make check
# make install
# popd
# rm -rf m4-1.4.18
# popd
#
#
# # 6.15. Bc-1.07.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/bc-1.07.1.tar.gz
# pushd  ${LFS_BUILD}/bc-1.07.1
# cat > bc/fix-libmath_h << "EOF"
# #! /bin/bash
# sed -e '1   s/^/{"/' \
#     -e     's/$/",/' \
#     -e '2,$ s/^/"/'  \
#     -e   '$ d'       \
#     -i libmath.h
#
# sed -e '$ s/$/0}/' \
#     -i libmath.h
# EOF
#
# ln -sv /tools/lib/libncursesw.so.6 /usr/lib/libncursesw.so.6
# ln -sfv libncursesw.so.6 /usr/lib/libncurses.so
# sed -i -e '/flex/s/as_fn_error/: ;; # &/' configure
#
# ./configure --prefix=/usr           \
#             --with-readline         \
#             --mandir=/usr/share/man \
#             --infodir=/usr/share/info
# make
# echo "quit" | ./bc/bc -l Test/checklib.b
# make install
# popd
# rm -rf bc-1.07.1
# popd
#
#
# # 6.16. Binutils-2.32
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/binutils-2.32.tar.xz
# pushd  ${LFS_BUILD}/binutils-2.32
# mkdir -v build
# pushd build
# ../configure --prefix=/usr       \
#              --enable-gold       \
#              --enable-ld=default \
#              --enable-plugins    \
#              --enable-shared     \
#              --disable-werror    \
#              --enable-64-bit-bfd \
#              --with-system-zlib
# make tooldir=/usr
# make -k check
# make tooldir=/usr install
# popd
# popd
# rm -rf binutils-2.32
# popd
#
#
# # 6.17. GMP-6.1.2
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/gmp-6.1.2.tar.xz
# pushd  ${LFS_BUILD}/gmp-6.1.2
# ./configure --prefix=/usr    \
#             --enable-cxx     \
#             --disable-static \
#             --docdir=/usr/share/doc/gmp-6.1.2
# make
# make html
# make check 2>&1 | tee gmp-check-log
# awk '/# PASS:/{total+=$3} ; END{print total}' gmp-check-log
# make install
# make install-html
# popd
# rm -rf gmp-6.1.2
# popd
#
#
# # 6.18. MPFR-4.0.2
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/mpfr-4.0.2.tar.xz
# pushd  ${LFS_BUILD}/mpfr-4.0.2
# ./configure --prefix=/usr        \
#             --disable-static     \
#             --enable-thread-safe \
#             --docdir=/usr/share/doc/mpfr-4.0.2
# make
# make html
# make check
# make install
# make install-html
# popd
# rm -rf mpfr-4.0.2
# popd
#
#
# # 6.19. MPC-1.1.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/mpc-1.1.0.tar.gz
# pushd  ${LFS_BUILD}/mpc-1.1.0
# ./configure --prefix=/usr    \
#             --disable-static \
#             --docdir=/usr/share/doc/mpc-1.1.0
# make
# make html
# make check
# make install
# make install-html
# popd
# rm -rf mpc-1.1.0
# popd
#
#
# # 6.20. Shadow-4.6
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/shadow-4.6.tar.xz
# pushd  ${LFS_BUILD}/shadow-4.6
# sed -i 's/groups$(EXEEXT) //' src/Makefile.in
# find man -name Makefile.in -exec sed -i 's/groups\.1 / /'   {} \;
# find man -name Makefile.in -exec sed -i 's/getspnam\.3 / /' {} \;
# find man -name Makefile.in -exec sed -i 's/passwd\.5 / /'   {} \;
# sed -i -e 's@#ENCRYPT_METHOD DES@ENCRYPT_METHOD SHA512@' \
#        -e 's@/var/spool/mail@/var/mail@' etc/login.defs
# sed -i 's/1000/999/' etc/useradd
# ./configure --sysconfdir=/etc --with-group-name-max-length=32
# make
# make install
# mv -v /usr/bin/passwd /bin
# pwconv
# grpconv
# popd
# rm -rf shadow-4.6
# popd
#
#
# # 6.21. GCC-8.2.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/gcc-8.2.0.tar.xz
# pushd  ${LFS_BUILD}/gcc-8.2.0
# case $(uname -m) in
#   x86_64)
#     sed -e '/m64=/s/lib64/lib/' \
#         -i.orig gcc/config/i386/t-linux64
#   ;;
# esac
# rm -f /usr/lib/gcc
# mkdir -v build
# pushd build
# SED=sed                               \
# ../configure --prefix=/usr            \
#              --enable-languages=c,c++ \
#              --disable-multilib       \
#              --disable-bootstrap      \
#              --disable-libmpx         \
#              --with-system-zlib
# make
# ulimit -s 32768
# rm ../gcc/testsuite/g++.dg/pr83239.C
# chown -Rv nobody .
# su nobody -s /bin/bash -c "PATH=$PATH make -k check"
# cp ../contrib/test_summary /gcc_test_summary
# make install
# ln -sv ../usr/bin/cpp /lib
# ln -sv gcc /usr/bin/cc
# install -v -dm755 /usr/lib/bfd-plugins
# ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/8.2.0/liblto_plugin.so \
#         /usr/lib/bfd-plugins/
#
# echo "=============================================================================="
# echo "=============================================================================="
# echo "=============================================================================="
#
#
# echo 'int main(){}' > dummy.c
# cc dummy.c -v -Wl,--verbose &> dummy.log
# readelf -l a.out | grep ': /lib'
#
# grep -o '/usr/lib.*/crt[1in].*succeeded' dummy.log
#
# grep -B4 '^ /usr/include' dummy.log
#
# grep 'SEARCH.*/usr/lib' dummy.log |sed 's|; |\n|g'
#
# grep "/lib.*/libc.so.6 " dummy.log
#
# grep found dummy.log
#
# echo "=============================================================================="
# echo "=============================================================================="
# echo "=============================================================================="
#
# mkdir -pv /usr/share/gdb/auto-load/usr/lib
# mv -v /usr/lib/*gdb.py /usr/share/gdb/auto-load/usr/lib
#
# popd
# popd
# rm -rf gcc-8.2.0
# popd
#
#
# # 6.22. Bzip2-1.0.6
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/bzip2-1.0.6.tar.gz
# pushd  ${LFS_BUILD}/bzip2-1.0.6
# patch -Np1 -i /sources/8.4/bzip2-1.0.6-install_docs-1.patch
# sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile
# sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile
# make -f Makefile-libbz2_so
# make clean
# make
# make PREFIX=/usr install
# cp -v bzip2-shared /bin/bzip2
# cp -av libbz2.so* /lib
# ln -sv ../../lib/libbz2.so.1.0 /usr/lib/libbz2.so
# rm -v /usr/bin/{bunzip2,bzcat,bzip2}
# ln -sv bzip2 /bin/bunzip2
# ln -sv bzip2 /bin/bzcat
# popd
# rm -rf bzip2-1.0.6
# popd
#
#
# # 6.23. Pkg-config-0.29.2
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/pkg-config-0.29.2.tar.gz
# pushd  ${LFS_BUILD}/pkg-config-0.29.2
# ./configure --prefix=/usr              \
#             --with-internal-glib       \
#             --disable-host-tool        \
#             --docdir=/usr/share/doc/pkg-config-0.29.2
# make
# make check
# make install
# popd
# rm -rf pkg-config-0.29.2
# popd
#
#
# # 6.24. Ncurses-6.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/ncurses-6.1.tar.gz
# pushd  ${LFS_BUILD}/ncurses-6.1
# sed -i '/LIBTOOL_INSTALL/d' c++/Makefile.in
# ./configure --prefix=/usr           \
#             --mandir=/usr/share/man \
#             --with-shared           \
#             --without-debug         \
#             --without-normal        \
#             --enable-pc-files       \
#             --enable-widec
# make
# make install
# mv -v /usr/lib/libncursesw.so.6* /lib
# ln -sfv ../../lib/$(readlink /usr/lib/libncursesw.so) /usr/lib/libncursesw.so
#
# for lib in ncurses form panel menu ; do
#     rm -vf                    /usr/lib/lib${lib}.so
#     echo "INPUT(-l${lib}w)" > /usr/lib/lib${lib}.so
#     ln -sfv ${lib}w.pc        /usr/lib/pkgconfig/${lib}.pc
# done
#
# rm -vf                     /usr/lib/libcursesw.so
# echo "INPUT(-lncursesw)" > /usr/lib/libcursesw.so
# ln -sfv libncurses.so      /usr/lib/libcurses.so
#
# mkdir -v       /usr/share/doc/ncurses-6.1
# cp -v -R doc/* /usr/share/doc/ncurses-6.1
# popd
# rm -rf ncurses-6.1
# popd
#
#
# # 6.25. Attr-2.4.48
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/attr-2.4.48.tar.gz
# pushd  ${LFS_BUILD}/attr-2.4.48
# ./configure --prefix=/usr     \
#             --bindir=/bin     \
#             --disable-static  \
#             --sysconfdir=/etc \
#             --docdir=/usr/share/doc/attr-2.4.48
# make
# make check
# make install
# mv -v /usr/lib/libattr.so.* /lib
# ln -sfv ../../lib/$(readlink /usr/lib/libattr.so) /usr/lib/libattr.so
# popd
# rm -rf attr-2.4.48
# popd
#
#
# #  6.26. Acl-2.2.53
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/acl-2.2.53.tar.gz
# pushd  ${LFS_BUILD}/acl-2.2.53
# ./configure --prefix=/usr         \
#             --bindir=/bin         \
#             --disable-static      \
#             --libexecdir=/usr/lib \
#             --docdir=/usr/share/doc/acl-2.2.53
# make
# make install
# mv -v /usr/lib/libacl.so.* /lib
# ln -sfv ../../lib/$(readlink /usr/lib/libacl.so) /usr/lib/libacl.so
# popd
# rm -rf acl-2.2.53
# popd
#
#
# # 6.27. Libcap-2.26
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/libcap-2.26.tar.xz
# pushd  ${LFS_BUILD}/libcap-2.26
# sed -i '/install.*STALIBNAME/d' libcap/Makefile
# make
# make RAISE_SETFCAP=no lib=lib prefix=/usr install
# chmod -v 755 /usr/lib/libcap.so.2.26
# mv -v /usr/lib/libcap.so.* /lib
# ln -sfv ../../lib/$(readlink /usr/lib/libcap.so) /usr/lib/libcap.so
# popd
# rm -rf libcap-2.26
# popd
#
#
#
# # 6.28. Sed-4.7
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/sed-4.7.tar.xz
# pushd  ${LFS_BUILD}/sed-4.7
# sed -i 's/usr/tools/'                 build-aux/help2man
# sed -i 's/testsuite.panic-tests.sh//' Makefile.in
# ./configure --prefix=/usr --bindir=/bin
# make
# make html
# make check
# make install
# install -d -m755           /usr/share/doc/sed-4.7
# install -m644 doc/sed.html /usr/share/doc/sed-4.7
# popd
# rm -rf sed-4.7
# popd
#
#
#
# # 6.29. Psmisc-23.2
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/psmisc-23.2.tar.xz
# pushd  ${LFS_BUILD}/psmisc-23.2
# ./configure --prefix=/usr
# make
# make install
# mv -v /usr/bin/fuser   /bin
# mv -v /usr/bin/killall /bin
# popd
# rm -rf psmisc-23.2
# popd
#
#
#
# # 6.30. Iana-Etc-2.30
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/iana-etc-2.30.tar.bz2
# pushd  ${LFS_BUILD}/iana-etc-2.30
# make
# make install
# popd
# rm -rf iana-etc-2.30
# popd
#
#
# # 6.31. Bison-3.3.2
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/bison-3.3.2.tar.xz
# pushd  ${LFS_BUILD}/bison-3.3.2
# ./configure --prefix=/usr --docdir=/usr/share/doc/bison-3.3.2
# make
# make install
# popd
# rm -rf bison-3.3.2
# popd
#
# # 6.32. Flex-2.6.4
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/flex-2.6.4.tar.gz
# pushd  ${LFS_BUILD}/flex-2.6.4
# sed -i "/math.h/a #include <malloc.h>" src/flexdef.h
# HELP2MAN=/tools/bin/true \
# ./configure --prefix=/usr --docdir=/usr/share/doc/flex-2.6.4
# make
# make check
# make install
# popd
# rm -rf flex-2.6.4
# popd
#
# # 6.33. Grep-3.3
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/grep-3.3.tar.xz
# pushd  ${LFS_BUILD}/grep-3.3
# ./configure --prefix=/usr --bindir=/bin
# make
# make -k check
# make install
# popd
# rm -rf grep-3.3
# popd


# # 6.34. Bash-5.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/bash-5.0.tar.gz
# pushd  ${LFS_BUILD}/bash-5.0
# ./configure --prefix=/usr                    \
#             --docdir=/usr/share/doc/bash-5.0 \
#             --without-bash-malloc            \
#             --with-installed-readline
# make
# chown -Rv nobody .
# su nobody -s /bin/bash -c "PATH=$PATH HOME=/home make tests"
# make install
# mv -vf /usr/bin/bash /bin
# # TODO MAYBE PROBLEM HERE
# #exec /bin/bash --login +h
# popd
# rm -rf bash-5.0
# popd
#
#
# # 6.35. Libtool-2.4.6
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/libtool-2.4.6.tar.xz
# pushd  ${LFS_BUILD}/libtool-2.4.6
# ./configure --prefix=/usr
# make
# TESTSUITEFLAGS=-j7 make check
# make install
# popd
# rm -rf libtool-2.4.6
# popd
#
#
# # 6.36. GDBM-1.18.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/gdbm-1.18.1.tar.gz
# pushd  ${LFS_BUILD}/gdbm-1.18.1
# ./configure --prefix=/usr    \
#             --disable-static \
#             --enable-libgdbm-compat
# make
# make check
# make install
# popd
# rm -rf gdbm-1.18.1
# popd
#
#
# # 6.37. Gperf-3.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/gperf-3.1.tar.gz
# pushd  ${LFS_BUILD}/gperf-3.1
# ./configure --prefix=/usr --docdir=/usr/share/doc/gperf-3.1
# make
# make -j1 check
# make install
# popd
# rm -rf gperf-3.1
# popd
#
#
# # 6.38. Expat-2.2.6
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/expat-2.2.6.tar.bz2
# pushd  ${LFS_BUILD}/expat-2.2.6
# sed -i 's|usr/bin/env |bin/|' run.sh.in
# ./configure --prefix=/usr    \
#             --disable-static \
#             --docdir=/usr/share/doc/expat-2.2.6
# make
# make check
# make install
# install -v -m644 doc/*.{html,png,css} /usr/share/doc/expat-2.2.6
# popd
# rm -rf expat-2.2.6
# popd
#
#
# # 6.39. Inetutils-1.9.4
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/inetutils-1.9.4.tar.xz
# pushd  ${LFS_BUILD}/inetutils-1.9.4
# ./configure --prefix=/usr        \
#             --localstatedir=/var \
#             --disable-logger     \
#             --disable-whois      \
#             --disable-rcp        \
#             --disable-rexec      \
#             --disable-rlogin     \
#             --disable-rsh        \
#             --disable-servers
# make
# make check
# make install
# mv -v /usr/bin/{hostname,ping,ping6,traceroute} /bin
# mv -v /usr/bin/ifconfig /sbin
# popd
# rm -rf inetutils-1.9.4
# popd
#
#
# # 6.40. Perl-5.28.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/perl-5.28.1.tar.xz
# pushd  ${LFS_BUILD}/perl-5.28.1
# echo "127.0.0.1 localhost $(hostname)" > /etc/hosts
# export BUILD_ZLIB=False
# export BUILD_BZIP2=0
# sh Configure -des -Dprefix=/usr                 \
#                   -Dvendorprefix=/usr           \
#                   -Dman1dir=/usr/share/man/man1 \
#                   -Dman3dir=/usr/share/man/man3 \
#                   -Dpager="/usr/bin/less -isR"  \
#                   -Duseshrplib                  \
#                   -Dusethreads
# make
# make -k test
# make install
# unset BUILD_ZLIB BUILD_BZIP2
# popd
# rm -rf perl-5.28.1
# popd
#
#
# # 6.41. XML::Parser-2.44
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/XML-Parser-2.44.tar.gz
# pushd  ${LFS_BUILD}/XML-Parser-2.44
# perl Makefile.PL
# make
# make test
# make install
# popd
# rm -rf XML-Parser-2.44
# popd
#
#
# # 6.42. Intltool-0.51.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/intltool-0.51.0.tar.gz
# pushd  ${LFS_BUILD}/intltool-0.51.0
# sed -i 's:\\\${:\\\$\\{:' intltool-update.in
# ./configure --prefix=/usr
# make
# make check
# make install
# install -v -Dm644 doc/I18N-HOWTO /usr/share/doc/intltool-0.51.0/I18N-HOWTO
# popd
# rm -rf intltool-0.51.0
# popd
#
#
# # 6.43. Autoconf-2.69
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/autoconf-2.69.tar.xz
# pushd  ${LFS_BUILD}/autoconf-2.69
# sed '361 s/{/\\{/' -i bin/autoscan.in
# ./configure --prefix=/usr
# make
# make check
# make install
# popd
# rm -rf autoconf-2.69
# popd
#
#
# # 6.44. Automake-1.16.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/automake-1.16.1.tar.xz
# pushd  ${LFS_BUILD}/automake-1.16.1
# ./configure --prefix=/usr --docdir=/usr/share/doc/automake-1.16.1
# make
# make -j4 check
# make install
# popd
# rm -rf automake-1.16.1
# popd
#
#
# # 6.45. Xz-5.2.4
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/xz-5.2.4.tar.xz
# pushd  ${LFS_BUILD}/xz-5.2.4
# ./configure --prefix=/usr    \
#             --disable-static \
#             --docdir=/usr/share/doc/xz-5.2.4
# make
# make check
# make install
# mv -v   /usr/bin/{lzma,unlzma,lzcat,xz,unxz,xzcat} /bin
# mv -v /usr/lib/liblzma.so.* /lib
# ln -svf ../../lib/$(readlink /usr/lib/liblzma.so) /usr/lib/liblzma.so
# popd
# rm -rf xz-5.2.4
# popd
#
#
# #  6.46. Kmod-26
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/kmod-26.tar.xz
# pushd  ${LFS_BUILD}/kmod-26
# ./configure --prefix=/usr          \
#             --bindir=/bin          \
#             --sysconfdir=/etc      \
#             --with-rootlibdir=/lib \
#             --with-xz              \
#             --with-zlib
# make
# make install
#
# for target in depmod insmod lsmod modinfo modprobe rmmod; do
#   ln -sfv ../bin/kmod /sbin/$target
# done
#
# ln -sfv kmod /bin/lsmod
# popd
# rm -rf kmod-26
# popd
#
#
# #  6.47. Gettext-0.19.8.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/gettext-0.19.8.1.tar.xz
# pushd  ${LFS_BUILD}/gettext-0.19.8.1
# sed -i '/^TESTS =/d' gettext-runtime/tests/Makefile.in &&
# sed -i 's/test-lock..EXEEXT.//' gettext-tools/gnulib-tests/Makefile.in
# sed -e '/AppData/{N;N;p;s/\.appdata\./.metainfo./}' \
#     -i gettext-tools/its/appdata.loc
# ./configure --prefix=/usr    \
#             --disable-static \
#             --docdir=/usr/share/doc/gettext-0.19.8.1
# make
# make check
# make install
# chmod -v 0755 /usr/lib/preloadable_libintl.so
# popd
# rm -rf gettext-0.19.8.1
# popd
#
#
# # 6.48. Libelf from Elfutils-0.176
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/elfutils-0.176.tar.bz2
# pushd  ${LFS_BUILD}/elfutils-0.176
# ./configure --prefix=/usr
# make
# make check
# make -C libelf install
# install -vm644 config/libelf.pc /usr/lib/pkgconfig
# popd
# rm -rf elfutils-0.176
# popd
#
#
# # 6.49. Libffi-3.2.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/libffi-3.2.1.tar.gz
# pushd  ${LFS_BUILD}/libffi-3.2.1
# sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' \
#     -i include/Makefile.in
#
# sed -e '/^includedir/ s/=.*$/=@includedir@/' \
#     -e 's/^Cflags: -I${includedir}/Cflags:/' \
#     -i libffi.pc.in
# ./configure --prefix=/usr --disable-static --with-gcc-arch=native
# make
# make check
# make install
# popd
# rm -rf libffi-3.2.1
# popd
#
#
# #  6.50. OpenSSL-1.1.1a
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/openssl-1.1.1a.tar.gz
# pushd  ${LFS_BUILD}/openssl-1.1.1a
# ./config --prefix=/usr         \
#          --openssldir=/etc/ssl \
#          --libdir=lib          \
#          shared                \
#          zlib-dynamic
# make
# make test
# sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile
# make MANSUFFIX=ssl install
# mv -v /usr/share/doc/openssl /usr/share/doc/openssl-1.1.1a
# cp -vfr doc/* /usr/share/doc/openssl-1.1.1a
# popd
# rm -rf openssl-1.1.1a
# popd
#
#
# #  6.51. Python-3.7.2
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/Python-3.7.2.tar.xz
# pushd  ${LFS_BUILD}/Python-3.7.2
# ./configure --prefix=/usr       \
#          --enable-shared     \
#          --with-system-expat \
#          --with-system-ffi   \
#          --with-ensurepip=yes
# make
# make install
# chmod -v 755 /usr/lib/libpython3.7m.so
# chmod -v 755 /usr/lib/libpython3.so
# popd
# rm -rf Python-3.7.2
# popd
#
#
# # 6.52. Ninja-1.9.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/ninja-1.9.0.tar.gz
# pushd  ${LFS_BUILD}/ninja-1.9.0
# export NINJAJOBS=4
# sed -i '/int Guess/a \
#   int   j = 0;\
#   char* jobs = getenv( "NINJAJOBS" );\
#   if ( jobs != NULL ) j = atoi( jobs );\
#   if ( j > 0 ) return j;\
# ' src/ninja.cc
# python3 configure.py --bootstrap
# python3 configure.py
# ./ninja ninja_test
# ./ninja_test --gtest_filter=-SubprocessTest.SetWithLots
# install -vm755 ninja /usr/bin/
# install -vDm644 misc/bash-completion /usr/share/bash-completion/completions/ninja
# install -vDm644 misc/zsh-completion  /usr/share/zsh/site-functions/_ninja
# popd
# rm -rf ninja-1.9.0
# popd
#
#
# # 6.53. Meson-0.49.2
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/meson-0.49.2.tar.gz
# pushd  ${LFS_BUILD}/meson-0.49.2
# python3 setup.py build
# python3 setup.py install --root=dest
# cp -rv dest/* /
# popd
# rm -rf meson-0.49.2
# popd
#
#
# # 6.54. Coreutils-8.30
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/coreutils-8.30.tar.xz
# pushd  ${LFS_BUILD}/coreutils-8.30
# patch -Np1 -i /sources/8.4/coreutils-8.30-i18n-1.patch
# sed -i '/test.lock/s/^/#/' gnulib-tests/gnulib.mk
# autoreconf -fiv
# FORCE_UNSAFE_CONFIGURE=1 ./configure \
#             --prefix=/usr            \
#             --enable-no-install-program=kill,uptime
# FORCE_UNSAFE_CONFIGURE=1 make
# make NON_ROOT_USERNAME=nobody check-root
# echo "dummy:x:1000:nobody" >> /etc/group
# chown -Rv nobody .
# su nobody -s /bin/bash \
#           -c "PATH=$PATH make RUN_EXPENSIVE_TESTS=yes check"
# sed -i '/dummy/d' /etc/group
# make install
# mv -v /usr/bin/{cat,chgrp,chmod,chown,cp,date,dd,df,echo} /bin
# mv -v /usr/bin/{false,ln,ls,mkdir,mknod,mv,pwd,rm} /bin
# mv -v /usr/bin/{rmdir,stty,sync,true,uname} /bin
# mv -v /usr/bin/chroot /usr/sbin
# mv -v /usr/share/man/man1/chroot.1 /usr/share/man/man8/chroot.8
# sed -i s/\"1\"/\"8\"/1 /usr/share/man/man8/chroot.8
# mv -v /usr/bin/{head,nice,sleep,touch} /bin
# popd
# rm -rf coreutils-8.30
# popd
#
#
# #  6.55. Check-0.12.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/check-0.12.0.tar.gz
# pushd  ${LFS_BUILD}/check-0.12.0
# ./configure --prefix=/usr
# make
# make check
# make install
# sed -i '1 s/tools/usr/' /usr/bin/checkmk
# popd
# rm -rf check-0.12.0
# popd
#
#
# #  6.56. Diffutils-3.7
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/diffutils-3.7.tar.xz
# pushd  ${LFS_BUILD}/diffutils-3.7
# ./configure --prefix=/usr
# make
# make check
# make install
# popd
# rm -rf diffutils-3.7
# popd
#
#
# # 6.57. Gawk-4.2.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/gawk-4.2.1.tar.xz
# pushd  ${LFS_BUILD}/gawk-4.2.1
# sed -i 's/extras//' Makefile.in
# ./configure --prefix=/usr
# make
# make check
# make install
# popd
# rm -rf gawk-4.2.1
# popd
#
#
# #  6.58. Findutils-4.6.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/findutils-4.6.0.tar.gz
# pushd  ${LFS_BUILD}/findutils-4.6.0
# sed -i 's/test-lock..EXEEXT.//' tests/Makefile.in
# sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' gl/lib/*.c
# sed -i '/unistd/a #include <sys/sysmacros.h>' gl/lib/mountlist.c
# echo "#define _IO_IN_BACKUP 0x100" >> gl/lib/stdio-impl.h
# ./configure --prefix=/usr --localstatedir=/var/lib/locate
# make
# make check
# make install
# mv -v /usr/bin/find /bin
# sed -i 's|find:=${BINDIR}|find:=/bin|' /usr/bin/updatedb
# popd
# rm -rf findutils-4.6.0
# popd
#
#
# # 6.59. Groff-1.22.4
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/groff-1.22.4.tar.gz
# pushd  ${LFS_BUILD}/groff-1.22.4
# PAGE=letter ./configure --prefix=/usr
# make -j1
# make install
# popd
# rm -rf groff-1.22.4
# popd
#
#
# #  6.60. GRUB-2.02
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/grub-2.02.tar.xz
# pushd  ${LFS_BUILD}/grub-2.02
# ./configure --prefix=/usr          \
#             --sbindir=/sbin        \
#             --sysconfdir=/etc      \
#             --disable-efiemu       \
#             --disable-werror
# make
# make install
# mv -v /etc/bash_completion.d/grub /usr/share/bash-completion/completions
# popd
# rm -rf grub-2.02
# popd
#
#
# #  6.61. Less-530
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/less-530.tar.gz
# pushd  ${LFS_BUILD}/less-530
# ./configure --prefix=/usr --sysconfdir=/etc
# make
# make install
# popd
# rm -rf less-530
# popd
#
#
# #  6.62. Gzip-1.10
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/gzip-1.10.tar.xz
# pushd  ${LFS_BUILD}/gzip-1.10
# ./configure --prefix=/usr
# make
# make check
# make install
# mv -v /usr/bin/gzip /bin
# popd
# rm -rf gzip-1.10
# popd
#
#
# #  6.63. IPRoute2-4.20.0
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/iproute2-4.20.0.tar.xz
# pushd  ${LFS_BUILD}/iproute2-4.20.0
# sed -i /ARPD/d Makefile
# rm -fv man/man8/arpd.8
# sed -i 's/.m_ipt.o//' tc/Makefile
# make
# make DOCDIR=/usr/share/doc/iproute2-4.20.0 install
# popd
# rm -rf iproute2-4.20.0
# popd
#
# #  6.64. Kbd-2.0.4
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/kbd-2.0.4.tar.xz
# pushd  ${LFS_BUILD}/kbd-2.0.4
# patch -Np1 -i /sources/8.4/kbd-2.0.4-backspace-1.patch
# sed -i 's/\(RESIZECONS_PROGS=\)yes/\1no/g' configure
# sed -i 's/resizecons.8 //' docs/man/man8/Makefile.in
# PKG_CONFIG_PATH=/tools/lib/pkgconfig ./configure --prefix=/usr --disable-vlock
# make
# make check
# make install
# mkdir -v /usr/share/doc/kbd-2.0.4
# cp -R -v docs/doc/* /usr/share/doc/kbd-2.0.4
# popd
# rm -rf kbd-2.0.4
# popd
#
#
# # 6.65. Libpipeline-1.5.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/libpipeline-1.5.1.tar.gz
# pushd  ${LFS_BUILD}/libpipeline-1.5.1
# ./configure --prefix=/usr
# make
# make check
# make install
# popd
# rm -rf libpipeline-1.5.1
# popd
#
#
# # 6.66. Make-4.2.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/make-4.2.1.tar.bz2
# pushd  ${LFS_BUILD}/make-4.2.1
# sed -i '211,217 d; 219,229 d; 232 d' glob/glob.c
# ./configure --prefix=/usr
# make
# make PERL5LIB=$PWD/tests/ check
# make install
# popd
# rm -rf make-4.2.1
# popd
#
#
# # 6.67. Patch-2.7.6
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/patch-2.7.6.tar.xz
# pushd  ${LFS_BUILD}/patch-2.7.6
# ./configure --prefix=/usr
# make
# make check
# make install
# popd
# rm -rf patch-2.7.6
# popd
#
#
# # 6.68. Man-DB-2.8.5
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/man-db-2.8.5.tar.xz
# pushd  ${LFS_BUILD}/man-db-2.8.5
# ./configure --prefix=/usr                        \
#             --docdir=/usr/share/doc/man-db-2.8.5 \
#             --sysconfdir=/etc                    \
#             --disable-setuid                     \
#             --enable-cache-owner=bin             \
#             --with-browser=/usr/bin/lynx         \
#             --with-vgrind=/usr/bin/vgrind        \
#             --with-grap=/usr/bin/grap            \
#             --with-systemdtmpfilesdir=           \
#             --with-systemdsystemunitdir=
# make
# make check
# make install
# popd
# rm -rf man-db-2.8.5
# popd
#
#
# # 6.69. Tar-1.31
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/tar-1.31.tar.xz
# pushd  ${LFS_BUILD}/tar-1.31
# sed -i 's/abort.*/FALLTHROUGH;/' src/extract.c
# FORCE_UNSAFE_CONFIGURE=1  \
# ./configure --prefix=/usr \
#             --bindir=/bin
# make
# make check
# make install
# make -C doc install-html docdir=/usr/share/doc/tar-1.31
# popd
# rm -rf tar-1.31
# popd
#
#
# # 6.70. Texinfo-6.5
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/texinfo-6.5.tar.xz
# pushd  ${LFS_BUILD}/texinfo-6.5
# sed -i '5481,5485 s/({/(\\{/' tp/Texinfo/Parser.pm
# ./configure --prefix=/usr --disable-static
# make
# make check
# make install
# make TEXMF=/usr/share/texmf install-tex
# popd
# rm -rf texinfo-6.5
# popd
#
#
# #  6.71. Vim-8.1
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/vim-8.1.tar.bz2
# pushd ${LFS_BUILD}/vim81
# echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h
# ./configure --prefix=/usr
# make
# LANG=en_US.UTF-8 make -j1 test &> vim-test.log
# make install
# ln -sv vim /usr/bin/vi
# for L in  /usr/share/man/{,*/}man1/vim.1; do
#     ln -sv vim.1 $(dirname $L)/vi.1
# done
# ln -sv ../vim/vim81/doc /usr/share/doc/vim-8.1
# cat > /etc/vimrc << "EOF"
# " Begin /etc/vimrc
#
# " Ensure defaults are set before customizing settings, not after
# source $VIMRUNTIME/defaults.vim
# let skip_defaults_vim=1
#
# set nocompatible
# set backspace=2
# set mouse=
# syntax on
# if (&term == "xterm") || (&term == "putty")
#   set background=dark
# endif
#
# " End /etc/vimrc
# EOF
# popd
# rm -rf vim81
# popd
#
# 
# # 6.72. Procps-ng-3.3.15
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/procps-ng-3.3.15.tar.xz
# pushd  ${LFS_BUILD}/procps-ng-3.3.15
# ./configure --prefix=/usr                            \
#             --exec-prefix=                           \
#             --libdir=/usr/lib                        \
#             --docdir=/usr/share/doc/procps-ng-3.3.15 \
#             --disable-static                         \
#             --disable-kill
# make
# sed -i -r 's|(pmap_initname)\\\$|\1|' testsuite/pmap.test/pmap.exp
# sed -i '/set tty/d' testsuite/pkill.test/pkill.exp
# rm testsuite/pgrep.test/pgrep.exp
# make check
# make install
# mv -v /usr/lib/libprocps.so.* /lib
# ln -sfv ../../lib/$(readlink /usr/lib/libprocps.so) /usr/lib/libprocps.so
# popd
# rm -rf procps-ng-3.3.15
# popd
#
#
# # 6.73. Util-linux-2.33.1 TODO RUN TESTS
# pushd ${LFS_BUILD}
# tar xf ${LFS_SOURCES}/util-linux-2.33.1.tar.xz
# pushd  ${LFS_BUILD}/util-linux-2.33.1
# mkdir -pv /var/lib/hwclock
# rm -vf /usr/include/{blkid,libmount,uuid}
# ./configure ADJTIME_PATH=/var/lib/hwclock/adjtime   \
#             --docdir=/usr/share/doc/util-linux-2.33.1 \
#             --disable-chfn-chsh  \
#             --disable-login      \
#             --disable-nologin    \
#             --disable-su         \
#             --disable-setpriv    \
#             --disable-runuser    \
#             --disable-pylibmount \
#             --disable-static     \
#             --without-python     \
#             --without-systemd    \
#             --without-systemdsystemunitdir
# make
# make install
# popd
# rm -rf util-linux-2.33.1
# popd


# 6.74. E2fsprogs-1.44.5 
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/e2fsprogs-1.44.5.tar.gz
pushd  ${LFS_BUILD}/e2fsprogs-1.44.5
mkdir -v build
pushd build
../configure --prefix=/usr           \
             --bindir=/bin           \
             --with-root-prefix=""   \
             --enable-elf-shlibs     \
             --disable-libblkid      \
             --disable-libuuid       \
             --disable-uuidd         \
             --disable-fsck
make
make check
make install
make install-libs
chmod -v u+w /usr/lib/{libcom_err,libe2p,libext2fs,libss}.a
gunzip -v /usr/share/info/libext2fs.info.gz
install-info --dir-file=/usr/share/info/dir /usr/share/info/libext2fs.info
makeinfo -o      doc/com_err.info ../lib/et/com_err.texinfo
install -v -m644 doc/com_err.info /usr/share/info
install-info --dir-file=/usr/share/info/dir /usr/share/info/com_err.info
popd
popd
rm -rf e2fsprogs-1.44.5
popd


# 6.75. Sysklogd-1.5.1 
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/sysklogd-1.5.1.tar.gz
pushd  ${LFS_BUILD}/sysklogd-1.5.1
sed -i '/Error loading kernel symbols/{n;n;d}' ksym_mod.c
sed -i 's/union wait/int/' syslogd.c
make
make BINDIR=/sbin install
cat > /etc/syslog.conf << "EOF"
# Begin /etc/syslog.conf

auth,authpriv.* -/var/log/auth.log
*.*;auth,authpriv.none -/var/log/sys.log
daemon.* -/var/log/daemon.log
kern.* -/var/log/kern.log
mail.* -/var/log/mail.log
user.* -/var/log/user.log
*.emerg *

# End /etc/syslog.conf
EOF
popd
rm -rf sysklogd-1.5.1
popd


# 6.76. Sysvinit-2.93 
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/sysvinit-2.93.tar.xz
pushd  ${LFS_BUILD}/sysvinit-2.93
patch -Np1 -i /sources/8.4/sysvinit-2.93-consolidated-1.patc
make
make install
popd
rm -rf sysvinit-2.93
popd


#  6.77. Eudev-3.2.7 
pushd ${LFS_BUILD}
tar xf ${LFS_SOURCES}/eudev-3.2.7.tar.gz
pushd  ${LFS_BUILD}/eudev-3.2.7
cat > config.cache << "EOF"
HAVE_BLKID=1
BLKID_LIBS="-lblkid"
BLKID_CFLAGS="-I/tools/include"
EOF
./configure --prefix=/usr           \
            --bindir=/sbin          \
            --sbindir=/sbin         \
            --libdir=/usr/lib       \
            --sysconfdir=/etc       \
            --libexecdir=/lib       \
            --with-rootprefix=      \
            --with-rootlibdir=/lib  \
            --enable-manpages       \
            --disable-static        \
            --config-cache
LIBRARY_PATH=/tools/lib make
mkdir -pv /lib/udev/rules.d
mkdir -pv /etc/udev/rules.d
make LD_LIBRARY_PATH=/tools/lib check
make LD_LIBRARY_PATH=/tools/lib install
tar -xvf ${LFS_SOURCES}/udev-lfs-20171102.tar.bz2
make -f udev-lfs-20171102/Makefile.lfs install
LD_LIBRARY_PATH=/tools/lib udevadm hwdb --update
popd
rm -rf eudev-3.2.7
popd



