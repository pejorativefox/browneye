Name:       gtk-xfce-engine
Version:    3.2.0
Release:    1
Summary:    Xfce Gtk engine
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Xfce Gtk engine

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
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.2.0
- Initial RPM

