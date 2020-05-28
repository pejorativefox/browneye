Name:       usbutils
Version:    012
Release:    1
Summary:    Utilities for Linux USB devices
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The USB Utils package contains utilities used to display information about USB buses in the system and the devices connected to them.

%prep
%setup

%build
./autogen.sh --prefix=/usr --datadir=/usr/share/hwdata
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/lsusb
/usr/bin/lsusb.py
/usr/bin/usb-devices
/usr/bin/usbhid-dump
/usr/share/man/man1/usb-devices.1.gz
/usr/share/man/man8/lsusb.8.gz
/usr/share/man/man8/usbhid-dump.8.gz

%changelog
* Mon May 18 2020 Chris Statzer <chris.statzer@qq.com> 012
- Initial RPM

