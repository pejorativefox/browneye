Name:       libxext
Version:    1.3.5
Release:    1
Summary:    Library for common extensions to the X11 protocol
License:    GPL3
Prefix:     /usr
Source0:    libXext-%{version}.tar.xz



%description
Library for common extensions to the X11 protocol

%prep
%setup -q -n libXext-%{version}


%build
%configure ICE_LIBS=-lpthread
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/extensions/MITMisc.h
/usr/include/X11/extensions/XEVI.h
/usr/include/X11/extensions/XLbx.h
/usr/include/X11/extensions/XShm.h
/usr/include/X11/extensions/Xag.h
/usr/include/X11/extensions/Xcup.h
/usr/include/X11/extensions/Xdbe.h
/usr/include/X11/extensions/Xext.h
/usr/include/X11/extensions/Xge.h
/usr/include/X11/extensions/dpms.h
/usr/include/X11/extensions/extutil.h
/usr/include/X11/extensions/multibuf.h
/usr/include/X11/extensions/security.h
/usr/include/X11/extensions/shape.h
/usr/include/X11/extensions/sync.h
/usr/include/X11/extensions/xtestext1.h
/usr/lib64/libXext.a
/usr/lib64/libXext.so
/usr/lib64/libXext.so.6
/usr/lib64/libXext.so.6.4.0
/usr/lib64/pkgconfig/xext.pc
/usr/share/doc/
/usr/share/man/


%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.3.5-1
- Version bump
