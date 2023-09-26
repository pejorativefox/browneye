Name:       pangomm
Version:    2.46.3
Release:    1
Summary:    pangomm is the official C++ interface for the Pango font layout library. 
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

BuildRequires: glibmm

%description
pangomm is the official C++ interface for the Pango font layout library. 

%prep
%setup

%build
mkdir build
pushd build
meson setup --prefix=/usr --buildtype=release ..
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/include/pangomm-1.4/
/usr/lib64/libpangomm-1.4.so
/usr/lib64/libpangomm-1.4.so.1
/usr/lib64/libpangomm-1.4.so.1.0.30
/usr/lib64/pangomm-1.4/include/pangommconfig.h
/usr/lib64/pangomm-1.4/proc/m4/convert.m4
/usr/lib64/pangomm-1.4/proc/m4/convert_pango.m4
/usr/lib64/pangomm-1.4/proc/m4/convert_pangomm.m4
/usr/lib64/pkgconfig/pangomm-1.4.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.46.3-1
- Version bump

* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.42.1
- Initial RPM

