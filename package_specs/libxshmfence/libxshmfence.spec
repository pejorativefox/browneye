Name:       libxshmfence
Version:    1.3
Release:    1
Summary:    X SyncFence library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

%description
This library offers a CPU-based synchronization primitive compatible with the X SyncFence

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
/usr/include/X11/xshmfence.h
/usr/lib64/libxshmfence.a
/usr/lib64/libxshmfence.so
/usr/lib64/libxshmfence.so.1
/usr/lib64/libxshmfence.so.1.0.0
/usr/lib64/pkgconfig/xshmfence.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.3-1
- Version bump
