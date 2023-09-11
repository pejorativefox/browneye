Name:       sdl-image
Version:    1.2.12
Release:    1
Summary:    SDL_image is an image file loading library
License:    zlib
Source0:    SDL_image-%{version}.tar.gz
Prefix:     /usr

BuildRequires: sdl

%description
SDL_image is an image file loading library

%prep
%setup -n SDL_image-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/SDL/SDL_image.h
/usr/lib64/libSDL_image-1.2.so.0
/usr/lib64/libSDL_image-1.2.so.0.8.4
/usr/lib64/libSDL_image.a
/usr/lib64/libSDL_image.so
/usr/lib64/pkgconfig/SDL_image.pc

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 1.2.12
- Initial RPM

