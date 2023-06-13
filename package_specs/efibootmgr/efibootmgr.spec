Name:       efibootmgr
Version:    18
Release:    1
Summary:    The efibootmgr package provides tools and libraries to manipulate EFI variables.
License:    GPL-2.0
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
This is efibootmgr, a Linux user-space application to modify the Intel Extensible Firmware Interface (EFI) Boot Manager. This application can create and destroy boot entries, change the boot order, change the next running boot option, and more.

%prep
%setup

%build
make EFIDIR=LFS EFI_LOADER=grubx64.efi

%install
rm -rf %{buildroot}
%make_install EFIDIR=LFS

%files
/usr/sbin/efibootdump
/usr/sbin/efibootmgr
/usr/share/man/man8/efibootdump.8.gz
/usr/share/man/man8/efibootmgr.8.gz

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 18-1
- Initial RPM

