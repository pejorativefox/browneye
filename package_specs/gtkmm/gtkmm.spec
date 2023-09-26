Name:       gtkmm
Version:    3.24.8
Release:    1
Summary:    gtkmm is the official C++ interface for the popular GUI library GTK+.
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

BuildRequires: cairomm
BuildRequires: pangomm
BuildRequires: atkmm
BuildRequires: glibmm

%description
gtkmm is the official C++ interface for the popular GUI library GTK+.

%prep
%setup -q

%build
mkdir gtk-build
pushd gtk-build
meson --prefix=/usr --buildtype=release ..
ninja 
popd

%install
rm -rf %{buildroot}
pushd gtk-build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/include/gdkmm-3.0/
/usr/include/gtkmm-3.0/
/usr/lib64/gtkmm-3.0/
/usr/lib64/libgdkmm-3.0.so
/usr/lib64/libgdkmm-3.0.so.1
/usr/lib64/libgdkmm-3.0.so.1.1.0
/usr/lib64/libgtkmm-3.0.so
/usr/lib64/libgtkmm-3.0.so.1
/usr/lib64/libgtkmm-3.0.so.1.1.0
/usr/lib64/pkgconfig/gdkmm-3.0.pc
/usr/lib64/pkgconfig/gtkmm-3.0.pc
/usr/lib64/gdkmm-3.0/include/gdkmmconfig.h

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 3.24.8-1
- Version bump

* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 3.24.2-1
- Initial RPM
