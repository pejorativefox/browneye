Name:       dracut
Version:    050
Release:    1
Summary:    dracut is an event driven initramfs infrastructure.
License:    GPL2
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description


%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/dracut
/usr/bin/dracut-catimages
/usr/bin/lsinitrd
/usr/bin/mkinitrd
/usr/etc/dracut.conf
/usr/lib/kernel/install.d/50-dracut.install
/usr/lib/kernel/install.d/51-dracut-rescue.install
/usr/lib64/dracut/*
/usr/share/bash-completion/completions/dracut
/usr/share/bash-completion/completions/lsinitrd
/usr/share/man/*
/usr/share/pkgconfig/dracut.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 050
- Initial RPM

