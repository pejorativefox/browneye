Name:       pkgconf
Version:    2.0.1
Release:    1
Summary:    Successor to pkg-config
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Successor to pkg-config and contains a tool for passing the include path and/or library paths to build tools during the configure and make phases of package installations. 

%prep
%setup -q

%build
%configure  --disable-static           \
            --docdir=/usr/share/doc/pkgconf-%{version}
%make_build

%install
rm -rf %{buildroot}
%make_install

ln -sv pkgconf   %{buildroot}/usr/bin/pkg-config
ln -sv pkgconf.1 %{buildroot}/usr/share/man/man1/pkg-config.1

%files
/usr/bin/bomtool
/usr/bin/pkg-config
/usr/bin/pkgconf
/usr/include/pkgconf/libpkgconf/bsdstubs.h
/usr/include/pkgconf/libpkgconf/iter.h
/usr/include/pkgconf/libpkgconf/libpkgconf-api.h
/usr/include/pkgconf/libpkgconf/libpkgconf.h
/usr/include/pkgconf/libpkgconf/stdinc.h
/usr/lib64/libpkgconf.so
/usr/lib64/libpkgconf.so.4
/usr/lib64/libpkgconf.so.4.0.0
/usr/lib64/pkgconfig/libpkgconf.pc
/usr/share/aclocal/pkg.m4
/usr/share/doc/pkgconf-2.0.1/AUTHORS
/usr/share/doc/pkgconf-2.0.1/README.md
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 2.0.1
- Initial rpm
