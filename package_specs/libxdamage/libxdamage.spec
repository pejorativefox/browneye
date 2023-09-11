Name:       libxdamage
Version:    1.1.6
Release:    1
Summary:    X Damage Extension library
License:    GPL3
Prefix:     /usr
Source0:    libXdamage-%{version}.tar.xz

%description
X Damage Extension library

%prep
%setup -q -n libXdamage-%{version}


%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/Xdamage.h
/usr/lib64/libXdamage.a
/usr/lib64/libXdamage.so
/usr/lib64/libXdamage.so.1
/usr/lib64/libXdamage.so.1.1.0
/usr/lib64/pkgconfig/xdamage.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.1.6-1
- Version bump
