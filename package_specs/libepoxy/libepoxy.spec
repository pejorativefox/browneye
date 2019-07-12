Name:       libepoxy
Version:    1.5.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz



%description
TODO

%prep
%setup -a 0

%build
mkdir -pv build
pushd build
meson --prefix=/usr
ninja
popd

%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/epoxy/common.h
/usr/include/epoxy/egl.h
/usr/include/epoxy/egl_generated.h
/usr/include/epoxy/gl.h
/usr/include/epoxy/gl_generated.h
/usr/include/epoxy/glx.h
/usr/include/epoxy/glx_generated.h
/usr/lib64/libepoxy.so
/usr/lib64/libepoxy.so.0
/usr/lib64/libepoxy.so.0.0.0
/usr/lib64/pkgconfig/epoxy.pc

%changelog
# let's skip this for now

