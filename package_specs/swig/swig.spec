Name:       swig
Version:    4.0.1
Release:    1
Summary:    Simplified Wrapper and Interface Generator
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Simplified Wrapper and Interface Generator

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/ccache-swig
/usr/bin/swig
/usr/share/swig/4.0.1/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.0.1
- Initial RPM

