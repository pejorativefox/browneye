Name:       binutils
Version:    2.41
Release:    1
Summary:    GNU binutils
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr
Patch0:     binutils-libtool-lib64.patch 
%description
TODO

%prep
%setup -q
%patch -p1

%build
mkdir build
pushd build
../configure --prefix=/usr       \
             --sysconfdir=/etc   \
             --enable-gold       \
             --enable-ld=default \
             --enable-plugins    \
             --enable-shared     \
             --disable-werror    \
             --enable-64-bit-bfd \
             --with-system-zlib  \
             --libdir=%{_libdir}
%make_build tooldir=/usr
popd

%install
pushd build
rm -rf %{buildroot}
%make_install tooldir=/usr
rm -vf %{buildroot}%{_infodir}/dir*
rm -fv %{buildroot}/usr/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a
popd

%files -f ../../SOURCES/binutils.filelist

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 2.41
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.32
- Initial RPM
