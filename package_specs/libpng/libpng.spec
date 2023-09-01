Name:       libpng
Version:    1.6.36
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz
Patch:     libpng-1.6.36-apng.patch

BuildRequires: zlib, pkg-config

Provides: pkgconfig(libpng)

%description
TODO

%prep
%setup -a 0
%patch -p 1

%build
LIBS=-lpthread ./configure --prefix=/usr --disable-static 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/libpng-config
/usr/bin/libpng16-config
/usr/bin/png-fix-itxt
/usr/bin/pngfix
/usr/include/libpng16/png.h
/usr/include/libpng16/pngconf.h
/usr/include/libpng16/pnglibconf.h
/usr/include/png.h
/usr/include/pngconf.h
/usr/include/pnglibconf.h
/usr/lib/libpng.so
/usr/lib/libpng.la
/usr/lib/libpng16.so
/usr/lib/libpng16.so.16
/usr/lib/libpng16.so.16.36.0
/usr/lib/pkgconfig/libpng.pc
/usr/lib/pkgconfig/libpng16.pc
/usr/share/man/man3/libpng.3.gz
/usr/share/man/man3/libpngpf.3.gz
/usr/share/man/man5/png.5.gz

%changelog
# let's skip this for now

