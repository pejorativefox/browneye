Name:       sdl
Version:    1.2.15
Release:    1
Summary:    Simple DirectMedia Layer
License:    zlib
Source0:    SDL-%{version}.tar.gz
Patch:      SDL-1.2.15-const_XData32.patch
Prefix:     /usr

%description
Simple DirectMedia Layer is a cross-platform development library

%prep
%setup -n SDL-%{version}
%patch -p1

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/sdl-config
/usr/include/SDL/
/usr/lib64/libSDL-1.2.so.0
/usr/lib64/libSDL-1.2.so.0.11.4
/usr/lib64/libSDL.a
/usr/lib64/libSDL.so
/usr/lib64/libSDLmain.a
/usr/lib64/pkgconfig/sdl.pc
/usr/share/aclocal/sdl.m4
/usr/share/man/man3/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 1.2.15
- Initial RPM

