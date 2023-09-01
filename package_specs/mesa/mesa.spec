Name:       mesa
Version:    23.1.6
Release:    1
Summary:    The Mesa 3D Graphics Library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(gl)
Provides: pkgconfig(dri)

%description
Open source implementations of OpenGL, OpenGL ES, Vulkan, OpenCL.

%prep
%setup -a 0

%build
export GLL_DRV="svga,swrast,radeonsi"

mkdir build
pushd build
meson setup                   \
      --prefix=/usr   \
      --buildtype=release     \
      -Dplatforms=x11 \
      -Dgallium-drivers=$GLL_DRV  \
      -Dvulkan-drivers=""     \
      -Dvalgrind=disabled     \
      -Dlibunwind=disabled
ninja
popd
unset GLL_DRV

%install    
rm -rf %{buildroot}

pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/usr/include/
/usr/lib/dri/
/usr/lib/libEGL.so
/usr/lib/libEGL.so.1
/usr/lib/libEGL.so.1.0.0
/usr/lib/libGL.so
/usr/lib/libGL.so.1
/usr/lib/libGL.so.1.2.0
/usr/lib/libGLESv1_CM.so
/usr/lib/libGLESv1_CM.so.1
/usr/lib/libGLESv1_CM.so.1.1.0
/usr/lib/libGLESv2.so
/usr/lib/libGLESv2.so.2
/usr/lib/libGLESv2.so.2.0.0
/usr/lib/libgbm.so
/usr/lib/libgbm.so.1
/usr/lib/libgbm.so.1.0.0
/usr/lib/libglapi.so
/usr/lib/libglapi.so.0
/usr/lib/libglapi.so.0.0.0
/usr/lib/libxatracker.so
/usr/lib/libxatracker.so.2
/usr/lib/libxatracker.so.2.5.0
/usr/lib/pkgconfig/
/usr/share/drirc.d/00-mesa-defaults.conf

%changelog
* Thu Jun 15 2023 Chris Statzer <chris.statzer@gmail.com> 23.1.2
- Version bump
