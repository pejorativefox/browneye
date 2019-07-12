Name:       libdrm
Version:    2.4.97
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



%description
TODO

%prep
%setup -a 0


%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/libdrm/amdgpu.h
/usr/include/libdrm/amdgpu_drm.h
/usr/include/libdrm/drm.h
/usr/include/libdrm/drm_fourcc.h
/usr/include/libdrm/drm_mode.h
/usr/include/libdrm/drm_sarea.h
/usr/include/libdrm/i915_drm.h
/usr/include/libdrm/intel_aub.h
/usr/include/libdrm/intel_bufmgr.h
/usr/include/libdrm/intel_debug.h
/usr/include/libdrm/mach64_drm.h
/usr/include/libdrm/mga_drm.h
/usr/include/libdrm/msm_drm.h
/usr/include/libdrm/nouveau/nouveau.h
/usr/include/libdrm/nouveau/nvif/cl0080.h
/usr/include/libdrm/nouveau/nvif/cl9097.h
/usr/include/libdrm/nouveau/nvif/class.h
/usr/include/libdrm/nouveau/nvif/if0002.h
/usr/include/libdrm/nouveau/nvif/if0003.h
/usr/include/libdrm/nouveau/nvif/ioctl.h
/usr/include/libdrm/nouveau/nvif/unpack.h
/usr/include/libdrm/nouveau_drm.h
/usr/include/libdrm/qxl_drm.h
/usr/include/libdrm/r128_drm.h
/usr/include/libdrm/r600_pci_ids.h
/usr/include/libdrm/radeon_bo.h
/usr/include/libdrm/radeon_bo_gem.h
/usr/include/libdrm/radeon_bo_int.h
/usr/include/libdrm/radeon_cs.h
/usr/include/libdrm/radeon_cs_gem.h
/usr/include/libdrm/radeon_cs_int.h
/usr/include/libdrm/radeon_drm.h
/usr/include/libdrm/radeon_surface.h
/usr/include/libdrm/savage_drm.h
/usr/include/libdrm/sis_drm.h
/usr/include/libdrm/tegra_drm.h
/usr/include/libdrm/vc4_drm.h
/usr/include/libdrm/via_drm.h
/usr/include/libdrm/virtgpu_drm.h
/usr/include/libdrm/vmwgfx_drm.h
/usr/include/libkms/libkms.h
/usr/include/libsync.h
/usr/include/xf86drm.h
/usr/include/xf86drmMode.h
/usr/lib64/libdrm.la
/usr/lib64/libdrm.so
/usr/lib64/libdrm.so.2
/usr/lib64/libdrm.so.2.4.0
/usr/lib64/libdrm_amdgpu.la
/usr/lib64/libdrm_amdgpu.so
/usr/lib64/libdrm_amdgpu.so.1
/usr/lib64/libdrm_amdgpu.so.1.0.0
/usr/lib64/libdrm_intel.la
/usr/lib64/libdrm_intel.so
/usr/lib64/libdrm_intel.so.1
/usr/lib64/libdrm_intel.so.1.0.0
/usr/lib64/libdrm_nouveau.la
/usr/lib64/libdrm_nouveau.so
/usr/lib64/libdrm_nouveau.so.2
/usr/lib64/libdrm_nouveau.so.2.0.0
/usr/lib64/libdrm_radeon.la
/usr/lib64/libdrm_radeon.so
/usr/lib64/libdrm_radeon.so.1
/usr/lib64/libdrm_radeon.so.1.0.1
/usr/lib64/libkms.la
/usr/lib64/libkms.so
/usr/lib64/libkms.so.1
/usr/lib64/libkms.so.1.0.0
/usr/lib64/pkgconfig/libdrm.pc
/usr/lib64/pkgconfig/libdrm_amdgpu.pc
/usr/lib64/pkgconfig/libdrm_intel.pc
/usr/lib64/pkgconfig/libdrm_nouveau.pc
/usr/lib64/pkgconfig/libdrm_radeon.pc
/usr/lib64/pkgconfig/libkms.pc
/usr/share/libdrm/amdgpu.ids

%changelog
# let's skip this for now
