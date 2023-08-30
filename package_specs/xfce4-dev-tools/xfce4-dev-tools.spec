Name:       xfce4-dev-tools
Version:    4.19.0
Release:    1
Summary:    Collection of tools and macros for Xfce developers
License:    LGPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
The Xfce development tools are a collection of tools and macros for Xfce developers and people that want to build Xfce from Git In addition it contains the Xfce developer's handbook.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/
/usr/share/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.19.0
- Initial RPM

