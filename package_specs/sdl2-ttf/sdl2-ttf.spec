Name:       sdl2-ttf
Version:    2.0.15
Release:    1
Summary:    SDL2 True type font library
License:    zlib
Source0:    SDL2_ttf-%{version}.tar.gz
Prefix:     /usr

BuildRequires: sdl2
BuildRequires: freetype

%description
This is a sample library which allows you to use TrueType fonts in your SDL applications.

%prep
%setup -n SDL2_ttf-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/SDL2/SDL_ttf.h
/usr/lib64/libSDL2_ttf-2.0.so.0
/usr/lib64/libSDL2_ttf-2.0.so.0.14.1
/usr/lib64/libSDL2_ttf.a
/usr/lib64/libSDL2_ttf.so
/usr/lib64/pkgconfig/SDL2_ttf.pc

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.0.15-1
- Initial RPM

