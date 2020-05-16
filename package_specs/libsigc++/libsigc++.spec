Name:       libsigc++
Version:    2.10.3
Release:    1
Summary:    libsigc++ provides a typesafe (at compile time) callback system for standard C++.
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
libsigc++ provides a typesafe (at compile time) callback system for standard C++.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/sigc++-2.0/
/usr/share/doc/libsigc++-2.0/
/usr/lib64/libsigc-2.0.la
/usr/lib64/libsigc-2.0.so
/usr/lib64/libsigc-2.0.so.0
/usr/lib64/libsigc-2.0.so.0.0.0
/usr/lib64/pkgconfig/sigc++-2.0.pc
/usr/lib64/sigc++-2.0/include/sigc++config.h
/usr/share/devhelp/books/libsigc++-2.0/libsigc++-2.0.devhelp2

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.10.3
- Initial RPM

