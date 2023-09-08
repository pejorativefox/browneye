Name:       vala
Version:    0.40.8
Release:    1
Summary:    Vala programming language.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Vala is a new programming language that aims to bring modern programming language features to GNOME developers without imposing any additional runtime requirements and without using a different ABI compared to applications and libraries written in C. 

%prep
%setup

%build
sed -i '115d; 121,137d; 139,140d'  configure.ac &&
sed -i '/valadoc/d' Makefile.am                 &&
ACLOCAL= autoreconf -fiv
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/vala
/usr/bin/vala-0.40
/usr/bin/vala-gen-introspect
/usr/bin/vala-gen-introspect-0.40
/usr/bin/valac
/usr/bin/valac-0.40
/usr/bin/vapigen
/usr/bin/vapigen-0.40
/usr/include/vala-0.40/vala.h
/usr/include/vala-0.40/valagee.h
/usr/lib64/libvala-0.40.so
/usr/lib64/libvala-0.40.so.0
/usr/lib64/libvala-0.40.so.0.0.0
/usr/lib64/pkgconfig/libvala-0.40.pc
/usr/lib64/pkgconfig/vapigen-0.40.pc
/usr/lib64/pkgconfig/vapigen.pc
/usr/lib64/vala-0.40/gen-introspect-0.40
/usr/lib64/vala-0.40/libvalaccodegen.so
/usr/share/aclocal/vala.m4
/usr/share/aclocal/vapigen.m4
/usr/share/vala/Makefile.vapigen
/usr/share/vala/vapi/libvala-0.40.vapi
/usr/share/man/*
/usr/share/vala-0.40/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.40.8
- Initial RPM

