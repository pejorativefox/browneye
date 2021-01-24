Name:       libportal 
Version:    0.3
Release:    1
Summary:    Flatpak portal library 
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Flatpak portal library 

%prep
%setup

%build
sed -i "s/subdir('doc')/#subdir('doc')/g" meson.build
mkdir build
pushd build
meson --prefix=/usr ..
ninja all
popd

%install
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/include/libportal/
/usr/lib/libportal.so
/usr/lib/libportal.so.0
/usr/lib/libportal.so.0.0.1
/usr/lib/pkgconfig/libportal.pc

%changelog
* Tue Jan 19 2021 Chris Statzer <chris.statzer@qq.com> 0.3
- Initial RPM

