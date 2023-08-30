Name:       imlib2
Version:    1.12.0
Release:    1
Summary:    imlib2 is a general image loading and rendering library
License:    imlib2
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
imlib2 is a general image loading and rendering library

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/share/
/usr/lib64/
/usr/include/
/usr/bin/

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 1.12.0
- Initial RPM

