Name:       alsa-utils
Version:    1.2.2
Release:    1
Summary:    Alsa Utilities
License:    BSD
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
The ALSA Utilities package contains various utilities which are useful for controlling your sound card. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/lib/udev/rules.d/
/usr/bin/aconnect
/usr/bin/alsabat
/usr/bin/alsaloop
/usr/bin/alsamixer
/usr/bin/alsaucm
/usr/bin/amidi
/usr/bin/amixer
/usr/bin/aplay
/usr/bin/aplaymidi
/usr/bin/arecord
/usr/bin/arecordmidi
/usr/bin/aseqdump
/usr/bin/aseqnet
/usr/bin/axfer
/usr/bin/iecset
/usr/bin/speaker-test
/usr/sbin/alsa-info.sh
/usr/sbin/alsabat-test.sh
/usr/sbin/alsaconf
/usr/sbin/alsactl
/usr/share/alsa/
/usr/share/locale/
/usr/share/man/
/usr/share/sounds/alsa/

%changelog
* Thu May 28 2020 Chris Statzer <chris.statzer@qq.com> 1.2.2
- Initial RPM

