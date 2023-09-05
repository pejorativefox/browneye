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

echo "MULTILIB_OSDIRNAMES = m64=../lib64" >> gcc/config/i386/t-linux64

pushd build
../configure --prefix=/usr            \
             LD=ld                    \
             --enable-languages=c,c++ \
             --enable-default-pie     \
             --enable-default-ssp     \
             --disable-multilib       \
             --disable-bootstrap      \
             --disable-fixincludes    \
             --with-system-zlib       \
             --libdir=%{_libdir}
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
/usr/lib64/libstdc++.a
/usr/lib64/libstdc++.so
/usr/lib64/libstdc++.so.6
/usr/lib64/libstdc++.so.6.0.32
/usr/lib64/libstdc++.so.6.0.32-gdb.py
/usr/lib64/libstdc++fs.a
/usr/lib64/libstdc++exp.a
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
/usr/lib64/libgcc_s.so
/usr/lib64/libgcc_s.so.1

%files -f ../../SOURCES/gcc.filelist

%changelog
* Sun Sep 3 2023 Chris Statzer <chris.statzer@gmail.com> 13.2.0
- Version bump

* Thu May 15 2020 Chris Statzer <chris.statzer@qq.com> 8.2.0-3
- Cleaned up spec file and added libgcc, libstdc++ subpackages to clean up the deps of many packages.
