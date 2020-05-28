Name:       openjpeg
Version:    2.3.1
Release:    1
Summary:    An open-source JPEG 2000 codec written in C.
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
An open-source JPEG 2000 codec written in C.

%prep
%setup

%build
mkdir build
pushd build
cmake 	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
	..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/bin/opj_compress
/usr/bin/opj_decompress
/usr/bin/opj_dump
/usr/include/openjpeg-2.3/openjpeg.h
/usr/include/openjpeg-2.3/opj_config.h
/usr/include/openjpeg-2.3/opj_stdint.h
/usr/lib/libopenjp2.a
/usr/lib/libopenjp2.so
/usr/lib/libopenjp2.so.2.3.1
/usr/lib/libopenjp2.so.7
/usr/lib/openjpeg-2.3/OpenJPEGConfig.cmake
/usr/lib/openjpeg-2.3/OpenJPEGTargets-noconfig.cmake
/usr/lib/openjpeg-2.3/OpenJPEGTargets.cmake
/usr/lib/pkgconfig/libopenjp2.pc

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2.3.1
- Initial RPM

