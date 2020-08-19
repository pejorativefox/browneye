Name:       glew
Version:    2.1.0
Release:    1
Summary:    GLEW is the OpenGL Extension Wrangler Library. 
License:    GPL
Source0:    %{name}-%{version}.tgz
Prefix:     /usr

%description
GLEW is the OpenGL Extension Wrangler Library. 

%prep
%setup

%build
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/GL/
/usr/lib/pkgconfig/glew.pc
/usr/lib64/libGLEW.a
/usr/lib64/libGLEW.so
/usr/lib64/libGLEW.so.2.1
/usr/lib64/libGLEW.so.2.1.0

%changelog
* Wed Aug 19 2020 Chris Statzer <chris.statzer@qq.com> 2.1.0
- Initial RPM

