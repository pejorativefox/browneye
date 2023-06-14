Name:       efivar
Version:    38
Release:    1
Summary:     The efivar package provides tools and libraries to manipulate EFI variables.
License:    LGPL-2.1
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Tools and libraries to work with EFI variables 

%prep
%setup
sed '/prep :/a\\ttouch prep' -i src/Makefile

%build
%make_build ERRORS=

%install
rm -rf %{buildroot}
%make_install LIBDIR=/usr/lib

%files
/usr/bin/efisecdb
/usr/bin/efivar
/usr/include/efivar/
/usr/lib/libefiboot.so
/usr/lib/libefiboot.so.1
/usr/lib/libefiboot.so.1.38
/usr/lib/libefisec.so
/usr/lib/libefisec.so.1
/usr/lib/libefisec.so.1.38
/usr/lib/libefivar.so
/usr/lib/libefivar.so.1
/usr/lib/libefivar.so.1.38
/usr/lib/pkgconfig/efiboot.pc
/usr/lib/pkgconfig/efisec.pc
/usr/lib/pkgconfig/efivar.pc
/usr/share/man/man1/efisecdb.1.gz
/usr/share/man/man1/efivar.1.gz
/usr/share/man/man3/

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

