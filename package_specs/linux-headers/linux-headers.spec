Name:       linux-headers
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
make INSTALL_HDR_PATH=dest headers_install
find dest/include \( -name .install -o -name ..install.cmd \) -delete
popd

%install    
rm -rf %{buildroot}
pushd linux-4.20.12
mkdir -pv %{buildroot}/usr/include
cp -rv dest/include/* %{buildroot}/usr/include
popd

%files
/usr/include/*

%changelog
# let's skip this for now

