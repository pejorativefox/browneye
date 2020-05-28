Name:       linux-firmware
Version:    20200421
Release:    1
Summary:    Firmware files for the linux kernel.
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.gz
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

%files
/lib/firmware/iwlwifi*

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 20200421
- Initial RPM, added iwlwifi firmwares

