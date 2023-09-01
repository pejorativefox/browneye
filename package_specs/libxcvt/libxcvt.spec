Name:       libxcvt
Version:    0.1.2
Release:    1
Summary:    TODO
License:    TODO
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

Provides: pkgconfig(libxcvt)

%description
TODO

%prep
%setup

%build
mkdir build
pushd build

meson --prefix=/usr ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/bin/
/usr/lib/
/usr/share/
/usr/include/

%changelog
* Thu Aug 31 2023 Chris Statzer <chris.statzer@gmail.com> 0.1.2
- Initial RPM

