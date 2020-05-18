Name:       acpid
Version:    2.0.28
Release:    3
Summary:    The acpid (Advanced Configuration and Power Interface event daemon)
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.xz
Source1:    lidclose
Source2:    brightnessup
Source3:    brightnessdown
Source4:    acpid.conf
Prefix:     /usr

%description
The acpid (Advanced Configuration and Power Interface event daemon)

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

mkdir -pv %{buildroot}/etc/acpi/events
cp %{SOURCE1} %{buildroot}/etc/acpi/events
cp %{SOURCE2} %{buildroot}/etc/acpi/events
cp %{SOURCE3} %{buildroot}/etc/acpi/events

mkdir -pv %{buildroot}/etc/finit.d/available
cp %{SOURCE4} %{buildroot}/etc/finit.d/available/

%files
/usr/bin/acpi_listen
/usr/sbin/acpid
/usr/sbin/kacpimon
/usr/share/doc/acpid/COPYING
/usr/share/doc/acpid/Changelog
/usr/share/doc/acpid/README
/usr/share/doc/acpid/TESTPLAN
/usr/share/doc/acpid/TODO
/usr/share/man/man8/acpi_listen.8.gz
/usr/share/man/man8/acpid.8.gz
/usr/share/man/man8/kacpimon.8.gz
/etc/acpi/events/brightnessdown
/etc/acpi/events/brightnessup
/etc/acpi/events/lidclose
/etc/finit.d/available/acpid.conf

%changelog
* Mon May 18 2020 Chris Statzer <chris.statzer@qq.com> 2.0.28-3
- Added basic events and finit service

* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.0.28-1
- Initial RPM

