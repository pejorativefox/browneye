Name:       libxcb
Version:    1.15
Release:    1
Summary:    X11 client library
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
X11 client library

%prep
%setup -q

%build 
%configure --without-doxygen
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/xcb/bigreq.h
/usr/include/xcb/composite.h
/usr/include/xcb/damage.h
/usr/include/xcb/dpms.h
/usr/include/xcb/dri2.h
/usr/include/xcb/dri3.h
/usr/include/xcb/ge.h
/usr/include/xcb/glx.h
/usr/include/xcb/present.h
/usr/include/xcb/randr.h
/usr/include/xcb/record.h
/usr/include/xcb/render.h
/usr/include/xcb/res.h
/usr/include/xcb/screensaver.h
/usr/include/xcb/shape.h
/usr/include/xcb/shm.h
/usr/include/xcb/sync.h
/usr/include/xcb/xc_misc.h
/usr/include/xcb/xcb.h
/usr/include/xcb/xcbext.h
/usr/include/xcb/xevie.h
/usr/include/xcb/xf86dri.h
/usr/include/xcb/xfixes.h
/usr/include/xcb/xinerama.h
/usr/include/xcb/xinput.h
/usr/include/xcb/xkb.h
/usr/include/xcb/xprint.h
/usr/include/xcb/xproto.h
/usr/include/xcb/xselinux.h
/usr/include/xcb/xtest.h
/usr/include/xcb/xv.h
/usr/include/xcb/xvmc.h
/usr/lib64/libxcb-composite.a
/usr/lib64/libxcb-composite.so
/usr/lib64/libxcb-composite.so.0
/usr/lib64/libxcb-composite.so.0.0.0
/usr/lib64/libxcb-damage.a
/usr/lib64/libxcb-damage.so
/usr/lib64/libxcb-damage.so.0
/usr/lib64/libxcb-damage.so.0.0.0
/usr/lib64/libxcb-dpms.a
/usr/lib64/libxcb-dpms.so
/usr/lib64/libxcb-dpms.so.0
/usr/lib64/libxcb-dpms.so.0.0.0
/usr/lib64/libxcb-dri2.a
/usr/lib64/libxcb-dri2.so
/usr/lib64/libxcb-dri2.so.0
/usr/lib64/libxcb-dri2.so.0.0.0
/usr/lib64/libxcb-dri3.a
/usr/lib64/libxcb-dri3.so
/usr/lib64/libxcb-dri3.so.0
/usr/lib64/libxcb-dri3.so.0.1.0
/usr/lib64/libxcb-glx.a
/usr/lib64/libxcb-glx.so
/usr/lib64/libxcb-glx.so.0
/usr/lib64/libxcb-glx.so.0.0.0
/usr/lib64/libxcb-present.a
/usr/lib64/libxcb-present.so
/usr/lib64/libxcb-present.so.0
/usr/lib64/libxcb-present.so.0.0.0
/usr/lib64/libxcb-randr.a
/usr/lib64/libxcb-randr.so
/usr/lib64/libxcb-randr.so.0
/usr/lib64/libxcb-randr.so.0.1.0
/usr/lib64/libxcb-record.a
/usr/lib64/libxcb-record.so
/usr/lib64/libxcb-record.so.0
/usr/lib64/libxcb-record.so.0.0.0
/usr/lib64/libxcb-render.a
/usr/lib64/libxcb-render.so
/usr/lib64/libxcb-render.so.0
/usr/lib64/libxcb-render.so.0.0.0
/usr/lib64/libxcb-res.a
/usr/lib64/libxcb-res.so
/usr/lib64/libxcb-res.so.0
/usr/lib64/libxcb-res.so.0.0.0
/usr/lib64/libxcb-screensaver.a
/usr/lib64/libxcb-screensaver.so
/usr/lib64/libxcb-screensaver.so.0
/usr/lib64/libxcb-screensaver.so.0.0.0
/usr/lib64/libxcb-shape.a
/usr/lib64/libxcb-shape.so
/usr/lib64/libxcb-shape.so.0
/usr/lib64/libxcb-shape.so.0.0.0
/usr/lib64/libxcb-shm.a
/usr/lib64/libxcb-shm.so
/usr/lib64/libxcb-shm.so.0
/usr/lib64/libxcb-shm.so.0.0.0
/usr/lib64/libxcb-sync.a
/usr/lib64/libxcb-sync.so
/usr/lib64/libxcb-sync.so.1
/usr/lib64/libxcb-sync.so.1.0.0
/usr/lib64/libxcb-xf86dri.a
/usr/lib64/libxcb-xf86dri.so
/usr/lib64/libxcb-xf86dri.so.0
/usr/lib64/libxcb-xf86dri.so.0.0.0
/usr/lib64/libxcb-xfixes.a
/usr/lib64/libxcb-xfixes.so
/usr/lib64/libxcb-xfixes.so.0
/usr/lib64/libxcb-xfixes.so.0.0.0
/usr/lib64/libxcb-xinerama.a
/usr/lib64/libxcb-xinerama.so
/usr/lib64/libxcb-xinerama.so.0
/usr/lib64/libxcb-xinerama.so.0.0.0
/usr/lib64/libxcb-xinput.a
/usr/lib64/libxcb-xinput.so
/usr/lib64/libxcb-xinput.so.0
/usr/lib64/libxcb-xinput.so.0.1.0
/usr/lib64/libxcb-xkb.a
/usr/lib64/libxcb-xkb.so
/usr/lib64/libxcb-xkb.so.1
/usr/lib64/libxcb-xkb.so.1.0.0
/usr/lib64/libxcb-xtest.a
/usr/lib64/libxcb-xtest.so
/usr/lib64/libxcb-xtest.so.0
/usr/lib64/libxcb-xtest.so.0.0.0
/usr/lib64/libxcb-xv.a
/usr/lib64/libxcb-xv.so
/usr/lib64/libxcb-xv.so.0
/usr/lib64/libxcb-xv.so.0.0.0
/usr/lib64/libxcb-xvmc.a
/usr/lib64/libxcb-xvmc.so
/usr/lib64/libxcb-xvmc.so.0
/usr/lib64/libxcb-xvmc.so.0.0.0
/usr/lib64/libxcb.a
/usr/lib64/libxcb.so
/usr/lib64/libxcb.so.1
/usr/lib64/libxcb.so.1.1.0
/usr/lib64/pkgconfig/xcb-composite.pc
/usr/lib64/pkgconfig/xcb-damage.pc
/usr/lib64/pkgconfig/xcb-dpms.pc
/usr/lib64/pkgconfig/xcb-dri2.pc
/usr/lib64/pkgconfig/xcb-dri3.pc
/usr/lib64/pkgconfig/xcb-glx.pc
/usr/lib64/pkgconfig/xcb-present.pc
/usr/lib64/pkgconfig/xcb-randr.pc
/usr/lib64/pkgconfig/xcb-record.pc
/usr/lib64/pkgconfig/xcb-render.pc
/usr/lib64/pkgconfig/xcb-res.pc
/usr/lib64/pkgconfig/xcb-screensaver.pc
/usr/lib64/pkgconfig/xcb-shape.pc
/usr/lib64/pkgconfig/xcb-shm.pc
/usr/lib64/pkgconfig/xcb-sync.pc
/usr/lib64/pkgconfig/xcb-xf86dri.pc
/usr/lib64/pkgconfig/xcb-xfixes.pc
/usr/lib64/pkgconfig/xcb-xinerama.pc
/usr/lib64/pkgconfig/xcb-xinput.pc
/usr/lib64/pkgconfig/xcb-xkb.pc
/usr/lib64/pkgconfig/xcb-xtest.pc
/usr/lib64/pkgconfig/xcb-xv.pc
/usr/lib64/pkgconfig/xcb-xvmc.pc
/usr/lib64/pkgconfig/xcb.pc
/usr/share/doc/libxcb/tutorial/index.html
/usr/share/doc/libxcb/tutorial/xcb.css
/usr/share/man/

%changelog
# let's skip this for now
