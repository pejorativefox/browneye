Name:       libevdev
Version:    1.6.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -a 0

%build
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/libevdev-tweak-device
/usr/bin/mouse-dpi-tool
/usr/bin/touchpad-edge-detector
/usr/include/libevdev-1.0/libevdev/libevdev-uinput.h
/usr/include/libevdev-1.0/libevdev/libevdev.h
/usr/lib64/libevdev.a
/usr/lib64/libevdev.la
/usr/lib64/libevdev.so
/usr/lib64/libevdev.so.2
/usr/lib64/libevdev.so.2.2.0
/usr/lib64/pkgconfig/libevdev.pc
/usr/share/man/man3/libevdev.3.gz

%changelog
# let's skip this for now

