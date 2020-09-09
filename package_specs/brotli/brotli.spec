Name:       brotli
Version:    1.0.9
Release:    1
Summary:    Brotli compression format 
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Brotli compression format 

%prep
%setup

%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/bin/brotli
/usr/include/brotli/decode.h
/usr/include/brotli/encode.h
/usr/include/brotli/port.h
/usr/include/brotli/types.h
/usr/lib64/libbrotlicommon-static.a
/usr/lib64/libbrotlicommon.so
/usr/lib64/libbrotlicommon.so.1
/usr/lib64/libbrotlicommon.so.1.0.9
/usr/lib64/libbrotlidec-static.a
/usr/lib64/libbrotlidec.so
/usr/lib64/libbrotlidec.so.1
/usr/lib64/libbrotlidec.so.1.0.9
/usr/lib64/libbrotlienc-static.a
/usr/lib64/libbrotlienc.so
/usr/lib64/libbrotlienc.so.1
/usr/lib64/libbrotlienc.so.1.0.9
/usr/lib64/pkgconfig/libbrotlicommon.pc
/usr/lib64/pkgconfig/libbrotlidec.pc
/usr/lib64/pkgconfig/libbrotlienc.pc

%changelog
* Wed Sep 09 2020 Chris Statzer <chris.statzer@qq.com> 1.0.9
- Initial RPM

