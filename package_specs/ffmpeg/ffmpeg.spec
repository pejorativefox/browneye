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
/usr/include/libavcodec/*
/usr/include/libavdevice/avdevice.h
/usr/include/libavdevice/version.h
/usr/include/libavfilter/avfilter.h
/usr/include/libavfilter/buffersink.h
/usr/include/libavfilter/buffersrc.h
/usr/include/libavfilter/version.h
/usr/include/libavformat/avformat.h
/usr/include/libavformat/avio.h
/usr/include/libavformat/version.h
/usr/include/libavutil/*
/usr/include/libpostproc/postprocess.h
/usr/include/libpostproc/version.h
/usr/include/libswresample/swresample.h
/usr/include/libswresample/version.h
/usr/include/libswscale/swscale.h
/usr/include/libswscale/version.h
/usr/lib/libavcodec.so
/usr/lib/libavcodec.so.58
/usr/lib/libavcodec.so.58.35.100
/usr/lib/libavdevice.so
/usr/lib/libavdevice.so.58
/usr/lib/libavdevice.so.58.5.100
/usr/lib/libavfilter.so
/usr/lib/libavfilter.so.7
/usr/lib/libavfilter.so.7.40.101
/usr/lib/libavformat.so
/usr/lib/libavformat.so.58
/usr/lib/libavformat.so.58.20.100
/usr/lib/libavutil.so
/usr/lib/libavutil.so.56
/usr/lib/libavutil.so.56.22.100
/usr/lib/libpostproc.so
/usr/lib/libpostproc.so.55
/usr/lib/libpostproc.so.55.3.100
/usr/lib/libswresample.so
/usr/lib/libswresample.so.3
/usr/lib/libswresample.so.3.3.100
/usr/lib/libswscale.so
/usr/lib/libswscale.so.5
/usr/lib/libswscale.so.5.3.100
/usr/lib/pkgconfig/libavcodec.pc
/usr/lib/pkgconfig/libavdevice.pc
/usr/lib/pkgconfig/libavfilter.pc
/usr/lib/pkgconfig/libavformat.pc
/usr/lib/pkgconfig/libavutil.pc
/usr/lib/pkgconfig/libpostproc.pc
/usr/lib/pkgconfig/libswresample.pc
/usr/lib/pkgconfig/libswscale.pc
/usr/share/doc/*
/usr/share/ffmpeg/*
/usr/share/man/*
/usr/bin/ffplay
/usr/share/doc/ffmpeg-4.1.1/ffplay-all.html
/usr/share/doc/ffmpeg-4.1.1/ffplay.html
/usr/share/man/man1/ffplay-all.1.gz
/usr/share/man/man1/ffplay.1.gz


%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.1.1
- Initial RPM

