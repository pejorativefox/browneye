Name:       ffmpeg
Version:    4.1.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description

%prep
%setup

%build
sed -i 's/-lflite"/-lflite -lasound"/' configure &&

./configure  --prefix=/usr --enable-gpl         \
            --enable-version3    \
            --enable-nonfree     \
            --disable-static     \
            --enable-shared      \
            --disable-debug      \
            --enable-libfreetype \
            --enable-libmp3lame  \
            --enable-libopus     \
            --enable-libtheora   \
            --enable-libvorbis   \
            --enable-libvpx      \
            --enable-libx264     \
            --enable-libx265     \
            --docdir=/usr/share/doc/ffmpeg-4.1.1
            
TEXINFO_XS=omit make

gcc tools/qt-faststart.c -o tools/qt-faststart

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

cp -v tools/qt-faststart %{buildroot}/usr/bin

%files
/usr/bin/ffmpeg
/usr/bin/ffprobe
/usr/bin/qt-faststart
/usr/include/
/usr/lib/
/usr/share/
/usr/bin/ffplay

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.1.1
- Initial RPM

