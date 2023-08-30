Name:       qemu
Version:    8.1.0
Release:    1
Summary:    QEMU is a generic and open source machine emulator and virtualizer.
License:    GPL2
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
QEMU is a generic and open source machine emulator and virtualizer.

%prep
%setup

%build
./configure --prefix=/usr \
            --enable-kvm \
            --target-list=x86_64-softmmu,x86_64-linux-user
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/
/usr/libexec/
/usr/share/
/usr/include/
/usr/lib/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 8.1.0
- Version bump

* Thu Jun 15 2023 Chris Statzer <chris.statzer@gmail.com> 4.2.0
- Cleaned package of non-x86 and added kvm suppport.

* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 4.2.0
- Initial RPM

