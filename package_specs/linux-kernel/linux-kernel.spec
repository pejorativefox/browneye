Name:       linux-kernel
Version:    5.3.16
Release:    1
Summary:    Linux kernel
License:    GPL3
Prefix:     /usr
Source0:    linux-%{version}.tar.xz

%description
Linux kernel

%prep
%setup -n linux-%{version}

%build
make mrproper
make defconfig
%make_build

%install    
mkdir -pv %{buildroot}/boot
%make_install INSTALL_PATH=%{buildroot}/boot

%files
/boot/System.map
/boot/vmlinuz

%changelog
* Mon Dec 16 2019 Chris Statzer <chris.statzer@qq.com> 5.3.16
- Kernel upgrade

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.20.12
- Initial RPM
