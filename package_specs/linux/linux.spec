Name:       linux
Version:    6.4.13
Release:    1
Summary:    Linux
License:    GPL3
Prefix:     /usr
Source0:    linux-%{version}.tar.xz
Source1:    linux-%{version}.config

%description
Linux

%prep
%setup -q -n linux-%{version}

%build
make mrproper
cp -v %{SOURCE1} ./.config
#%make_build
make -j20
make -j14 modules

%install    
# kernel
mkdir -pv %{buildroot}/boot
%make_install INSTALL_PATH=%{buildroot}/boot
mv %{buildroot}/boot/vmlinuz %{buildroot}/boot/vmlinuz-%{version}

# headers 
make INSTALL_HDR_PATH=dest headers_install
find dest/include \( -name .install -o -name ..install.cmd \) -delete
mkdir -pv %{buildroot}/usr/include
cp -rv dest/include/* %{buildroot}/usr/include

# modules
make INSTALL_MOD_PATH=%{buildroot} modules_install

%package kernel
Summary: Linux Kernel
%description kernel
Linux kernel

%files kernel
/boot/System.map
/boot/vmlinuz-%{version}

%package headers
Summary: Linux kernel headers
%description headers
Linux kernel headers

%files headers
/usr/include/*

%package modules
Summary: Linux kernel modules
%description modules
Linux kernel modules

%files modules
/lib/modules/*

%post modules
depmod

%changelog
* Wed May 27 2020 Chris Statzer <chris.statzer@qq.com> 5.6.14-1
- Upgraded kernel to current stable

* Sat May 16 2020 Chris Statzer <chris.statzer@qq.com> 5.3.16-2
- Fixed vmlinuz filenames to include version so they can be auto
  added by grubmkconfig.

* Mon Dec 16 2019 Chris Statzer <chris.statzer@qq.com> 5.3.16
- Kernel upgrade

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.20.12
- Initial RPM
