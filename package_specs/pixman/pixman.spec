Name:       pixman
Version:    0.42.2
Release:    1
Summary:    Low-level image libraary
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz



%description
The Pixman package contains a library that provides low-level pixel manipulation features such as image compositing and trapezoid rasterization. 

%prep
%setup -a 0

%build
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/pixman-1/pixman-version.h
/usr/include/pixman-1/pixman.h
/usr/lib64/libpixman-1.so
/usr/lib64/libpixman-1.so.0
/usr/lib64/libpixman-1.so.0.42.2
/usr/lib64/pkgconfig/pixman-1.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.42.2
- Version bump
