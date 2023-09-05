Name:       libxcrypt
Version:    4.4.36
Release:    1
Summary:    Password hashing library
License:    GPL2
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The Libxcrypt package contains a modern library for one-way hashing of passwords.

%prep
%setup -q

%build
%configure  --enable-hashes=strong,glibc \
            --enable-obsolete-api=no     \
            	--disable-static             \
            --disable-failure-tokens
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/crypt.h
/usr/lib64/libcrypt.so
/usr/lib64/libcrypt.so.2
/usr/lib64/libcrypt.so.2.0.0
/usr/lib64/pkgconfig/libcrypt.pc
/usr/lib64/pkgconfig/libxcrypt.pc
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Initial RPM

