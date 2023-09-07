Name:       libuev
Version:    2.4.0
Release:    1
Summary:    Simple event loop for Linux
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
Lightweight event loop library for Linux epoll() family APIs 

%prep
%setup -q

%build
%configure 
%make_build

%install
%make_install

%files
/usr/include/uev/private.h
/usr/include/uev/uev.h
/usr/lib64/pkgconfig/libuev.pc
/usr/lib64/libuev.a
/usr/lib64/libuev.so
/usr/lib64/libuev.so.3
/usr/lib64/libuev.so.3.0.0
/usr/share/doc/libuev/LICENSE
/usr/share/doc/libuev/README.md

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.4.0-1
- Version bump
