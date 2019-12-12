Name:       wmname
Version:    0.1
Release:    1
Summary:    wmname prints/sets the window manager name
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
wmname prints/sets the window manager name

%prep
%setup

%build
%make_build

%install
rm -rf %{buildroot}
%make_install DESTDIR=%{buildroot} PREFIX=/usr

%files
/usr/bin/wmname

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.1
- Initial RPM

