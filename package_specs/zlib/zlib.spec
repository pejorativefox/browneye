Name:       zlib
Version:    1.2.13
Release:    1
Summary:    zlib compression library
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The zlib compression library.

%prep
%setup -q -a0

%build
./configure --prefix=/usr
%make_build
rm -fv /usr/lib/libz.a

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/zconf.h
/usr/include/zlib.h
/usr/lib/libz.a
/usr/lib/libz.so
/usr/lib/libz.so.1
/usr/lib/libz.so.1.2.13
/usr/lib/pkgconfig/zlib.pc
/usr/share/man/man3/zlib.3.gz


%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.2.13
- Version bump
