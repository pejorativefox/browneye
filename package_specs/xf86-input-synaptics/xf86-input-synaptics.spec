Name:       xf86-input-synaptics
Version:    1.9.1
Release:    1
Summary:    Synaptics touchpad driver
License:    Xorg
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Synaptics touchpad driver

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/synclient
/usr/bin/syndaemon
/usr/include/xorg/synaptics-properties.h
/usr/lib64/pkgconfig/xorg-synaptics.pc
/usr/lib64/xorg/modules/input/synaptics_drv.la
/usr/lib64/xorg/modules/input/synaptics_drv.so
/usr/share/X11/xorg.conf.d/70-synaptics.conf
/usr/share/man/man1/synclient.1.gz
/usr/share/man/man1/syndaemon.1.gz
/usr/share/man/man4/synaptics.4.gz

%changelog
* Mon May 18 2020 Chris Statzer <chris.statzer@qq.com> 1.9.1
- Initial RPM

