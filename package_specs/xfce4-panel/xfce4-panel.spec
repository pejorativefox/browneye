Name:       xfce4-panel
Version:    4.19.1
Release:    1
Summary:    Panel for the Xfce desktop environment
License:    GPL2
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

BuildRequires: libxfce4util
BuildRequires: garcon
BuildRequires: exo
BuildRequires: libxfce4windowing


%description
Panel for the Xfce desktop environment

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
/usr/include/
/usr/lib64/
/usr/share/
/usr/etc/xdg/xfce4/panel/default.xml

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 4.19.1
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14.0
- Initial RPM

