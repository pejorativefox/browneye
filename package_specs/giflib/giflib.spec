Name:       giflib
Version:    5.2.1
Release:    1
Summary:    Library for loading and manipulationg GIF images
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The giflib package contains libraries for reading and writing GIFs as well as programs for converting and working with GIF files. 

%prep
%setup

%build
%make_build 

%install
rm -rf %{buildroot}
make install PREFIX=%{buildroot}/usr

%files
/usr/bin/gif2rgb
/usr/bin/gifbuild
/usr/bin/gifclrmp
/usr/bin/giffix
/usr/bin/giftext
/usr/bin/giftool
/usr/include/gif_lib.h
/usr/lib/libgif.a
/usr/lib/libgif.so
/usr/lib/libgif.so.7
/usr/lib/libgif.so.7.2.0
/usr/share/man/man1/

%changelog
* Wed Aug 19 2020 Chris Statzer <chris.statzer@qq.com> 5.2.1
- Initial RPM

