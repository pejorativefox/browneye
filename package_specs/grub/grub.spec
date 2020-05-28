Name:       grub
Version:    2.02
Release:    1
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
/usr/bin/grub-editenv
/usr/bin/grub-file
/usr/bin/grub-fstest
/usr/bin/grub-glue-efi
/usr/bin/grub-kbdcomp
/usr/bin/grub-menulst2cfg
/usr/bin/grub-mkfont
/usr/bin/grub-mkimage
/usr/bin/grub-mklayout
/usr/bin/grub-mknetdir
/usr/bin/grub-mkpasswd-pbkdf2
/usr/bin/grub-mkrelpath
/usr/bin/grub-mkrescue
/usr/bin/grub-mkstandalone
/usr/bin/grub-mount
/usr/bin/grub-render-label
/usr/bin/grub-script-check
/usr/bin/grub-syslinux2cfg
/usr/lib64/grub/i386-pc/*
/usr/sbin/grub-bios-setup
/usr/sbin/grub-install
/usr/sbin/grub-macbless
/usr/sbin/grub-mkconfig
/usr/sbin/grub-ofpathname
/usr/sbin/grub-probe
/usr/sbin/grub-reboot
/usr/sbin/grub-set-default
/usr/sbin/grub-sparc64-setup
/usr/share/bash-completion/completions/grub
/usr/share/grub/grub-mkconfig_lib
/usr/share/info/grub-dev.info.gz
/usr/share/info/grub.info.gz
/usr/share/locale/*
/usr/share/man/*

%changelog
# let's skip this for now
