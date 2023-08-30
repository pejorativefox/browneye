Name:       libevent
Version:    2.1.12
Release:    1
Summary:    Provides callback functions for file descriptors.
License:    BSD
Source0:    %{name}-%{version}-stable.tar.gz
Prefix:     /usr

%description
The libevent API provides a mechanism to execute a callback function when a specific event occurs on a file descriptor.

%prep
%setup -n %{name}-%{version}-stable

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/
/usr/lib64
/usr/bin/event_rpcgen.py

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 2.1.12
- Initial RPM

