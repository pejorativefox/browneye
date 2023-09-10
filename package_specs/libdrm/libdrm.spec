Name:       libdrm
Version:    2.4.115
Release:    1
Summary:    Libdrm provides a userspace library for accessing the direct rendering manager (DRM)
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz



%description
Libdrm provides a userspace library for accessing the direct rendering manager (DRM) on operating systems that support the ioctl interface. Libdrm is a low-level library, typically used by graphics drivers such as the Mesa DRI drivers, the X drivers, libva and similar projects. 

%prep
%setup -a 0


%build
mkdir build
pushd build
meson setup --prefix=/usr \
            --buildtype=release   \
            -Dudev=true           \
            -Dvalgrind=disabled   \
            ..
ninja
popd
%install    
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/libdrm/
/usr/include/libsync.h
/usr/include/xf86drm.h
/usr/include/xf86drmMode.h
/usr/lib64/libdrm.so
/usr/lib64/libdrm.so.2
/usr/lib64/libdrm.so.2.4.0
/usr/lib64/libdrm_amdgpu.so
/usr/lib64/libdrm_amdgpu.so.1
/usr/lib64/libdrm_amdgpu.so.1.0.0
/usr/lib64/libdrm_intel.so
/usr/lib64/libdrm_intel.so.1
/usr/lib64/libdrm_intel.so.1.0.0
/usr/lib64/libdrm_nouveau.so
/usr/lib64/libdrm_nouveau.so.2
/usr/lib64/libdrm_nouveau.so.2.0.0
/usr/lib64/libdrm_radeon.so
/usr/lib64/libdrm_radeon.so.1
/usr/lib64/libdrm_radeon.so.1.0.1
/usr/lib64/pkgconfig/
/usr/share/libdrm/amdgpu.ids
/usr/share/man/

%changelog
* Thu Jun 15 2023 Chris Statzer <chris.statzer@gmail.com> 2.4.115
- Bumped version to 2.4.115
