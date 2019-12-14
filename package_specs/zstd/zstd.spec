Name:       zstd
Version:    1.4.4
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
pushd build/cmake
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
%make_build
popd

%install
rm -rf %{buildroot}
pushd build/cmake
%make_install
popd

%files
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt
/usr/include/cover.h
/usr/include/zbuff.h
/usr/include/zdict.h
/usr/include/zstd.h
/usr/include/zstd_errors.h
/usr/lib64/libzstd.a
/usr/lib64/libzstd.so
/usr/lib64/libzstd.so.1
/usr/lib64/libzstd.so.1.4.4
/usr/lib64/pkgconfig/libzstd.pc
/usr/share/man/man1/unzstd.1.gz
/usr/share/man/man1/zstd.1.gz
/usr/share/man/man1/zstdcat.1.gz
/usr/share/man/man1/zstdgrep.1.gz
/usr/share/man/man1/zstdless.1.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.4.4
- Initial RPM

