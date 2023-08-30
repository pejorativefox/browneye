Name:       libxfce4windowing
Version:    4.19.2
Release:    1
Summary:    Abstraction library for windowing concepts
License:    LGPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Libxfce4windowing is an abstraction library that attempts to present windowing concepts (screens, toplevel windows, workspaces, etc.) in a windowing-system-independent manner.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/share/
/usr/include/
/usr/lib64/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.19.2
- Initial RPM

