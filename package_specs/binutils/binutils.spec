Name:       binutils
Version:    2.32
Release:    1
Summary:    GNU binutils
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup

%build
mkdir build
pushd build
../configure --prefix=/usr --enable-gold --enable-ld=default    \
             --enable-plugins --enable-shared  --disable-werror \
             --enable-64-bit-bfd --with-system-zlib
%make_build tooldir=/usr
popd

%install
pushd build
rm -rf %{buildroot}
%make_install tooldir=/usr
rm -vf %{buildroot}%{_infodir}/dir*
popd

%files
/usr/bin/addr2line
/usr/bin/ar
/usr/bin/as
/usr/bin/c++filt
/usr/bin/dwp
/usr/bin/elfedit
/usr/bin/gprof
/usr/bin/ld
/usr/bin/ld.bfd
/usr/bin/ld.gold
/usr/bin/nm
/usr/bin/objcopy
/usr/bin/objdump
/usr/bin/ranlib
/usr/bin/readelf
/usr/bin/size
/usr/bin/strings
/usr/bin/strip
/usr/include/ansidecl.h
/usr/include/bfd.h
/usr/include/bfd_stdint.h
/usr/include/bfdlink.h
/usr/include/diagnostics.h
/usr/include/dis-asm.h
/usr/include/plugin-api.h
/usr/include/symcat.h
/usr/lib/ldscripts/*
/usr/lib/libbfd-2.32.so
/usr/lib/libbfd.a
/usr/lib/libbfd.la
/usr/lib/libbfd.so
/usr/lib/libopcodes-2.32.so
/usr/lib/libopcodes.a
/usr/lib/libopcodes.la
/usr/lib/libopcodes.so
/usr/share/info/as.info.gz
/usr/share/info/bfd.info.gz
/usr/share/info/binutils.info.gz
/usr/share/info/gprof.info.gz
/usr/share/info/ld.info.gz
/usr/share/locale/*
/usr/share/man/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.32
- Initial RPM
