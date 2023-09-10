Name:       xorgproto
Version:    2023.2
Release:    1
Summary:    Xorg Protocols
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Xorg Protocols

%prep
%setup -q

%build 
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/GL/glxint.h
/usr/include/GL/glxmd.h
/usr/include/GL/glxproto.h
/usr/include/GL/glxtokens.h
/usr/include/GL/internal/glcore.h
/usr/share/pkgconfig/applewmproto.pc
/usr/share/pkgconfig/bigreqsproto.pc
/usr/share/pkgconfig/compositeproto.pc
/usr/share/pkgconfig/damageproto.pc
/usr/share/pkgconfig/dmxproto.pc
/usr/share/pkgconfig/dpmsproto.pc
/usr/share/pkgconfig/dri2proto.pc
/usr/share/pkgconfig/dri3proto.pc
/usr/share/pkgconfig/fixesproto.pc
/usr/share/pkgconfig/fontsproto.pc
/usr/share/pkgconfig/glproto.pc
/usr/share/pkgconfig/inputproto.pc
/usr/share/pkgconfig/kbproto.pc
/usr/share/pkgconfig/presentproto.pc
/usr/share/pkgconfig/randrproto.pc
/usr/share/pkgconfig/recordproto.pc
/usr/share/pkgconfig/renderproto.pc
/usr/share/pkgconfig/resourceproto.pc
/usr/share/pkgconfig/scrnsaverproto.pc
/usr/share/pkgconfig/videoproto.pc
/usr/share/pkgconfig/xcmiscproto.pc
/usr/share/pkgconfig/xextproto.pc
/usr/share/pkgconfig/xf86bigfontproto.pc
/usr/share/pkgconfig/xf86dgaproto.pc
/usr/share/pkgconfig/xf86driproto.pc
/usr/share/pkgconfig/xf86vidmodeproto.pc
/usr/share/pkgconfig/xineramaproto.pc
/usr/share/pkgconfig/xproto.pc
/usr/share/pkgconfig/xwaylandproto.pc
/usr/include/X11/
/usr/share/doc/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2023.2
- Version bump
