Name:       zstd
Version:    1.5.5
Release:    1
Summary:    Fast real-time compression algorith
License:    BSD
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Fast real-time compression algorith

%prep
%setup

%build
make prefix=/usr

%install
rm -rf %{buildroot}
make prefix=%{buildroot}/usr/ install
rm -v %{buildroot}/usr/lib/libzstd.a

%files
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt
/usr/include/zdict.h
/usr/include/zstd.h
/usr/include/zstd_errors.h
/usr/lib/libzstd.so
/usr/lib/libzstd.so.1
/usr/lib/libzstd.so.1.5.5
/usr/lib/pkgconfig/libzstd.pc
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 1.5.5
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.4.4
- Initial RPM

