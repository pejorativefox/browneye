Name:       freetype
Version:    2.9.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

Provides: pkgconfig(freetype2)

%description
TODO

%prep
%setup -a 0


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
/usr/lib64/libfreetype.so.6.16.1
/usr/lib64/pkgconfig/freetype2.pc
/usr/share/aclocal/freetype2.m4
/usr/share/man/man1/freetype-config.1.gz

%changelog
# let's skip this for now
