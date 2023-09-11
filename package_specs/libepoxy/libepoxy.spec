Name:       libepoxy
Version:    1.5.10
Release:    1
Summary:    OpenGL function management
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(epoxy)

%description
libepoxy is a library for handling OpenGL function pointer management. 

%prep
%setup -q

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
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.5.10-1
- Version bump
