Name:       gcc
Version:    13.2.0
Release:    2
Summary:    The GNU Compiler Collection
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr


%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages


%prep
%setup -q


%build
case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
  ;;
esac

mkdir -v build
pushd build
../configure --prefix=/usr            \
             LD=ld                    \
             --enable-languages=c,c++ \
             --enable-default-pie     \
             --enable-default-ssp     \
             --disable-multilib       \
             --disable-bootstrap      \
             --disable-fixincludes    \
             --with-system-zlib
%make_build
popd


%install
rm -rf %{buildroot}
pushd build
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*
ln -sfv gcc %{buildroot}/usr/bin/cc


%package -n libstdc++
Summary: The GNU Standard C++ Library v3
%description -n libstdc++
The GNU Standard C++ Library v3 is an ongoing project to implement the ISO 14882 C++ Standard Library as described in clauses 20 through 33 and annex D (prior to the 2017 standard the library clauses started with 17).

%files -n libstdc++
/usr/lib/libstdc++.a
/usr/lib/libstdc++.so
/usr/lib/libstdc++.so.6
/usr/lib/libstdc++.so.6.0.32
/usr/lib/libstdc++.so.6.0.32-gdb.py
/usr/lib/libstdc++fs.a
/usr/share/gcc-13.2.0/python/libstdcxx/__init__.py
/usr/share/gcc-13.2.0/python/libstdcxx/v6/__init__.py
/usr/share/gcc-13.2.0/python/libstdcxx/v6/printers.py
/usr/share/gcc-13.2.0/python/libstdcxx/v6/xmethods.py

%package -n libgcc
Summary: GCC low-level runtime library
Provides: libgcc_s.so.1()(64bit), libgcc_s.so.1(GCC_3.0)(64bit), libgcc_s.so.1(GCC_3.3)(64bit), libgcc_s.so.1(GCC_4.2.0)(64bit), libgcc_s.so.1(GCC_3.4)(64bit), libgcc_s.so.1(GCC_3.3.1)(64bit), libgcc_s.so.1(GCC_4.7.0)(64bit)
%description -n libgcc
The GCC low-level runtime library

%files -n libgcc
/usr/lib/libgcc_s.so
/usr/lib/libgcc_s.so.1

%files
/usr/bin/c++
/usr/bin/cpp
/usr/bin/g++
/usr/bin/cc
/usr/bin/gcc
/usr/bin/gcc-ar
/usr/bin/gcc-nm
/usr/bin/gcc-ranlib
/usr/bin/gcov
/usr/bin/gcov-dump
/usr/bin/gcov-tool
/usr/bin/x86_64-pc-linux-gnu-c++
/usr/bin/x86_64-pc-linux-gnu-g++
/usr/bin/x86_64-pc-linux-gnu-gcc
/usr/bin/x86_64-pc-linux-gnu-gcc-%{version}
/usr/bin/x86_64-pc-linux-gnu-gcc-ar
/usr/bin/x86_64-pc-linux-gnu-gcc-nm
/usr/bin/x86_64-pc-linux-gnu-gcc-ranlib
/usr/bin/lto-dump
/usr/lib/libasan.a
/usr/lib/libasan.so
/usr/lib/libasan.so.8
/usr/lib/libasan.so.8.0.0
/usr/lib/libhwasan.a
/usr/lib/libhwasan.so
/usr/lib/libhwasan.so.0
/usr/lib/libhwasan.so.0.0.0
/usr/lib/libhwasan_preinit.o
/usr/lib/libstdc++exp.a
/usr/lib/libtsan.so.2
/usr/lib/libtsan.so.2.0.0
/usr/include/c++/%{version}/*
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/*
/usr/lib/libasan_preinit.o
/usr/lib/libatomic.a
/usr/lib/libatomic.so
/usr/lib/libatomic.so.1
/usr/lib/libatomic.so.1.2.0
/usr/lib/libcc1.so
/usr/lib/libcc1.so.0
/usr/lib/libcc1.so.0.0.0
/usr/lib/libgomp.a
/usr/lib/libgomp.so
/usr/lib/libgomp.so.1
/usr/lib/libgomp.so.1.0.0
/usr/lib/libgomp.spec
/usr/lib/libitm.a
/usr/lib/libitm.so
/usr/lib/libitm.so.1
/usr/lib/libitm.so.1.0.0
/usr/lib/libitm.spec
/usr/lib/liblsan.a
/usr/lib/liblsan.so
/usr/lib/liblsan.so.0
/usr/lib/liblsan.so.0.0.0
/usr/lib/liblsan_preinit.o
/usr/lib/libquadmath.a
/usr/lib/libquadmath.so
/usr/lib/libquadmath.so.0
/usr/lib/libquadmath.so.0.0.0
/usr/lib/libsanitizer.spec
/usr/lib/libssp.a
/usr/lib/libssp.so
/usr/lib/libssp.so.0
/usr/lib/libssp.so.0.0.0
/usr/lib/libssp_nonshared.a
/usr/lib/libsupc++.a
/usr/lib/libtsan.a
/usr/lib/libtsan.so
/usr/lib/libtsan_preinit.o
/usr/lib/libubsan.a
/usr/lib/libubsan.so
/usr/lib/libubsan.so.1
/usr/lib/libubsan.so.1.0.0
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/*
/usr/share/info/*
/usr/share/locale/*
/usr/share/man/*


%changelog
* Sun Sep 3 2023 Chris Statzer <chris.statzer@gmail.com> 13.2.0
- Version bump

* Thu May 15 2020 Chris Statzer <chris.statzer@qq.com> 8.2.0-3
- Cleaned up spec file and added libgcc, libstdc++ subpackages to clean up the deps of many packages.
