Name:       linux-headers
Version:    5.3.16
Release:    1
Summary:    Linux kernel headers
License:    GPL3
Prefix:     /usr
Source0:    linux-%{version}.tar.xz

%description
Linux kernel headers

%prep
%setup -n linux-%{version}

%build
make mrproper
make INSTALL_HDR_PATH=dest headers_install
find dest/include \( -name .install -o -name ..install.cmd \) -delete

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/usr/include
cp -rv dest/include/* %{buildroot}/usr/include

%files
/usr/include/*

%changelog
* Mon Dec 16 2019 Chris Statzer <chris.statzer@qq.com> 5.3.16
- Kernel upgrade.

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.20.12
- Initial RPM

