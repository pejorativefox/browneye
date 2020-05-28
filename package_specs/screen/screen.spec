Name:       screen
Version:    4.8.0
Release:    1
Summary:    Screen is a full-screen window manager that multiplexes a physical terminal between several processes
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Screen is a full-screen window manager that multiplexes a physical terminal between several processes

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/info/dir

%files
/usr/bin/screen
/usr/bin/screen-4.8.0
/usr/share/info/screen.info.gz
/usr/share/man/man1/screen.1.gz
/usr/share/screen/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.8.0
- Initial RPM

