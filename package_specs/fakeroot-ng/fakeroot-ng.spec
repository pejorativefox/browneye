Name:       fakeroot-ng
Version:    0.18
Release:    1
Summary:    Tool to simulate a root user for package builds.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Tool to simulate a root user for package builds.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/fakeroot-ng
/usr/share/man/man1/fakeroot-ng.1.gz

%changelog
* Fri Jun 23 2023 Chris Statzer <chris.statzer@gmail.com> 0.18
- Initial RPM

