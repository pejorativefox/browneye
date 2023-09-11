Name:       libxi
Version:    1.8.1
Release:    1
Summary:    Library for the X Input Extension.
License:    GPL3
Prefix:     /usr
Source0:    libXi-%{version}.tar.xz

%description
Library for the X Input Extension.

%prep
%setup -q -n libXi-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/XInput.h
/usr/include/X11/extensions/XInput2.h
/usr/lib64/libXi.a
/usr/lib64/libXi.so
/usr/lib64/libXi.so.6
/usr/lib64/libXi.so.6.1.0
/usr/lib64/pkgconfig/xi.pc
/usr/share/doc/libXi/encoding.xml
/usr/share/doc/libXi/inputlib.xml
/usr/share/doc/libXi/library.xml
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.8.1-1
- Version bump
