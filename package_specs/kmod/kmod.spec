Name:       kmod
Version:    26
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
%configure --with-xz              \
           --with-zlib
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
pushd %{buildroot}/usr/bin
for target in depmod insmod lsmod modinfo modprobe rmmod; do
  ln -sfv kmod $target
done
popd
%files
/usr/bin/kmod
/usr/bin/depmod
/usr/bin/insmod
/usr/bin/lsmod
/usr/bin/modinfo
/usr/bin/modprobe
/usr/bin/rmmod
/usr/include/libkmod.h
/usr/lib64/libkmod.so
/usr/lib64/libkmod.so.2
/usr/lib64/libkmod.so.2.3.4
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
