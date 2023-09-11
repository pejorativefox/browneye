Name:       libxtst
Version:    1.2.4
Release:    1
Summary:    Xlib-based library for XTEST & RECORD
License:    GPL3
Prefix:     /usr
Source0:    libXtst-%{version}.tar.xz

BuildRequires: libxi

%description
Xlib-based library for XTEST & RECORD

%prep
%setup -q -n libXtst-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/XTest.h
/usr/include/X11/extensions/record.h
/usr/lib64/libXtst.a
/usr/lib64/libXtst.so
/usr/lib64/libXtst.so.6
/usr/lib64/libXtst.so.6.1.0
/usr/lib64/pkgconfig/xtst.pc
/usr/share/doc/libXtst/recordlib.xml
/usr/share/doc/libXtst/xtestlib.xml
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.2.4-1
- Version bump
