Name:       libxcomposite
Version:    0.4.6
Release:    1
Summary:    Xorg composite ext library
License:    GPL3
Prefix:     /usr
Source0:    libXcomposite-%{version}.tar.xz

BuildRequires: libxfixes

%description
Xlib-based client library for the Composite extension to the X11 protocol.

%prep
%setup -q -n libXcomposite-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/Xcomposite.h
/usr/lib64/libXcomposite.a
/usr/lib64/libXcomposite.so
/usr/lib64/libXcomposite.so.1
/usr/lib64/libXcomposite.so.1.0.0
/usr/lib64/pkgconfig/xcomposite.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.4.6-1
- Version bump
