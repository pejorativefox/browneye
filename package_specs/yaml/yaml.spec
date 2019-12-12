Name:       yaml
Version:    0.2.1
Release:    1
Summary:    YAML Ain't Markup Language
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
YAML Ain't Markup Language

%prep
%setup

%build
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/yaml.h
/usr/lib64/libyaml-0.so.2
/usr/lib64/libyaml-0.so.2.0.5
/usr/lib64/libyaml.la
/usr/lib64/libyaml.so
/usr/lib64/pkgconfig/yaml-0.1.pc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.2.1
- Initial RPM

