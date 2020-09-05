Name:       webp
Version:    1.1.0
Release:    1
Summary:    A new image format for the Web
License:    Apache 2
Source0:    lib%{name}-%{version}.tar.gz
Prefix:     /usr

%description
A new image format for the Web

%prep
%setup -n lib%{name}-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/cwebp
/usr/bin/dwebp
/usr/include/webp/
/usr/lib64/libwebp.a
/usr/lib64/libwebp.la
/usr/lib64/libwebp.so
/usr/lib64/libwebp.so.7
/usr/lib64/libwebp.so.7.1.0
/usr/lib64/libwebpdemux.a
/usr/lib64/libwebpdemux.la
/usr/lib64/libwebpdemux.so
/usr/lib64/libwebpdemux.so.2
/usr/lib64/libwebpdemux.so.2.0.6
/usr/lib64/pkgconfig/libwebp.pc
/usr/lib64/pkgconfig/libwebpdemux.pc
/usr/share/man/man1/cwebp.1.gz
/usr/share/man/man1/dwebp.1.gz

%changelog
* Sat Sep 05 2020 Chris Statzer <chris.statzer@qq.com> 1.1.0
- Initial RPM

