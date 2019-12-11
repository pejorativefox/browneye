Name:       sdl2 
Version:    2.0.8
Release:    1
Summary:    Simple Direct Media Layer 2
License:    GPM
Source0:    SDL2-%{version}.tar.gz
Prefix:     /usr

%description
Simple DirectMedia Layer is a cross-platform development library designed to 
provide low level access to audio, keyboard, mouse, joystick, and graphics 
hardware via OpenGL and Direct3D.

%prep
%setup -n SDL2-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/sdl2-config
/usr/include/*
/usr/lib64/cmake/SDL2/sdl2-config.cmake
/usr/lib64/libSDL2-2.0.so.0
/usr/lib64/libSDL2-2.0.so.0.8.0
/usr/lib64/libSDL2.a
/usr/lib64/libSDL2.la
/usr/lib64/libSDL2.so
/usr/lib64/libSDL2_test.a
/usr/lib64/libSDL2_test.la
/usr/lib64/libSDL2main.a
/usr/lib64/libSDL2main.la
/usr/lib64/pkgconfig/sdl2.pc
/usr/share/aclocal/sdl2.m4

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.0.8
- Initial RPM

