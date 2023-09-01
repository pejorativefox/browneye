Name:       binutils
Version:    2.41
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
/usr/bin/
/usr/include/
/usr/lib/
/usr/share/
/usr/etc/gprofng.rc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.32
- Initial RPM
