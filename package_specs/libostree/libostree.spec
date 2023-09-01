Name:       libostree
Version:    2019.6
Release:    1
Summary:    Operating system and container binary deployment and upgrades
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Operating system and container binary deployment and upgrades

%prep
%setup

%build
%configure --disable-gtk-doc --disable-man
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/ostree
/usr/bin/rofiles-fuse
/usr/etc/grub.d/15_ostree
/usr/include/ostree-1/*
/usr/lib/ostree/ostree-prepare-root
/usr/lib64/girepository-1.0/OSTree-1.0.typelib
/usr/lib64/libostree-1.so
/usr/lib64/libostree-1.so.1
/usr/lib64/libostree-1.so.1.0.0
/usr/lib64/pkgconfig/ostree-1.pc
/usr/libexec/libostree/grub2-15_ostree
/usr/libexec/libostree/ostree-trivial-httpd
/usr/share/bash-completion/completions/ostree
/usr/share/gir-1.0/OSTree-1.0.gir
/usr/share/ostree/trusted.gpg.d/README-gpg

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2019.06
- Initial RPM

