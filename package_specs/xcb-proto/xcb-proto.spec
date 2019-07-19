Name:       xcb-proto
Version:    1.13
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build 
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
   /usr/lib/python2.7/site-packages/xcbgen/__init__.py
   /usr/lib/python2.7/site-packages/xcbgen/__init__.pyc
   /usr/lib/python2.7/site-packages/xcbgen/__init__.pyo
   /usr/lib/python2.7/site-packages/xcbgen/align.py
   /usr/lib/python2.7/site-packages/xcbgen/align.pyc
   /usr/lib/python2.7/site-packages/xcbgen/align.pyo
   /usr/lib/python2.7/site-packages/xcbgen/error.py
   /usr/lib/python2.7/site-packages/xcbgen/error.pyc
   /usr/lib/python2.7/site-packages/xcbgen/error.pyo
   /usr/lib/python2.7/site-packages/xcbgen/expr.py
   /usr/lib/python2.7/site-packages/xcbgen/expr.pyc
   /usr/lib/python2.7/site-packages/xcbgen/expr.pyo
   /usr/lib/python2.7/site-packages/xcbgen/matcher.py
   /usr/lib/python2.7/site-packages/xcbgen/matcher.pyc
   /usr/lib/python2.7/site-packages/xcbgen/matcher.pyo
   /usr/lib/python2.7/site-packages/xcbgen/state.py
   /usr/lib/python2.7/site-packages/xcbgen/state.pyc
   /usr/lib/python2.7/site-packages/xcbgen/state.pyo
   /usr/lib/python2.7/site-packages/xcbgen/xtypes.py
   /usr/lib/python2.7/site-packages/xcbgen/xtypes.pyc
   /usr/lib/python2.7/site-packages/xcbgen/xtypes.pyo
/usr/lib64/pkgconfig/xcb-proto.pc
/usr/share/xcb/bigreq.xml
/usr/share/xcb/composite.xml
/usr/share/xcb/damage.xml
/usr/share/xcb/dpms.xml
/usr/share/xcb/dri2.xml
/usr/share/xcb/dri3.xml
/usr/share/xcb/ge.xml
/usr/share/xcb/glx.xml
/usr/share/xcb/present.xml
/usr/share/xcb/randr.xml
/usr/share/xcb/record.xml
/usr/share/xcb/render.xml
/usr/share/xcb/res.xml
/usr/share/xcb/screensaver.xml
/usr/share/xcb/shape.xml
/usr/share/xcb/shm.xml
/usr/share/xcb/sync.xml
/usr/share/xcb/xc_misc.xml
/usr/share/xcb/xcb.xsd
/usr/share/xcb/xevie.xml
/usr/share/xcb/xf86dri.xml
/usr/share/xcb/xf86vidmode.xml
/usr/share/xcb/xfixes.xml
/usr/share/xcb/xinerama.xml
/usr/share/xcb/xinput.xml
/usr/share/xcb/xkb.xml
/usr/share/xcb/xprint.xml
/usr/share/xcb/xproto.xml
/usr/share/xcb/xselinux.xml
/usr/share/xcb/xtest.xml
/usr/share/xcb/xv.xml
/usr/share/xcb/xvmc.xml

%changelog
# let's skip this for now
