Name:       linux-firmware
Version:    20230515
Release:    1
Summary:    Firmware files for the linux kernel.
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Firmware files for the linux kernel.

%prep
%setup

%build

%install
rm -rf %{buildroot}
mkdir -pv %{buildroot}/lib/firmware
cp iwlwifi* %{buildroot}/lib/firmware
cp -r mediatek %{buildroot}/lib/firmware
cp -r rtlwifi/ %{buildroot}/lib/firmware

%files
/lib/firmware/

%changelog
* Thu Jun 15 2023 Chris Statzer <chris.statzer@gmail.com> 20230515
- Update of linux firmwares alongside to newest stable kernel.

* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 20200421
- Initial RPM, added iwlwifi firmwares

