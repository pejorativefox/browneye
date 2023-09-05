Name:       kmod
Version:    30
Release:    1
Summary:    Kernel module utilities
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The Kmod package contains libraries and utilities for loading kernel modules 

%prep
%setup -q

%build
%configure  --with-openssl         \
            --with-xz              \
            --with-zstd            \
            --with-zlib
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

mkdir -pv %{buildroot}/usr/sbin

for target in depmod insmod modinfo modprobe rmmod; do
  ln -sfv ../bin/kmod %{buildroot}/usr/sbin/$target
done

ln -sfv kmod %{buildroot}/usr/bin/lsmod

%files
/usr/bin/kmod
/usr/bin/lsmod
/usr/sbin/depmod
/usr/sbin/insmod
/usr/sbin/modinfo
/usr/sbin/modprobe
/usr/sbin/rmmod
/usr/include/libkmod.h
/usr/lib64/libkmod.so
/usr/lib64/libkmod.so.2
/usr/lib64/libkmod.so.2.4.0
/usr/lib64/pkgconfig/libkmod.pc
/usr/share/bash-completion/completions/kmod
/usr/share/man/man5/depmod.d.5.gz
/usr/share/man/man5/modprobe.d.5.gz
/usr/share/man/man5/modules.dep.5.gz
/usr/share/man/man5/modules.dep.bin.5.gz
/usr/share/man/man8/depmod.8.gz
/usr/share/man/man8/insmod.8.gz
/usr/share/man/man8/kmod.8.gz
/usr/share/man/man8/lsmod.8.gz
/usr/share/man/man8/modinfo.8.gz
/usr/share/man/man8/modprobe.8.gz
/usr/share/man/man8/rmmod.8.gz


%changelog
# let's skip this for now
