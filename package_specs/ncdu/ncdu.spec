Name:       ncdu
Version:    1.14.1
Release:    1
Summary:    Ncdu is a disk usage analyzer with an ncurses interface.
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Ncdu is a disk usage analyzer with an ncurses interface.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/ncdu
/usr/share/man/man1/ncdu.1.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.14.1
- Initial RPM

