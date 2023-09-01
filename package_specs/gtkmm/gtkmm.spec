Name:       gtkmm
Version:    3.24.2
Release:    1
Summary:    gtkmm is the official C++ interface for the popular GUI library GTK+.
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
gtkmm is the official C++ interface for the popular GUI library GTK+.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

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
/usr/share/devhelp/books/gtkmm-3.0/gtkmm-3.0.devhelp2
/usr/share/doc/gtkmm-3.0/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 3.24.2
- Initial RPM
