Name:       libpciaccess
Version:    0.17
Release:    1
Summary:    Generic PCI access library.
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
Generic PCI access library.

%prep
%setup -q

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/pciaccess.h
/usr/lib64/libpciaccess.a
/usr/lib64/libpciaccess.so
/usr/lib64/libpciaccess.so.0
/usr/lib64/libpciaccess.so.0.11.1
/usr/lib64/pkgconfig/pciaccess.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.17-1
- Version bump
