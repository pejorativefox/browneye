Name:       libsm
Version:    1.2.4
Release:    1
Summary:    X Session Management Library
License:    GPL3
Prefix:     /usr
Source0:    libSM-%{version}.tar.xz

BuildRequires: libice

%description
X Session Management Library

%prep
%setup -q -n libSM-%{version}

%build
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/SM/SM.h
/usr/include/X11/SM/SMlib.h
/usr/include/X11/SM/SMproto.h
/usr/lib64/libSM.a
/usr/lib64/libSM.so
/usr/lib64/libSM.so.6
/usr/lib64/libSM.so.6.0.1
/usr/lib64/pkgconfig/sm.pc
/usr/share/doc/libSM/SMlib.xml
/usr/share/doc/libSM/xsmp.xml

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.2.4-1
- Version bump
