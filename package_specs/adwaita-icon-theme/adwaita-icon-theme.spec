Name:       adwaita-icon-theme
Version:    3.30.1
Release:    1
Summary:    Gnome standard icon set.
License:    LGPL
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
Gnome standard icons.

%prep
%setup

%build
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/share/icons/*
/usr/share/pkgconfig/adwaita-icon-theme.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.30.1
- Initial RPM release

