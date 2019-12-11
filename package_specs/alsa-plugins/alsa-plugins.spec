Name:       alsa-plugins
Version:    1.1.6
Release:    1
Summary:    ALSA sound interface plugins.
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
 The ALSA Plugins package contains plugins for various audio libraries and sound servers.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/lib64/alsa-lib/*
/usr/share/alsa/alsa.conf.d/50-pulseaudio.conf
/usr/share/alsa/alsa.conf.d/99-pulseaudio-default.conf.example

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.1.6
- Initial RPM

