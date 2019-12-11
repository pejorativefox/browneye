Name:       ffmpeg
Version:    4.1.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

            #--enable-avresample  \
            #--enable-libfdk-aac  \

%prep
%setup -a 0 

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
/usr/include/libavcodec/ac3_parser.h
/usr/include/libavcodec/adts_parser.h
/usr/include/libavcodec/avcodec.h
/usr/include/libavcodec/avdct.h
/usr/include/libavcodec/avfft.h
/usr/include/libavcodec/d3d11va.h
/usr/include/libavcodec/dirac.h
/usr/include/libavcodec/dv_profile.h
/usr/include/libavcodec/dxva2.h
/usr/include/libavcodec/jni.h
/usr/include/libavcodec/mediacodec.h
/usr/include/libavcodec/qsv.h
/usr/include/libavcodec/vaapi.h
/usr/include/libavcodec/vdpau.h
/usr/include/libavcodec/version.h
/usr/include/libavcodec/videotoolbox.h
/usr/include/libavcodec/vorbis_parser.h
/usr/include/libavcodec/xvmc.h
/usr/include/libavdevice/avdevice.h
/usr/include/libavdevice/version.h
/usr/include/libavfilter/avfilter.h
/usr/include/libavfilter/buffersink.h
/usr/include/libavfilter/buffersrc.h
/usr/include/libavfilter/version.h
/usr/include/libavformat/avformat.h
/usr/include/libavformat/avio.h
/usr/include/libavformat/version.h
/usr/include/libavutil/adler32.h
/usr/include/libavutil/aes.h
/usr/include/libavutil/aes_ctr.h
/usr/include/libavutil/attributes.h
/usr/include/libavutil/audio_fifo.h
/usr/include/libavutil/avassert.h
/usr/include/libavutil/avconfig.h
/usr/include/libavutil/avstring.h
/usr/include/libavutil/avutil.h
/usr/include/libavutil/base64.h
/usr/include/libavutil/blowfish.h
/usr/include/libavutil/bprint.h
/usr/include/libavutil/bswap.h
/usr/include/libavutil/buffer.h
/usr/include/libavutil/camellia.h
/usr/include/libavutil/cast5.h
/usr/include/libavutil/channel_layout.h
/usr/include/libavutil/common.h
/usr/include/libavutil/cpu.h
/usr/include/libavutil/crc.h
/usr/include/libavutil/des.h
/usr/include/libavutil/dict.h
/usr/include/libavutil/display.h
/usr/include/libavutil/downmix_info.h
/usr/include/libavutil/encryption_info.h
/usr/include/libavutil/error.h
/usr/include/libavutil/eval.h
/usr/include/libavutil/ffversion.h
/usr/include/libavutil/fifo.h
/usr/include/libavutil/file.h
/usr/include/libavutil/frame.h
/usr/include/libavutil/hash.h
/usr/include/libavutil/hmac.h
/usr/include/libavutil/hwcontext.h
/usr/include/libavutil/hwcontext_cuda.h
/usr/include/libavutil/hwcontext_d3d11va.h
/usr/include/libavutil/hwcontext_drm.h
/usr/include/libavutil/hwcontext_dxva2.h
/usr/include/libavutil/hwcontext_mediacodec.h
/usr/include/libavutil/hwcontext_qsv.h
/usr/include/libavutil/hwcontext_vaapi.h
/usr/include/libavutil/hwcontext_vdpau.h
/usr/include/libavutil/hwcontext_videotoolbox.h
/usr/include/libavutil/imgutils.h
/usr/include/libavutil/intfloat.h
/usr/include/libavutil/intreadwrite.h
/usr/include/libavutil/lfg.h
/usr/include/libavutil/log.h
/usr/include/libavutil/lzo.h
/usr/include/libavutil/macros.h
/usr/include/libavutil/mastering_display_metadata.h
/usr/include/libavutil/mathematics.h
/usr/include/libavutil/md5.h
/usr/include/libavutil/mem.h
/usr/include/libavutil/motion_vector.h
/usr/include/libavutil/murmur3.h
/usr/include/libavutil/opt.h
/usr/include/libavutil/parseutils.h
/usr/include/libavutil/pixdesc.h
/usr/include/libavutil/pixelutils.h
/usr/include/libavutil/pixfmt.h
/usr/include/libavutil/random_seed.h
/usr/include/libavutil/rational.h
/usr/include/libavutil/rc4.h
/usr/include/libavutil/replaygain.h
/usr/include/libavutil/ripemd.h
/usr/include/libavutil/samplefmt.h
/usr/include/libavutil/sha.h
/usr/include/libavutil/sha512.h
/usr/include/libavutil/spherical.h
/usr/include/libavutil/stereo3d.h
/usr/include/libavutil/tea.h
/usr/include/libavutil/threadmessage.h
/usr/include/libavutil/time.h
/usr/include/libavutil/timecode.h
/usr/include/libavutil/timestamp.h
/usr/include/libavutil/tree.h
/usr/include/libavutil/twofish.h
/usr/include/libavutil/version.h
/usr/include/libavutil/xtea.h
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
/usr/share/doc/ffmpeg-4.1.1/developer.html
/usr/share/doc/ffmpeg-4.1.1/faq.html
/usr/share/doc/ffmpeg-4.1.1/fate.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-all.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-bitstream-filters.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-codecs.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-devices.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-filters.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-formats.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-protocols.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-resampler.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-scaler.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg-utils.html
/usr/share/doc/ffmpeg-4.1.1/ffmpeg.html
/usr/share/doc/ffmpeg-4.1.1/ffprobe-all.html
/usr/share/doc/ffmpeg-4.1.1/ffprobe.html
/usr/share/doc/ffmpeg-4.1.1/general.html
/usr/share/doc/ffmpeg-4.1.1/git-howto.html
/usr/share/doc/ffmpeg-4.1.1/libavcodec.html
/usr/share/doc/ffmpeg-4.1.1/libavdevice.html
/usr/share/doc/ffmpeg-4.1.1/libavfilter.html
/usr/share/doc/ffmpeg-4.1.1/libavformat.html
/usr/share/doc/ffmpeg-4.1.1/libavutil.html
/usr/share/doc/ffmpeg-4.1.1/libswresample.html
/usr/share/doc/ffmpeg-4.1.1/libswscale.html
/usr/share/doc/ffmpeg-4.1.1/mailing-list-faq.html
/usr/share/doc/ffmpeg-4.1.1/nut.html
/usr/share/doc/ffmpeg-4.1.1/platform.html
/usr/share/ffmpeg/examples/Makefile
/usr/share/ffmpeg/examples/README
/usr/share/ffmpeg/examples/avio_dir_cmd.c
/usr/share/ffmpeg/examples/avio_reading.c
/usr/share/ffmpeg/examples/decode_audio.c
/usr/share/ffmpeg/examples/decode_video.c
/usr/share/ffmpeg/examples/demuxing_decoding.c
/usr/share/ffmpeg/examples/encode_audio.c
/usr/share/ffmpeg/examples/encode_video.c
/usr/share/ffmpeg/examples/extract_mvs.c
/usr/share/ffmpeg/examples/filter_audio.c
/usr/share/ffmpeg/examples/filtering_audio.c
/usr/share/ffmpeg/examples/filtering_video.c
/usr/share/ffmpeg/examples/http_multiclient.c
/usr/share/ffmpeg/examples/hw_decode.c
/usr/share/ffmpeg/examples/metadata.c
/usr/share/ffmpeg/examples/muxing.c
/usr/share/ffmpeg/examples/qsvdec.c
/usr/share/ffmpeg/examples/remuxing.c
/usr/share/ffmpeg/examples/resampling_audio.c
/usr/share/ffmpeg/examples/scaling_video.c
/usr/share/ffmpeg/examples/transcode_aac.c
/usr/share/ffmpeg/examples/transcoding.c
/usr/share/ffmpeg/examples/vaapi_encode.c
/usr/share/ffmpeg/examples/vaapi_transcode.c
/usr/share/ffmpeg/ffprobe.xsd
/usr/share/ffmpeg/libvpx-1080p.ffpreset
/usr/share/ffmpeg/libvpx-1080p50_60.ffpreset
/usr/share/ffmpeg/libvpx-360p.ffpreset
/usr/share/ffmpeg/libvpx-720p.ffpreset
/usr/share/ffmpeg/libvpx-720p50_60.ffpreset
/usr/share/man/man1/ffmpeg-all.1.gz
/usr/share/man/man1/ffmpeg-bitstream-filters.1.gz
/usr/share/man/man1/ffmpeg-codecs.1.gz
/usr/share/man/man1/ffmpeg-devices.1.gz
/usr/share/man/man1/ffmpeg-filters.1.gz
/usr/share/man/man1/ffmpeg-formats.1.gz
/usr/share/man/man1/ffmpeg-protocols.1.gz
/usr/share/man/man1/ffmpeg-resampler.1.gz
/usr/share/man/man1/ffmpeg-scaler.1.gz
/usr/share/man/man1/ffmpeg-utils.1.gz
/usr/share/man/man1/ffmpeg.1.gz
/usr/share/man/man1/ffprobe-all.1.gz
/usr/share/man/man1/ffprobe.1.gz
/usr/share/man/man3/libavcodec.3.gz
/usr/share/man/man3/libavdevice.3.gz
/usr/share/man/man3/libavfilter.3.gz
/usr/share/man/man3/libavformat.3.gz
/usr/share/man/man3/libavutil.3.gz
/usr/share/man/man3/libswresample.3.gz
/usr/share/man/man3/libswscale.3.gz
/usr/bin/ffplay
/usr/share/doc/ffmpeg-4.1.1/ffplay-all.html
/usr/share/doc/ffmpeg-4.1.1/ffplay.html
/usr/share/man/man1/ffplay-all.1.gz
/usr/share/man/man1/ffplay.1.gz


%changelog
# let's skip this for now

