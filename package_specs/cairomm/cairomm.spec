Name:       cairomm
Version:    1.12.2
Release:    1
Summary:    The Cairomm package provides a C++ interface to Cairo. 
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

BuildRequires: libsigc++

%description
The Cairomm package provides a C++ interface to Cairo. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/cairomm-1.0/
/usr/lib64/cairomm-1.0/include/cairommconfig.h
/usr/lib64/libcairomm-1.0.so
/usr/lib64/libcairomm-1.0.so.1
/usr/lib64/libcairomm-1.0.so.1.4.0
/usr/lib64/pkgconfig/cairomm-1.0.pc
/usr/lib64/pkgconfig/cairomm-ft-1.0.pc
/usr/lib64/pkgconfig/cairomm-pdf-1.0.pc
/usr/lib64/pkgconfig/cairomm-png-1.0.pc
/usr/lib64/pkgconfig/cairomm-ps-1.0.pc
/usr/lib64/pkgconfig/cairomm-svg-1.0.pc
/usr/lib64/pkgconfig/cairomm-xlib-1.0.pc
/usr/lib64/pkgconfig/cairomm-xlib-xrender-1.0.pc
/usr/share/devhelp/books/cairomm-1.0/cairomm-1.0.devhelp2
/usr/share/doc/cairomm-1.0/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 1.12.2
- Initial RPM

