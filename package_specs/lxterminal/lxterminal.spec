Name:       lxterminal
Version:    0.3.2
Release:    1
Summary:    LXDE Terminal emulator
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
LXDE Terminal emulator.

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
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.3.2
- Initial RPM 

