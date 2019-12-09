Name:       libusb
Version:    1.0.23
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

%description
TODO

%prep
%setup -a 0

%build
%configure 
%make_build

%install
%make_install

%files
/usr/include/libusb-1.0/libusb.h
/usr/lib64/libusb-1.0.a
/usr/lib64/libusb-1.0.la
/usr/lib64/libusb-1.0.so
/usr/lib64/libusb-1.0.so.0
/usr/lib64/libusb-1.0.so.0.2.0
/usr/lib64/pkgconfig/libusb-1.0.pc


%changelog
# let's skip this for now
