Name:       fontconfig
Version:    2.13.1
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
rm -f src/fcobjshash.h
%configure  --sysconfdir=/etc    \
            --localstatedir=/var \
            --disable-docs       \
            --docdir=/usr/share/doc/fontconfig-2.13.1
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/fonts/conf.d/10-hinting-slight.conf
/etc/fonts/conf.d/10-scale-bitmap-fonts.conf
/etc/fonts/conf.d/20-unhint-small-vera.conf
/etc/fonts/conf.d/30-metric-aliases.conf
/etc/fonts/conf.d/40-nonlatin.conf
/etc/fonts/conf.d/45-generic.conf
/etc/fonts/conf.d/45-latin.conf
/etc/fonts/conf.d/49-sansserif.conf
/etc/fonts/conf.d/50-user.conf
/etc/fonts/conf.d/51-local.conf
/etc/fonts/conf.d/60-generic.conf
/etc/fonts/conf.d/60-latin.conf
/etc/fonts/conf.d/65-fonts-persian.conf
/etc/fonts/conf.d/65-nonlatin.conf
/etc/fonts/conf.d/69-unifont.conf
/etc/fonts/conf.d/80-delicious.conf
/etc/fonts/conf.d/90-synthetic.conf
/etc/fonts/conf.d/README
/etc/fonts/fonts.conf
/usr/bin/fc-cache
/usr/bin/fc-cat
/usr/bin/fc-conflist
/usr/bin/fc-list
/usr/bin/fc-match
/usr/bin/fc-pattern
/usr/bin/fc-query
/usr/bin/fc-scan
/usr/bin/fc-validate
/usr/include/fontconfig/fcfreetype.h
/usr/include/fontconfig/fcprivate.h
/usr/include/fontconfig/fontconfig.h
/usr/lib64/libfontconfig.so
/usr/lib64/libfontconfig.so.1
/usr/lib64/libfontconfig.so.1.12.0
/usr/lib64/pkgconfig/fontconfig.pc
/usr/share/fontconfig/conf.avail/10-autohint.conf
/usr/share/fontconfig/conf.avail/10-hinting-full.conf
/usr/share/fontconfig/conf.avail/10-hinting-medium.conf
/usr/share/fontconfig/conf.avail/10-hinting-none.conf
/usr/share/fontconfig/conf.avail/10-hinting-slight.conf
/usr/share/fontconfig/conf.avail/10-no-sub-pixel.conf
/usr/share/fontconfig/conf.avail/10-scale-bitmap-fonts.conf
/usr/share/fontconfig/conf.avail/10-sub-pixel-bgr.conf
/usr/share/fontconfig/conf.avail/10-sub-pixel-rgb.conf
/usr/share/fontconfig/conf.avail/10-sub-pixel-vbgr.conf
/usr/share/fontconfig/conf.avail/10-sub-pixel-vrgb.conf
/usr/share/fontconfig/conf.avail/10-unhinted.conf
/usr/share/fontconfig/conf.avail/11-lcdfilter-default.conf
/usr/share/fontconfig/conf.avail/11-lcdfilter-legacy.conf
/usr/share/fontconfig/conf.avail/11-lcdfilter-light.conf
/usr/share/fontconfig/conf.avail/20-unhint-small-vera.conf
/usr/share/fontconfig/conf.avail/25-unhint-nonlatin.conf
/usr/share/fontconfig/conf.avail/30-metric-aliases.conf
/usr/share/fontconfig/conf.avail/40-nonlatin.conf
/usr/share/fontconfig/conf.avail/45-generic.conf
/usr/share/fontconfig/conf.avail/45-latin.conf
/usr/share/fontconfig/conf.avail/49-sansserif.conf
/usr/share/fontconfig/conf.avail/50-user.conf
/usr/share/fontconfig/conf.avail/51-local.conf
/usr/share/fontconfig/conf.avail/60-generic.conf
/usr/share/fontconfig/conf.avail/60-latin.conf
/usr/share/fontconfig/conf.avail/65-fonts-persian.conf
/usr/share/fontconfig/conf.avail/65-khmer.conf
/usr/share/fontconfig/conf.avail/65-nonlatin.conf
/usr/share/fontconfig/conf.avail/69-unifont.conf
/usr/share/fontconfig/conf.avail/70-no-bitmaps.conf
/usr/share/fontconfig/conf.avail/70-yes-bitmaps.conf
/usr/share/fontconfig/conf.avail/80-delicious.conf
/usr/share/fontconfig/conf.avail/90-synthetic.conf
/usr/share/gettext/its/fontconfig.its
/usr/share/gettext/its/fontconfig.loc
/usr/share/locale/zh_CN/LC_MESSAGES/fontconfig-conf.mo
/usr/share/locale/zh_CN/LC_MESSAGES/fontconfig.mo
/usr/share/xml/fontconfig/fonts.dtd


%changelog
# let's skip this for now
