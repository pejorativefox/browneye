Name:       pulseaudio
Version:    12.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

BuildRequires: libsndfile

%description
TODO

%prep
%setup 

%build
%configure  --sysconfdir=/etc    \
            --localstatedir=/var \
            --disable-bluez4     \
            --disable-bluez5     \
            --disable-rpath
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
sed -i '/load-module module-console-kit/s/^/#/' %{buildroot}/etc/pulse/default.pa
rm -fv %{buildroot}/etc/dbus-1/system.d/pulseaudio-system.conf

%files
/etc/pulse/client.conf
/etc/pulse/daemon.conf
/etc/pulse/default.pa
/etc/pulse/system.pa
/etc/xdg/autostart/pulseaudio.desktop
/usr/bin/esdcompat
/usr/bin/pacat
/usr/bin/pacmd
/usr/bin/pactl
/usr/bin/padsp
/usr/bin/pamon
/usr/bin/paplay
/usr/bin/parec
/usr/bin/parecord
/usr/bin/pasuspender
/usr/bin/pax11publish
/usr/bin/pulseaudio
/usr/bin/start-pulseaudio-x11
/usr/include/pulse/*
/lib/udev/rules.d/90-pulseaudio.rules
/usr/lib64/cmake/PulseAudio/PulseAudioConfig.cmake
/usr/lib64/cmake/PulseAudio/PulseAudioConfigVersion.cmake
/usr/lib64/libpulse-mainloop-glib.so
/usr/lib64/libpulse-mainloop-glib.so.0
/usr/lib64/libpulse-mainloop-glib.so.0.0.5
/usr/lib64/libpulse-simple.so
/usr/lib64/libpulse-simple.so.0
/usr/lib64/libpulse-simple.so.0.1.1
/usr/lib64/libpulse.so
/usr/lib64/libpulse.so.0
/usr/lib64/libpulse.so.0.20.3
/usr/lib64/pkgconfig/libpulse-mainloop-glib.pc
/usr/lib64/pkgconfig/libpulse-simple.pc
/usr/lib64/pkgconfig/libpulse.pc
/usr/lib64/pulse-12.2/*
/usr/lib64/pulseaudio/libpulsecommon-12.2.so
/usr/lib64/pulseaudio/libpulsecore-12.2.so
/usr/lib64/pulseaudio/libpulsedsp.so
/usr/libexec/pulse/gsettings-helper
/usr/share/GConf/gsettings/pulseaudio.convert
/usr/share/bash-completion/completions/*
/usr/share/glib-2.0/schemas/org.freedesktop.pulseaudio.gschema.xml
/usr/share/locale/*
/usr/share/man/*
/usr/share/vala/vapi/*
/usr/share/zsh/site-functions/_pulseaudio
/usr/share/pulseaudio/*


%changelog
# let's skip this for now

