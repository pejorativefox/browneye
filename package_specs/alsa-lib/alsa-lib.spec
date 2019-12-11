Name:       alsa-lib
Version:    1.1.6
Release:    1
Summary:    ALSA sound interface library.
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
The ALSA Library package contains the ALSA library used by programs (including ALSA Utilities) requiring access to the ALSA sound interface. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/share/alsa/*
/usr/include/alsa/*
/usr/bin/aserver
/usr/include/sys/asoundlib.h
/usr/lib64/libasound.la
/usr/lib64/libasound.so
/usr/lib64/libasound.so.2
/usr/lib64/libasound.so.2.0.0
/usr/lib64/pkgconfig/alsa.pc
/usr/share/aclocal/alsa.m4

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.1.6
- Initial RPM

