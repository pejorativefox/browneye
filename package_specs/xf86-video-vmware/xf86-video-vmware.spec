Name:       xf86-video-vmware
Version:    13.4.0
Release:    1
Summary:    Vmware video friver for Xorg
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz



%description
Vmware video deiver for Xorg.

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
/usr/lib64/xorg/modules/drivers/vmware_drv.la
/usr/lib64/xorg/modules/drivers/vmware_drv.so
/usr/share/man/man4/vmware.4.gz

%changelog
* Tue Jun 20 2023 Chris Statzer <chris.statzer@gmail.com> 13.4.0
- Version bump needed for new mesa/libdrm versions
