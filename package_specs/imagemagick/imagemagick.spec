Name:       imagemagick
Version:    7.1.1
Release:    1
Summary:    OSS image manipulation toolkit
License:    GPL3
Prefix:     /usr
Source0:    ImageMagick-7.1.1-15.tar.xz

%description
ImageMagick is a free, open-source software suite, used for editing and manipulating digital images.

%prep
%setup -q -n ImageMagick-7.1.1-15

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

%files -f ../../SOURCES/imagemagick.filelist

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 7.1.1-1
- Version bump

