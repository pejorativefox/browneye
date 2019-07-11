Name:       elfutils
Version:    0.176
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install -C libelf
rm -vf %{buildroot}%{_infodir}/dir*
mkdir %{buildroot}/usr/lib64/pkgconfig/
install -vm644 config/libelf.pc %{buildroot}/usr/lib64/pkgconfig/

%files
/usr/include/elfutils/elf-knowledge.h
/usr/include/gelf.h
/usr/include/libelf.h
/usr/include/nlist.h
/usr/lib64/libelf-0.176.so
/usr/lib64/libelf.a
/usr/lib64/libelf.so
/usr/lib64/libelf.so.1
/usr/lib64/pkgconfig/libelf.pc

%changelog
# let's skip this for now
