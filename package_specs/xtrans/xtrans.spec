Name:       xtrans
Version:    1.5.0
Release:    1
Summary:    X Window System Protocols Transport layer
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

%description
X Window System Protocols Transport laye

%prep
%setup -q

%build
%configure ICE_LIBS=-lpthread
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/Xtrans/Xtrans.c
/usr/include/X11/Xtrans/Xtrans.h
/usr/include/X11/Xtrans/Xtransint.h
/usr/include/X11/Xtrans/Xtranslcl.c
/usr/include/X11/Xtrans/Xtranssock.c
/usr/include/X11/Xtrans/Xtransutil.c
/usr/include/X11/Xtrans/transport.c
/usr/share/aclocal/xtrans.m4
/usr/share/doc/xtrans/xtrans.xml
/usr/share/pkgconfig/xtrans.pc

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.5.0-1
- Version bump
