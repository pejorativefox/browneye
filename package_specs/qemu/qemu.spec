Name:       qemu
Version:    4.2.0
Release:    2
Summary:    QEMU is a generic and open source machine emulator and virtualizer.
License:    GPL2
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
QEMU is a generic and open source machine emulator and virtualizer.

%prep
%setup

%build
./configure --prefix=/usr \
            --enable-kvm \
            --target-list=x86_64-softmmu,x86_64-linux-user
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/elf2dmp
/usr/bin/ivshmem-client
/usr/bin/ivshmem-server
/usr/bin/qemu-edid
/usr/bin/qemu-ga
/usr/bin/qemu-img
/usr/bin/qemu-io
/usr/bin/qemu-keymap
/usr/bin/qemu-nbd
/usr/bin/qemu-pr-helper
/usr/bin/qemu-system-x86_64
/usr/bin/qemu-x86_64
/usr/bin/virtfs-proxy-helper
/usr/libexec/qemu-bridge-helper
/usr/share/

%changelog
* Thu Jun 15 2023 Chris Statzer <chris.statzer@gmail.com> 4.2.0
- Cleaned package of non-x86 and added kvm suppport.

* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 4.2.0
- Initial RPM

