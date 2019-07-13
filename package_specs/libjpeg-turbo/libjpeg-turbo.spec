Name:       libjpeg-turbo
Version:    2.0.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build


mkdir build
pushd build

cmake -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_BUILD_TYPE=RELEASE  \
      -DENABLE_STATIC=FALSE       \
      -DCMAKE_INSTALL_DOCDIR=/usr/share/doc/libjpeg-turbo-2.0.2 \
      -DCMAKE_INSTALL_DEFAULT_LIBDIR=lib  \
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
/usr/lib/libjpeg.so
/usr/lib/libjpeg.so.62
/usr/lib/libjpeg.so.62.3.0
/usr/lib/libturbojpeg.so
/usr/lib/libturbojpeg.so.0
/usr/lib/libturbojpeg.so.0.2.0
/usr/lib/pkgconfig/libjpeg.pc
/usr/lib/pkgconfig/libturbojpeg.pc
/usr/share/doc/libjpeg-turbo-2.0.2/LICENSE.md
/usr/share/doc/libjpeg-turbo-2.0.2/README.ijg
/usr/share/doc/libjpeg-turbo-2.0.2/README.md
/usr/share/doc/libjpeg-turbo-2.0.2/example.txt
/usr/share/doc/libjpeg-turbo-2.0.2/libjpeg.txt
/usr/share/doc/libjpeg-turbo-2.0.2/structure.txt
/usr/share/doc/libjpeg-turbo-2.0.2/tjexample.c
/usr/share/doc/libjpeg-turbo-2.0.2/usage.txt
/usr/share/doc/libjpeg-turbo-2.0.2/wizard.txt
/usr/share/man/man1/cjpeg.1.gz
/usr/share/man/man1/djpeg.1.gz
/usr/share/man/man1/jpegtran.1.gz
/usr/share/man/man1/rdjpgcom.1.gz
/usr/share/man/man1/wrjpgcom.1.gz

%changelog
# let's skip this for now

