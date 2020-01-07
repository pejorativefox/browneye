Name:       bdftopcf
Version:    1.1
Release:    1
Summary:    bdftopcf font conversion
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
bdftopcf font conversion

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/bdftopcf
/usr/share/man/man1/bdftopcf.1.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.1
- Initial RPM

