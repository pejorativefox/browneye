Name:       dunst
Version:    1.4.1
Release:    1
Summary:    Dunst notification daemon
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Dunst notification daemon

%prep
%setup

%build
%make_build

%install
rm -rf %{buildroot}
%make_install PREFIX=/usr

%files
/usr/bin/dunst
/usr/share/dbus-1/services/org.knopwob.dunst.service
/usr/share/dunst/dunstrc
/usr/share/man/man1/dunst.1.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.4.1
- Initial RPM

