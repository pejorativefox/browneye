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
%make_install LIBDIR=/usr/lib64

%files
/usr/bin/efisecdb
/usr/bin/efivar
/usr/include/efivar/efiboot-creator.h
/usr/include/efivar/efiboot-loadopt.h
/usr/include/efivar/efiboot.h
/usr/include/efivar/efisec-secdb.h
/usr/include/efivar/efisec-types.h
/usr/include/efivar/efisec.h
/usr/include/efivar/efivar-dp.h
/usr/include/efivar/efivar-guids.h
/usr/include/efivar/efivar-time.h
/usr/include/efivar/efivar-types.h
/usr/include/efivar/efivar.h
/usr/lib64/libefiboot.so
/usr/lib64/libefiboot.so.1
/usr/lib64/libefiboot.so.1.38
/usr/lib64/libefisec.so
/usr/lib64/libefisec.so.1
/usr/lib64/libefisec.so.1.38
/usr/lib64/libefivar.so
/usr/lib64/libefivar.so.1
/usr/lib64/libefivar.so.1.38
/usr/lib64/pkgconfig/efiboot.pc
/usr/lib64/pkgconfig/efisec.pc
/usr/lib64/pkgconfig/efivar.pc
/usr/share/man/

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

