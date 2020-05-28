Name:       mono
Version:    6.8.0.123
Release:    1
Summary:    Mono open source ECMA CLI, C# and .NET implementation.
License:    MIT
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Mono open source ECMA CLI, C# and .NET implementation.

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
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 6.8.0.123-1
- Initial RPM

