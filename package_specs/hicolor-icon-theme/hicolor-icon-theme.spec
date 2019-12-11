Name:       hicolor-icon-theme
Version:    0.17
Release:    1
Summary:    Gnome hicolor icon theme.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Gnome hicolor icon theme

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/share/icons/hicolor/index.theme

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.17
- Initial RPM

