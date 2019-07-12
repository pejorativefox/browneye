Name:       mesa
Version:    18.3.3
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
export GLL_DRV="i915,nouveau,svga,swrast"
%configure CFLAGS='-O2' CXXFLAGS='-O2'         \
            --sysconfdir=/etc                  \
            --enable-osmesa                    \
            --enable-xa                        \
            --enable-glx-tls                   \
            --with-platforms="drm,x11" \
            --with-gallium-drivers=$GLL_DRV
%make_build
unset GLL_DRV

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/EGL/egl.h
/usr/include/EGL/eglext.h
/usr/include/EGL/eglextchromium.h
/usr/include/EGL/eglmesaext.h
/usr/include/EGL/eglplatform.h
/usr/include/GL/gl.h
/usr/include/GL/gl_mangle.h
/usr/include/GL/glcorearb.h
/usr/include/GL/glext.h
/usr/include/GL/glx.h
/usr/include/GL/glx_mangle.h
/usr/include/GL/glxext.h
/usr/include/GL/internal/dri_interface.h
/usr/include/GL/osmesa.h
/usr/include/GLES/egl.h
/usr/include/GLES/gl.h
/usr/include/GLES/glext.h
/usr/include/GLES/glplatform.h
/usr/include/GLES2/gl2.h
/usr/include/GLES2/gl2ext.h
/usr/include/GLES2/gl2platform.h
/usr/include/GLES3/gl3.h
/usr/include/GLES3/gl31.h
/usr/include/GLES3/gl32.h
/usr/include/GLES3/gl3ext.h
/usr/include/GLES3/gl3platform.h
/usr/include/KHR/khrplatform.h
/usr/include/gbm.h
/usr/include/xa_composite.h
/usr/include/xa_context.h
/usr/include/xa_tracker.h
/usr/lib64/dri/i915_dri.so
/usr/lib64/dri/i965_dri.so
/usr/lib64/dri/kms_swrast_dri.so
/usr/lib64/dri/nouveau_dri.so
/usr/lib64/dri/nouveau_vieux_dri.so
/usr/lib64/dri/r200_dri.so
/usr/lib64/dri/radeon_dri.so
/usr/lib64/dri/swrast_dri.so
/usr/lib64/dri/vmwgfx_dri.so
/usr/lib64/libEGL.la
/usr/lib64/libEGL.so
/usr/lib64/libEGL.so.1
/usr/lib64/libEGL.so.1.0.0
/usr/lib64/libGL.la
/usr/lib64/libGL.so
/usr/lib64/libGL.so.1
/usr/lib64/libGL.so.1.2.0
/usr/lib64/libGLESv1_CM.la
/usr/lib64/libGLESv1_CM.so
/usr/lib64/libGLESv1_CM.so.1
/usr/lib64/libGLESv1_CM.so.1.1.0
/usr/lib64/libGLESv2.la
/usr/lib64/libGLESv2.so
/usr/lib64/libGLESv2.so.2
/usr/lib64/libGLESv2.so.2.0.0
/usr/lib64/libOSMesa.la
/usr/lib64/libOSMesa.so
/usr/lib64/libOSMesa.so.8
/usr/lib64/libOSMesa.so.8.0.0
/usr/lib64/libXvMCnouveau.so
/usr/lib64/libXvMCnouveau.so.1
/usr/lib64/libXvMCnouveau.so.1.0
/usr/lib64/libXvMCnouveau.so.1.0.0
/usr/lib64/libgbm.la
/usr/lib64/libgbm.so
/usr/lib64/libgbm.so.1
/usr/lib64/libgbm.so.1.0.0
/usr/lib64/libglapi.la
/usr/lib64/libglapi.so
/usr/lib64/libglapi.so.0
/usr/lib64/libglapi.so.0.0.0
/usr/lib64/libxatracker.la
/usr/lib64/libxatracker.so
/usr/lib64/libxatracker.so.2
/usr/lib64/libxatracker.so.2.4.0
/usr/lib64/pkgconfig/dri.pc
/usr/lib64/pkgconfig/egl.pc
/usr/lib64/pkgconfig/gbm.pc
/usr/lib64/pkgconfig/gl.pc
/usr/lib64/pkgconfig/glesv1_cm.pc
/usr/lib64/pkgconfig/glesv2.pc
/usr/lib64/pkgconfig/osmesa.pc
/usr/lib64/pkgconfig/xatracker.pc
/usr/share/drirc.d/00-mesa-defaults.conf

%changelog
# let's skip this for now
