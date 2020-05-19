Name:       ImageMagick
Version:    7.0.8
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-7.0.8-27.tar.xz

%description
TODO

%prep
%setup -a 0 -n ImageMagick-7.0.8-27

%build
%configure  --sysconfdir=/etc \
            --enable-hdri     \
            --with-modules    \
            --with-perl       \
            --disable-static
%make_build


%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/ImageMagick-7/
/usr/bin/Magick++-config
/usr/bin/MagickCore-config
/usr/bin/MagickWand-config
/usr/bin/animate
/usr/bin/compare
/usr/bin/composite
/usr/bin/conjure
/usr/bin/convert
/usr/bin/display
/usr/bin/identify
/usr/bin/import
/usr/bin/magick
/usr/bin/magick-script
/usr/bin/mogrify
/usr/bin/montage
/usr/bin/stream
/usr/include/ImageMagick-7/
/usr/lib/perl5/5.28.1/x86_64-linux-thread-multi/perllocal.pod
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/Image/Magick.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/Image/Magick/Q16HDRI.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/Image/Magick/.packlist
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/Image/Magick/Q16HDRI/Q16HDRI.so
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/Image/Magick/Q16HDRI/autosplit.ix
/usr/lib64/ImageMagick-7.0.8/
/usr/lib64/libMagick++-7.Q16HDRI.la
/usr/lib64/libMagick++-7.Q16HDRI.so
/usr/lib64/libMagick++-7.Q16HDRI.so.4
/usr/lib64/libMagick++-7.Q16HDRI.so.4.0.0
/usr/lib64/libMagickCore-7.Q16HDRI.la
/usr/lib64/libMagickCore-7.Q16HDRI.so
/usr/lib64/libMagickCore-7.Q16HDRI.so.6
/usr/lib64/libMagickCore-7.Q16HDRI.so.6.0.0
/usr/lib64/libMagickWand-7.Q16HDRI.la
/usr/lib64/libMagickWand-7.Q16HDRI.so
/usr/lib64/libMagickWand-7.Q16HDRI.so.6
/usr/lib64/libMagickWand-7.Q16HDRI.so.6.0.0
/usr/lib64/pkgconfig/ImageMagick-7.Q16HDRI.pc
/usr/lib64/pkgconfig/ImageMagick.pc
/usr/lib64/pkgconfig/Magick++-7.Q16HDRI.pc
/usr/lib64/pkgconfig/Magick++.pc
/usr/lib64/pkgconfig/MagickCore-7.Q16HDRI.pc
/usr/lib64/pkgconfig/MagickCore.pc
/usr/lib64/pkgconfig/MagickWand-7.Q16HDRI.pc
/usr/lib64/pkgconfig/MagickWand.pc
/usr/share/ImageMagick-7/english.xml
/usr/share/ImageMagick-7/francais.xml
/usr/share/ImageMagick-7/locale.xml
/usr/share/doc/ImageMagick-7/
/usr/share/man/man1/
/usr/share/man/man3/Image::Magick.3.gz
/usr/share/man/man3/Image::Magick::Q16HDRI.3.gz

%changelog
# let's skip this for now

