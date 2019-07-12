Name:       freetype
Version:    2.9.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



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
/usr/include/freetype2/freetype/config/ftconfig.h
/usr/include/freetype2/freetype/config/ftheader.h
/usr/include/freetype2/freetype/config/ftmodule.h
/usr/include/freetype2/freetype/config/ftoption.h
/usr/include/freetype2/freetype/config/ftstdlib.h
/usr/include/freetype2/freetype/freetype.h
/usr/include/freetype2/freetype/ftadvanc.h
/usr/include/freetype2/freetype/ftbbox.h
/usr/include/freetype2/freetype/ftbdf.h
/usr/include/freetype2/freetype/ftbitmap.h
/usr/include/freetype2/freetype/ftbzip2.h
/usr/include/freetype2/freetype/ftcache.h
/usr/include/freetype2/freetype/ftchapters.h
/usr/include/freetype2/freetype/ftcid.h
/usr/include/freetype2/freetype/ftdriver.h
/usr/include/freetype2/freetype/fterrdef.h
/usr/include/freetype2/freetype/fterrors.h
/usr/include/freetype2/freetype/ftfntfmt.h
/usr/include/freetype2/freetype/ftgasp.h
/usr/include/freetype2/freetype/ftglyph.h
/usr/include/freetype2/freetype/ftgxval.h
/usr/include/freetype2/freetype/ftgzip.h
/usr/include/freetype2/freetype/ftimage.h
/usr/include/freetype2/freetype/ftincrem.h
/usr/include/freetype2/freetype/ftlcdfil.h
/usr/include/freetype2/freetype/ftlist.h
/usr/include/freetype2/freetype/ftlzw.h
/usr/include/freetype2/freetype/ftmac.h
/usr/include/freetype2/freetype/ftmm.h
/usr/include/freetype2/freetype/ftmodapi.h
/usr/include/freetype2/freetype/ftmoderr.h
/usr/include/freetype2/freetype/ftotval.h
/usr/include/freetype2/freetype/ftoutln.h
/usr/include/freetype2/freetype/ftparams.h
/usr/include/freetype2/freetype/ftpfr.h
/usr/include/freetype2/freetype/ftrender.h
/usr/include/freetype2/freetype/ftsizes.h
/usr/include/freetype2/freetype/ftsnames.h
/usr/include/freetype2/freetype/ftstroke.h
/usr/include/freetype2/freetype/ftsynth.h
/usr/include/freetype2/freetype/ftsystem.h
/usr/include/freetype2/freetype/fttrigon.h
/usr/include/freetype2/freetype/fttypes.h
/usr/include/freetype2/freetype/ftwinfnt.h
/usr/include/freetype2/freetype/t1tables.h
/usr/include/freetype2/freetype/ttnameid.h
/usr/include/freetype2/freetype/tttables.h
/usr/include/freetype2/freetype/tttags.h
/usr/include/freetype2/ft2build.h
/usr/lib64/libfreetype.la
/usr/lib64/libfreetype.so
/usr/lib64/libfreetype.so.6
/usr/lib64/libfreetype.so.6.16.1
/usr/lib64/pkgconfig/freetype2.pc
/usr/share/aclocal/freetype2.m4
/usr/share/man/man1/freetype-config.1.gz

%changelog
# let's skip this for now
