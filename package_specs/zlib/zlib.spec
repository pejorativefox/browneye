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
./configure --prefix=/usr --libdir=%{_libdir}
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -fv %{buildroot}/usr/lib64/libz.a

%files
/usr/include/zconf.h
/usr/include/zlib.h
/usr/lib64/libz.so
/usr/lib64/libz.so.1
/usr/lib64/libz.so.1.2.13
/usr/lib64/pkgconfig/zlib.pc
/usr/share/man/man3/zlib.3.gz


%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.2.13
- Version bump
