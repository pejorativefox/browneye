Name:       xf86-video-amdgpu
Version:    23.0.0
Release:    1
Summary:    Xorg AMDGPU driver
License:    Historical Permission Notice and Disclaimer
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Xorg driver for AMD Radeon GPUs using the amdgpu kernel driver

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/lib64/xorg/modules/drivers/amdgpu_drv.la
/usr/lib64/xorg/modules/drivers/amdgpu_drv.so
/usr/share/X11/xorg.conf.d/10-amdgpu.conf
/usr/share/man/man4/amdgpu.4.gz

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

