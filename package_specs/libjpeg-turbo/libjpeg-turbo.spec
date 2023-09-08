Name:       libjpeg-turbo
Version:    3.0.0
Release:    1
Summary:    JPEG library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
libjpeg-turbo is a fork of the original IJG libjpeg which uses SIMD to accelerate baseline JPEG compression and decompression.

%prep
%setup -q

%build


mkdir build
pushd build

cmake -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_BUILD_TYPE=RELEASE  \
      -DENABLE_STATIC=FALSE       \
      -DCMAKE_INSTALL_DOCDIR=/usr/share/doc/libjpeg-turbo-%{version} \
      -DCMAKE_INSTALL_DEFAULT_LIBDIR=lib64  \
      ..
%make_build
popd

%install    
rm -rf %{buildroot}
pushd build
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/cjpeg
/usr/bin/djpeg
/usr/bin/jpegtran
/usr/bin/rdjpgcom
/usr/bin/tjbench
/usr/bin/wrjpgcom
/usr/include/jconfig.h
/usr/include/jerror.h
/usr/include/jmorecfg.h
/usr/include/jpeglib.h
/usr/include/turbojpeg.h
/usr/lib64/libjpeg.so
/usr/lib64/libjpeg.so.62
/usr/lib64/libturbojpeg.so
/usr/lib64/libturbojpeg.so.0
/usr/lib64/pkgconfig/libjpeg.pc
/usr/lib64/pkgconfig/libturbojpeg.pc
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboConfig.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboConfigVersion.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboTargets-release.cmake
/usr/lib64/cmake/libjpeg-turbo/libjpeg-turboTargets.cmake
/usr/lib64/libjpeg.so.62.4.0
/usr/lib64/libturbojpeg.so.0.3.0
/usr/share/doc/libjpeg-turbo-%{version}/
/usr/share/man/man1/cjpeg.1.gz
/usr/share/man/man1/djpeg.1.gz
/usr/share/man/man1/jpegtran.1.gz
/usr/share/man/man1/rdjpgcom.1.gz
/usr/share/man/man1/wrjpgcom.1.gz

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 3.0.0-1
- Version bump
