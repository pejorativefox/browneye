Name:       xf86-video-fbdev
Version:    0.5.0
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
/usr/lib64/xorg/modules/drivers/fbdev_drv.la
/usr/lib64/xorg/modules/drivers/fbdev_drv.so
/usr/share/man/man4/fbdev.4.gz

%changelog
# let's skip this for now

