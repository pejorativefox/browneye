Name:       help2man
Version:    1.47.15
Release:    1
Summary:    help2man produces simple manual pages from the ‘--help’ and ‘--version’ output of other commands.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
help2man produces simple manual pages from the ‘--help’ and ‘--version’ output of other commands.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/help2man
/usr/share/info/help2man.info.gz
/usr/share/man/man1/help2man.1.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.47.15
- Initial RPM

