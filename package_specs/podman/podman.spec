Name:       podman
Version:    4.5.1
Release:    1
Summary:    A tool for managing OCI containers and pods
License:    Apache2
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Podman (the POD MANager) is a tool for managing containers and images, volumes mounted into those containers, and pods made from groups of containers.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files

%changelog
* Sun Jun 18 2023 Chris Statzer <chris.statzer@gmail.com> 4.5.1
- Initial RPM

