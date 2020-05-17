Name:       acpid
Version:    2.0.28
Release:    1
Summary:    The acpid (Advanced Configuration and Power Interface event daemon)
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.xz
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

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.0.28
- Initial RPM

