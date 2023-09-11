Name:       libglu
Version:    9.0.1
Release:    1
Summary:    This package provides the Mesa OpenGL Utility library. 
License:    NO_IDEA
Source0:    glu-%{version}.tar.xz
Prefix:     /usr

%description
This package provides the Mesa OpenGL Utility library. 

%prep
%setup -n glu-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/GL/glu.h
/usr/include/GL/glu_mangle.h
/usr/lib64/libGLU.a
/usr/lib64/libGLU.so
/usr/lib64/libGLU.so.1
/usr/lib64/libGLU.so.1.3.1
/usr/lib64/pkgconfig/glu.pc

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 9.0.1-1
- Initial RPM

