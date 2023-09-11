Name:       sdl2-image
Version:    2.0.5
Release:    1
Summary:    SDL_image is an image file loading library.
License:    zlib
Source0:    SDL2_image-%{version}.tar.gz
Prefix:     /usr

BuildRequires: sdl2

%description
SDL_image is an image file loading library.

%prep
%setup -n SDL2_image-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/SDL2/SDL_image.h
/usr/lib64/libSDL2_image-2.0.so.0
/usr/lib64/libSDL2_image-2.0.so.0.2.3
/usr/lib64/libSDL2_image.a
/usr/lib64/libSDL2_image.so
/usr/lib64/pkgconfig/SDL2_image.pc

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.0.5-1
- Initial RPM

