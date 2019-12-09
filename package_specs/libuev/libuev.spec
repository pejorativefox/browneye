Name:       libuev
Version:    2.3.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
TODO

%prep
%setup -a 0

%build
%configure 
%make_build

%install
%make_install

%files
/usr/include/uev/private.h
/usr/include/uev/uev.h
/usr/lib64/libuev.a
/usr/lib64/libuev.la
/usr/lib64/libuev.so
/usr/lib64/libuev.so.2
/usr/lib64/libuev.so.2.2.0
/usr/lib64/pkgconfig/libuev.pc
/usr/share/doc/libuev/API.md
/usr/share/doc/libuev/LICENSE
/usr/share/doc/libuev/README.md

%changelog
# let's skip this for now
