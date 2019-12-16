Name:       linux-kernel-modules
Version:    5.3.16
Release:    1
Summary:    Linux kernel modules
License:    GPL3
Prefix:     /usr
Source0:    linux-%{version}.tar.xz

%description
Linux kernel modules

%prep
%setup -n linux-%{version}

%build
make mrproper
make defconfig
%make_build
make modules

%install    
rm -rf %{buildroot}
make INSTALL_MOD_PATH=%{buildroot} modules_install

%files
/lib/modules/*

%changelog
* Mon Dec 16 2019 Chris Statzer <chris.statzer@qq.com> 5.3.16
- Kernel upgrade.

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.20.12
- Initial RPM

