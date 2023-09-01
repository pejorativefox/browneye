Name:       xf86-input-libinput
Version:    0.28.2
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
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/xorg/libinput-properties.h
/usr/lib64/pkgconfig/xorg-libinput.pc
/usr/lib64/xorg/modules/input/libinput_drv.so
/usr/share/X11/xorg.conf.d/40-libinput.conf
/usr/share/man/man4/libinput.4.gz

%changelog
# let's skip this for now

