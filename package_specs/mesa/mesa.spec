Name:       mesa
Version:    23.1.2
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
%setup -q

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
/usr/lib64/dri/
/usr/lib64/libEGL.so
/usr/lib64/libEGL.so.1
/usr/lib64/libEGL.so.1.0.0
/usr/lib64/libGL.so
/usr/lib64/libGL.so.1
/usr/lib64/libGL.so.1.2.0
/usr/lib64/libGLESv1_CM.so
/usr/lib64/libGLESv1_CM.so.1
/usr/lib64/libGLESv1_CM.so.1.1.0
/usr/lib64/libGLESv2.so
/usr/lib64/libGLESv2.so.2
/usr/lib64/libGLESv2.so.2.0.0
/usr/lib64/libgbm.so
/usr/lib64/libgbm.so.1
/usr/lib64/libgbm.so.1.0.0
/usr/lib64/libglapi.so
/usr/lib64/libglapi.so.0
/usr/lib64/libglapi.so.0.0.0
/usr/lib64/libxatracker.so
/usr/lib64/libxatracker.so.2
/usr/lib64/libxatracker.so.2.5.0
/usr/lib64/pkgconfig/
/usr/share/drirc.d/00-mesa-defaults.conf

%changelog
* Thu Jun 15 2023 Chris Statzer <chris.statzer@gmail.com> 23.1.2
- Version bump
