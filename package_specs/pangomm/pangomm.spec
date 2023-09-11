Name:       pangomm
Version:    2.42.1
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
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/pangomm-1.4/
/usr/share/doc/pangomm-1.4/
/usr/lib64/libpangomm-1.4.la
/usr/lib64/libpangomm-1.4.so
/usr/lib64/libpangomm-1.4.so.1
/usr/lib64/libpangomm-1.4.so.1.0.30
/usr/lib64/pangomm-1.4/include/pangommconfig.h
/usr/lib64/pangomm-1.4/proc/m4/convert.m4
/usr/lib64/pangomm-1.4/proc/m4/convert_pango.m4
/usr/lib64/pangomm-1.4/proc/m4/convert_pangomm.m4
/usr/lib64/pkgconfig/pangomm-1.4.pc
/usr/share/devhelp/books/pangomm-1.4/pangomm-1.4.devhelp2

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.42.1
- Initial RPM

