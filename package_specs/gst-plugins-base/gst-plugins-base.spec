Name:       gst-plugins-base
Version:    1.16.2
Release:    1
Summary:    Base gstreamer plugins
License:    Various
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Base gstreamer plugins

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/gst-device-monitor-1.0
/usr/bin/gst-discoverer-1.0
/usr/bin/gst-play-1.0
/usr/include/gstreamer-1.0/
/usr/lib64/girepository-1.0/GstAllocators-1.0.typelib
/usr/lib64/girepository-1.0/GstApp-1.0.typelib
/usr/lib64/girepository-1.0/GstAudio-1.0.typelib
/usr/lib64/girepository-1.0/GstGL-1.0.typelib
/usr/lib64/girepository-1.0/GstPbutils-1.0.typelib
/usr/lib64/girepository-1.0/GstRtp-1.0.typelib
/usr/lib64/girepository-1.0/GstRtsp-1.0.typelib
/usr/lib64/girepository-1.0/GstSdp-1.0.typelib
/usr/lib64/girepository-1.0/GstTag-1.0.typelib
/usr/lib64/girepository-1.0/GstVideo-1.0.typelib
/usr/lib64/gstreamer-1.0/
/usr/lib64/libgstallocators-1.0.la
/usr/lib64/libgstallocators-1.0.so
/usr/lib64/libgstallocators-1.0.so.0
/usr/lib64/libgstallocators-1.0.so.0.1602.0
/usr/lib64/libgstapp-1.0.la
/usr/lib64/libgstapp-1.0.so
/usr/lib64/libgstapp-1.0.so.0
/usr/lib64/libgstapp-1.0.so.0.1602.0
/usr/lib64/libgstaudio-1.0.la
/usr/lib64/libgstaudio-1.0.so
/usr/lib64/libgstaudio-1.0.so.0
/usr/lib64/libgstaudio-1.0.so.0.1602.0
/usr/lib64/libgstfft-1.0.la
/usr/lib64/libgstfft-1.0.so
/usr/lib64/libgstfft-1.0.so.0
/usr/lib64/libgstfft-1.0.so.0.1602.0
/usr/lib64/libgstgl-1.0.la
/usr/lib64/libgstgl-1.0.so
/usr/lib64/libgstgl-1.0.so.0
/usr/lib64/libgstgl-1.0.so.0.1602.0
/usr/lib64/libgstpbutils-1.0.la
/usr/lib64/libgstpbutils-1.0.so
/usr/lib64/libgstpbutils-1.0.so.0
/usr/lib64/libgstpbutils-1.0.so.0.1602.0
/usr/lib64/libgstriff-1.0.la
/usr/lib64/libgstriff-1.0.so
/usr/lib64/libgstriff-1.0.so.0
/usr/lib64/libgstriff-1.0.so.0.1602.0
/usr/lib64/libgstrtp-1.0.la
/usr/lib64/libgstrtp-1.0.so
/usr/lib64/libgstrtp-1.0.so.0
/usr/lib64/libgstrtp-1.0.so.0.1602.0
/usr/lib64/libgstrtsp-1.0.la
/usr/lib64/libgstrtsp-1.0.so
/usr/lib64/libgstrtsp-1.0.so.0
/usr/lib64/libgstrtsp-1.0.so.0.1602.0
/usr/lib64/libgstsdp-1.0.la
/usr/lib64/libgstsdp-1.0.so
/usr/lib64/libgstsdp-1.0.so.0
/usr/lib64/libgstsdp-1.0.so.0.1602.0
/usr/lib64/libgsttag-1.0.la
/usr/lib64/libgsttag-1.0.so
/usr/lib64/libgsttag-1.0.so.0
/usr/lib64/libgsttag-1.0.so.0.1602.0
/usr/lib64/libgstvideo-1.0.la
/usr/lib64/libgstvideo-1.0.so
/usr/lib64/libgstvideo-1.0.so.0
/usr/lib64/libgstvideo-1.0.so.0.1602.0
/usr/lib64/pkgconfig/gstreamer-allocators-1.0.pc
/usr/lib64/pkgconfig/gstreamer-app-1.0.pc
/usr/lib64/pkgconfig/gstreamer-audio-1.0.pc
/usr/lib64/pkgconfig/gstreamer-fft-1.0.pc
/usr/lib64/pkgconfig/gstreamer-gl-1.0.pc
/usr/lib64/pkgconfig/gstreamer-pbutils-1.0.pc
/usr/lib64/pkgconfig/gstreamer-plugins-base-1.0.pc
/usr/lib64/pkgconfig/gstreamer-riff-1.0.pc
/usr/lib64/pkgconfig/gstreamer-rtp-1.0.pc
/usr/lib64/pkgconfig/gstreamer-rtsp-1.0.pc
/usr/lib64/pkgconfig/gstreamer-sdp-1.0.pc
/usr/lib64/pkgconfig/gstreamer-tag-1.0.pc
/usr/lib64/pkgconfig/gstreamer-video-1.0.pc
/usr/share/gir-1.0/GstAllocators-1.0.gir
/usr/share/gir-1.0/GstApp-1.0.gir
/usr/share/gir-1.0/GstAudio-1.0.gir
/usr/share/gir-1.0/GstGL-1.0.gir
/usr/share/gir-1.0/GstPbutils-1.0.gir
/usr/share/gir-1.0/GstRtp-1.0.gir
/usr/share/gir-1.0/GstRtsp-1.0.gir
/usr/share/gir-1.0/GstSdp-1.0.gir
/usr/share/gir-1.0/GstTag-1.0.gir
/usr/share/gir-1.0/GstVideo-1.0.gir
/usr/share/gst-plugins-base/1.0/license-translations.dict
/usr/share/gtk-doc/html/gst-plugins-base-libs-1.0/
/usr/share/gtk-doc/html/gst-plugins-base-plugins-1.0/
/usr/share/locale/
/usr/share/man/man1/gst-device-monitor-1.0.1.gz
/usr/share/man/man1/gst-discoverer-1.0.1.gz
/usr/share/man/man1/gst-play-1.0.1.gz

%changelog
* Thu Sep 10 2020 Chris Statzer <chris.statzer@qq.com> 1.16.2
- Initial RPM

