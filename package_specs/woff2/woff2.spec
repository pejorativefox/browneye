Name:       woff2
Version:    1.0.2
Release:    1
Summary:    Font format library
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The primary purpose of the WOFF2 format is to efficiently package fonts linked to Web documents by means of CSS

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
/usr/include/woff2/decode.h
/usr/include/woff2/encode.h
/usr/include/woff2/output.h
/usr/lib64/libwoff2common.so
/usr/lib64/libwoff2common.so.1.0.2
/usr/lib64/libwoff2dec.so
/usr/lib64/libwoff2dec.so.1.0.2
/usr/lib64/libwoff2enc.so
/usr/lib64/libwoff2enc.so.1.0.2
/usr/lib64/pkgconfig/libwoff2common.pc
/usr/lib64/pkgconfig/libwoff2dec.pc
/usr/lib64/pkgconfig/libwoff2enc.pc

%changelog
* Wed Sep 09 2020 Chris Statzer <chris.statzer@qq.com> 1.0.2
- Initial RPM

