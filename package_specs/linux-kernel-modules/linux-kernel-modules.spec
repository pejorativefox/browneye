Name:       linux-kernel-modules
Version:    4.20.12
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    linux-4.20.12.tar.xz

%description
TODO

%prep
tar xf %{SOURCE0}

%build
pushd linux-4.20.12
make mrproper
make defconfig
make modules
popd

%install    
rm -rf %{buildroot}
pushd linux-4.20.12
make INSTALL_MOD_PATH=%{buildroot} modules_install
popd

%files
/lib/modules/*

%changelog
# let's skip this for now

