Name:       libx11
Version:    1.8.6
Release:    1
Summary:    X11 protocol library
License:    GPL3
Prefix:     /usr
Source0:    libX11-%{version}.tar.xz

%description
X Window System protocol client library 

%prep
%setup -q -n libX11-%{version}


%build
%configure ICE_LIBS=-lpthread
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/ImUtil.h
/usr/include/X11/XKBlib.h
/usr/include/X11/Xcms.h
/usr/include/X11/Xlib-xcb.h
/usr/include/X11/Xlib.h
/usr/include/X11/XlibConf.h
/usr/include/X11/Xlibint.h
/usr/include/X11/Xlocale.h
/usr/include/X11/Xregion.h
/usr/include/X11/Xresource.h
/usr/include/X11/Xutil.h
/usr/include/X11/cursorfont.h
/usr/include/X11/extensions/XKBgeom.h
/usr/lib64/libX11-xcb.a
/usr/lib64/libX11-xcb.so
/usr/lib64/libX11-xcb.so.1
/usr/lib64/libX11-xcb.so.1.0.0
/usr/lib64/libX11.a
/usr/lib64/libX11.so
/usr/lib64/libX11.so.6
/usr/lib64/libX11.so.6.4.0
/usr/lib64/pkgconfig/x11-xcb.pc
/usr/lib64/pkgconfig/x11.pc
/usr/share/X11/XErrorDB
/usr/share/X11/Xcms.txt
/usr/share/X11/locale/
/usr/share/doc/libX11/
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.8.6-1
- Version bump
