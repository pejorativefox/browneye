Name:       libxres
Version:    1.2.2
Release:    1
Summary:    X-Resource extension client library
License:    GPL3
Prefix:     /usr
Source0:    libXres-%{version}.tar.xz

%description
X-Resource extension client library

%prep
%setup -q -n libXres-%{version}


%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/XRes.h
/usr/lib64/libXRes.a
/usr/lib64/libXRes.so
/usr/lib64/libXRes.so.1
/usr/lib64/libXRes.so.1.0.0
/usr/lib64/pkgconfig/xres.pc
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.2.2-1
- Version bump
