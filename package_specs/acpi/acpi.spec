Name:       acpi
Version:    1.7
Release:    1
Summary:    Client for battery, power, and thermal readings
License:    GPL2
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Client for battery, power, and thermal readings

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/acpi
/usr/share/man/man1/acpi.1.gz

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 1.7-1
- Initial RPM

