Name:       grub
Version:    2.02
Release:    2
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build

%configure --disable-efiemu       \
           --sysconfdir=/etc      \
           --disable-efimenu      \
           --with-patform=efi     \
           --target=x86_64        \
           --enable-grub-mkfont   \
           --disable-werror
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/usr/share/bash-completion/completions
mv -v %{buildroot}/etc/bash_completion.d/grub %{buildroot}/usr/share/bash-completion/completions

%files
/etc/grub.d/*
/usr/bin/grub-*
/usr/lib64/grub/i386-pc/*
/usr/sbin/grub-*
/usr/share/bash-completion/completions/grub
/usr/share/grub/grub-mkconfig_lib
/usr/share/info/grub-dev.info.gz
/usr/share/info/grub.info.gz
/usr/share/locale/*
/usr/share/man/*

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 2.02-2
- Added UEFI support to build
