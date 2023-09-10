Name:       libxmu
Version:    1.1.4
Release:    1
Summary:    Xlib misc utilities
License:    GPL3
Prefix:     /usr
Source0:    libXmu-%{version}.tar.xz

BuildRequires: libxt

%description
This library contains miscellaneous utilities and is not part of the Xlib standard. 

%prep
%setup -q -n libXmu-%{version}

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/Xmu/Atoms.h
/usr/include/X11/Xmu/CharSet.h
/usr/include/X11/Xmu/CloseHook.h
/usr/include/X11/Xmu/Converters.h
/usr/include/X11/Xmu/CurUtil.h
/usr/include/X11/Xmu/CvtCache.h
/usr/include/X11/Xmu/DisplayQue.h
/usr/include/X11/Xmu/Drawing.h
/usr/include/X11/Xmu/Editres.h
/usr/include/X11/Xmu/EditresP.h
/usr/include/X11/Xmu/Error.h
/usr/include/X11/Xmu/ExtAgent.h
/usr/include/X11/Xmu/Initer.h
/usr/include/X11/Xmu/Lookup.h
/usr/include/X11/Xmu/Misc.h
/usr/include/X11/Xmu/StdCmap.h
/usr/include/X11/Xmu/StdSel.h
/usr/include/X11/Xmu/SysUtil.h
/usr/include/X11/Xmu/WhitePoint.h
/usr/include/X11/Xmu/WidgetNode.h
/usr/include/X11/Xmu/WinUtil.h
/usr/include/X11/Xmu/Xct.h
/usr/include/X11/Xmu/Xmu.h
/usr/lib64/libXmu.a
/usr/lib64/libXmu.so
/usr/lib64/libXmu.so.6
/usr/lib64/libXmu.so.6.2.0
/usr/lib64/libXmuu.a
/usr/lib64/libXmuu.so
/usr/lib64/libXmuu.so.1
/usr/lib64/libXmuu.so.1.0.0
/usr/lib64/pkgconfig/xmu.pc
/usr/lib64/pkgconfig/xmuu.pc
/usr/share/doc/libXmu/Xmu.xml
/usr/share/doc/libXmu/xlogo.svg

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.1.4-1
- Version bump
