Name:       sdl-ttf
Version:    2.0.11
Release:    1
Summary:    SDL TrueType font library
License:    zlib
Source0:    SDL_ttf-%{version}.tar.gz
Prefix:     /usr

%description
SDL TrueType font library

%prep
%setup -n SDL_ttf-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/SDL/SDL_ttf.h
/usr/lib64/libSDL_ttf-2.0.so.0
/usr/lib64/libSDL_ttf-2.0.so.0.10.1
/usr/lib64/libSDL_ttf.a
/usr/lib64/libSDL_ttf.la
/usr/lib64/libSDL_ttf.so
/usr/lib64/pkgconfig/SDL_ttf.pc

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.0.11-1
- Initial RPM

