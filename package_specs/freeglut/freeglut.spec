Name:       freeglut
Version:    3.2.1
Release:    1
Summary:    GLUT is a window system independent toolkit for writing OpenGL programs
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Freeglut is intended to be a 100% compatible, completely opensourced clone of the GLUT library. GLUT is a window system independent toolkit for writing OpenGL programs, implementing a simple windowing API, which makes learning about and exploring OpenGL programming very easy.

%prep
%setup

%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/include/GL/freeglut.h
/usr/include/GL/freeglut_ext.h
/usr/include/GL/freeglut_std.h
/usr/include/GL/freeglut_ucall.h
/usr/include/GL/glut.h
/usr/lib64/cmake/FreeGLUT/FreeGLUTConfig.cmake
/usr/lib64/cmake/FreeGLUT/FreeGLUTConfigVersion.cmake
/usr/lib64/cmake/FreeGLUT/FreeGLUTTargets-noconfig.cmake
/usr/lib64/cmake/FreeGLUT/FreeGLUTTargets.cmake
/usr/lib64/libglut.a
/usr/lib64/libglut.so
/usr/lib64/libglut.so.3
/usr/lib64/libglut.so.3.11.0
/usr/lib64/pkgconfig/glut.pc

%changelog
* Tue Jun 16 2020 Chris Statzer <chris.statzer@qq.com> 3.2.1
- Initial RPM

