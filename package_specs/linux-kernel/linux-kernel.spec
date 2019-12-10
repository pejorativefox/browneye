Name:       linux-kernel
Version:    4.20.12
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    linux-4.20.12.tar.xz

%description
TODO

%prep
rm -rf %{buildroot}
tar xf %{SOURCE0}

%build
pushd linux-4.20.12
make mrproper
make defconfig
%make_build
popd

%install    
pushd linux-4.20.12
mkdir -pv %{buildroot}/boot
%make_install INSTALL_PATH=%{buildroot}/boot
popd

%files
/boot/System.map
/boot/vmlinuz

%changelog
# let's skip this for now



