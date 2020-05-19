Name:       qemu
Version:    4.2.0
Release:    1
Summary:    QEMU is a generic and open source machine emulator and virtualizer.
License:    GPL2
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
QEMU is a generic and open source machine emulator and virtualizer.

%prep
%setup

%build
./configure --prefix=/usr
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/elf2dmp
/usr/bin/ivshmem-client
/usr/bin/ivshmem-server
/usr/bin/qemu-aarch64
/usr/bin/qemu-aarch64_be
/usr/bin/qemu-alpha
/usr/bin/qemu-arm
/usr/bin/qemu-armeb
/usr/bin/qemu-cris
/usr/bin/qemu-edid
/usr/bin/qemu-ga
/usr/bin/qemu-hppa
/usr/bin/qemu-i386
/usr/bin/qemu-img
/usr/bin/qemu-io
/usr/bin/qemu-keymap
/usr/bin/qemu-m68k
/usr/bin/qemu-microblaze
/usr/bin/qemu-microblazeel
/usr/bin/qemu-mips
/usr/bin/qemu-mips64
/usr/bin/qemu-mips64el
/usr/bin/qemu-mipsel
/usr/bin/qemu-mipsn32
/usr/bin/qemu-mipsn32el
/usr/bin/qemu-nbd
/usr/bin/qemu-nios2
/usr/bin/qemu-or1k
/usr/bin/qemu-ppc
/usr/bin/qemu-ppc64
/usr/bin/qemu-ppc64abi32
/usr/bin/qemu-ppc64le
/usr/bin/qemu-pr-helper
/usr/bin/qemu-riscv32
/usr/bin/qemu-riscv64
/usr/bin/qemu-s390x
/usr/bin/qemu-sh4
/usr/bin/qemu-sh4eb
/usr/bin/qemu-sparc
/usr/bin/qemu-sparc32plus
/usr/bin/qemu-sparc64
/usr/bin/qemu-system-aarch64
/usr/bin/qemu-system-alpha
/usr/bin/qemu-system-arm
/usr/bin/qemu-system-cris
/usr/bin/qemu-system-hppa
/usr/bin/qemu-system-i386
/usr/bin/qemu-system-lm32
/usr/bin/qemu-system-m68k
/usr/bin/qemu-system-microblaze
/usr/bin/qemu-system-microblazeel
/usr/bin/qemu-system-mips
/usr/bin/qemu-system-mips64
/usr/bin/qemu-system-mips64el
/usr/bin/qemu-system-mipsel
/usr/bin/qemu-system-moxie
/usr/bin/qemu-system-nios2
/usr/bin/qemu-system-or1k
/usr/bin/qemu-system-ppc
/usr/bin/qemu-system-ppc64
/usr/bin/qemu-system-riscv32
/usr/bin/qemu-system-riscv64
/usr/bin/qemu-system-s390x
/usr/bin/qemu-system-sh4
/usr/bin/qemu-system-sh4eb
/usr/bin/qemu-system-sparc
/usr/bin/qemu-system-sparc64
/usr/bin/qemu-system-tricore
/usr/bin/qemu-system-unicore32
/usr/bin/qemu-system-x86_64
/usr/bin/qemu-system-xtensa
/usr/bin/qemu-system-xtensaeb
/usr/bin/qemu-tilegx
/usr/bin/qemu-x86_64
/usr/bin/qemu-xtensa
/usr/bin/qemu-xtensaeb
/usr/bin/virtfs-proxy-helper
/usr/libexec/qemu-bridge-helper
/usr/share/applications/qemu.desktop
/usr/share/icons/
/usr/share/locale/
/usr/share/qemu/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 4.2.0
- Initial RPM

