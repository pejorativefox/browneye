Name:       freetype
Version:    2.13.1
Release:    1
Summary:    TrueType font library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

BuildRequires: harfbuzz >= 8.1.1

Provides: pkgconfig(freetype2)

%description
The FreeType2 package contains a library which allows applications to properly render TrueType fonts. 

%prep
%setup -q

%build
sed -ri "s:.*(AUX_MODULES.*valid):\1:" modules.cfg &&

sed -r "s:.*(#.*SUBPIXEL_RENDERING) .*:\1:" \
    -i include/freetype/config/ftoption.h  &&
%configure --enable-freetype-config --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/freetype-config
/usr/include/freetype2/
/usr/lib64/libfreetype.so
/usr/lib64/libfreetype.so.6
/usr/lib64/libfreetype.so.6.20.0
/usr/lib64/pkgconfig/freetype2.pc
/usr/share/aclocal/freetype2.m4
/usr/share/man/man1/freetype-config.1.gz

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.13.1-1
- Version bump
