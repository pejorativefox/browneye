Name:       elfutils
Version:    0.189
Release:    1
Summary:    ELF file handling library
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Libelf is a library for handling ELF (Executable and Linkable Format) files. 

%prep
%setup -q

%build
%configure  --disable-debuginfod         \
            --enable-libdebuginfod=dummy
%make_build

%install
rm -rf %{buildroot}
%make_install -C libelf
rm -vf %{buildroot}%{_infodir}/dir*
mkdir %{buildroot}/usr/lib64/pkgconfig/
install -vm644 config/libelf.pc %{buildroot}/usr/lib64/pkgconfig/
rm %{buildroot}/usr/lib64/libelf.a

%files
/usr/include/elfutils/elf-knowledge.h
/usr/include/gelf.h
/usr/include/libelf.h
/usr/include/nlist.h
/usr/lib64/libelf-%{version}.so
/usr/lib64/libelf.so
/usr/lib64/libelf.so.1
/usr/lib64/pkgconfig/libelf.pc

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 0.189-1
- Version bump
