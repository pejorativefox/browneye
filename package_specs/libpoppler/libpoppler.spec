Name:       libpoppler
Version:    0.88.0
Release:    1
Summary:    Poppler is a PDF rendering library based on the xpdf-3.0 code base. 
License:    NO_IDEA
Source0:    poppler-%{version}.tar.xz
Prefix:     /usr

BuildRequires: openjpeg

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base. 

%prep
%setup -n poppler-%{version}

%build
mkdir build
pushd build
cmake 	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DENABLE_QT5=OFF \
	..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd


%files
/usr/bin/pdfattach
/usr/bin/pdfdetach
/usr/bin/pdffonts
/usr/bin/pdfimages
/usr/bin/pdfinfo
/usr/bin/pdfseparate
/usr/bin/pdfsig
/usr/bin/pdftocairo
/usr/bin/pdftohtml
/usr/bin/pdftoppm
/usr/bin/pdftops
/usr/bin/pdftotext
/usr/bin/pdfunite
/usr/include/poppler/cpp/
/usr/include/poppler/glib/
/usr/lib64/girepository-1.0/Poppler-0.18.typelib
/usr/lib64/libpoppler-cpp.so
/usr/lib64/libpoppler-cpp.so.0
/usr/lib64/libpoppler-cpp.so.0.8.0
/usr/lib64/libpoppler-glib.so
/usr/lib64/libpoppler-glib.so.8
/usr/lib64/libpoppler-glib.so.8.16.0
/usr/lib64/libpoppler.so
/usr/lib64/libpoppler.so.99
/usr/lib64/libpoppler.so.99.0.0
/usr/lib64/pkgconfig/
/usr/share/gir-1.0/Poppler-0.18.gir
/usr/share/man/man1/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 0.88.0
- Initial RPM

