Name:       nss
Version:    3.92
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

BuildRequires: nspr

%description
TODO

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/nss-3.92-standalone-1.patch
pushd nss
%make_build BUILD_OPT=1                  \
  NSPR_INCLUDE_DIR=/usr/include/nspr  \
  USE_SYSTEM_ZLIB=1                   \
  ZLIB_LIBS=-lz                       \
  NSS_ENABLE_WERROR=0                 \
  $([ $(uname -m) = x86_64 ] && echo USE_64=1) \
  $([ -f /usr/include/sqlite3.h ] && echo NSS_USE_SYSTEM_SQLITE=1)
popd

%install    
rm -rf %{buildroot}

pushd dist
mkdir -pv %{buildroot}/usr/lib
mkdir -pv %{buildroot}/usr/include/nss
mkdir -pv %{buildroot}/usr/bin
mkdir -pv %{buildroot}/usr/lib/pkgconfig

install -v -m755 Linux*/lib/*.so              %{buildroot}/usr/lib
install -v -m644 Linux*/lib/{*.chk,libcrmf.a} %{buildroot}/usr/lib

install -v -m755 -d                           %{buildroot}/usr/include/nss
cp -v -RL {public,private}/nss/*              %{buildroot}/usr/include/nss
chmod -v 644                                  %{buildroot}/usr/include/nss/*

install -v -m755 Linux*/bin/{certutil,nss-config,pk12util} %{buildroot}/usr/bin

install -v -m644 Linux*/lib/pkgconfig/nss.pc  %{buildroot}/usr/lib/pkgconfig

rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/certutil
/usr/bin/nss-config
/usr/bin/pk12util
/usr/include/nss/*
/usr/lib/libcrmf.a
/usr/lib/libfreebl3.chk
/usr/lib/libfreebl3.so
/usr/lib/libfreeblpriv3.chk
/usr/lib/libfreeblpriv3.so
/usr/lib/libnss3.so
/usr/lib/libnssckbi.so
/usr/lib/libnssdbm3.chk
/usr/lib/libnssdbm3.so
/usr/lib/libnsssysinit.so
/usr/lib/libnssutil3.so
/usr/lib/libsmime3.so
/usr/lib/libsoftokn3.chk
/usr/lib/libsoftokn3.so
/usr/lib/libssl3.so
/usr/lib/pkgconfig/nss.pc
/usr/lib/libnssckbi-testlib.so
/usr/lib/libpkcs11testmodule.so

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 3.92-1
- Version bump
