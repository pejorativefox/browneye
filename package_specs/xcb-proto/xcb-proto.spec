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
/usr/lib/python3.7/site-packages/xcbgen/__init__.py
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/__init__.cpython-37.opt-1.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/__init__.cpython-37.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/align.cpython-37.opt-1.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/align.cpython-37.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/error.cpython-37.opt-1.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/error.cpython-37.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/expr.cpython-37.opt-1.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/expr.cpython-37.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/matcher.cpython-37.opt-1.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/matcher.cpython-37.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/state.cpython-37.opt-1.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/state.cpython-37.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/xtypes.cpython-37.opt-1.pyc
/usr/lib/python3.7/site-packages/xcbgen/__pycache__/xtypes.cpython-37.pyc
/usr/lib/python3.7/site-packages/xcbgen/align.py
/usr/lib/python3.7/site-packages/xcbgen/error.py
/usr/lib/python3.7/site-packages/xcbgen/expr.py
/usr/lib/python3.7/site-packages/xcbgen/matcher.py
/usr/lib/python3.7/site-packages/xcbgen/state.py
/usr/lib/python3.7/site-packages/xcbgen/xtypes.py
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
