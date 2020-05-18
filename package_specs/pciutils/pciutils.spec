Name:       pciutils
Version:    3.6.4
Release:    1
Summary:    The PCI Utilities
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The PCI Utilities

%prep
%setup

%build
%make_build PREFIX=/usr

%install
rm -rf %{buildroot}
%make_install PREFIX=/usr

%files
/usr/sbin/lspci
/usr/sbin/setpci
/usr/sbin/update-pciids
/usr/share/man/man5/pci.ids.5.gz
/usr/share/man/man7/pcilib.7.gz
/usr/share/man/man8/lspci.8.gz
/usr/share/man/man8/setpci.8.gz
/usr/share/man/man8/update-pciids.8.gz
/usr/share/pci.ids.gz

%changelog
* Mon May 18 2020 Chris Statzer <chris.statzer@qq.com> 3.6.4
- Initial RPM

