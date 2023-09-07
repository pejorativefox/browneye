Name:       libxml2
Version:    2.10.4
Release:    1
Summary:    XML parsing library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
The libxml2 package contains libraries and utilities used for parsing XML files. 

%prep
%setup -q

%build
%configure  --disable-static \
            --with-history   \
            --with-python=/usr/bin/python3
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint
/usr/include/libxml2/
/usr/lib/python3.11/site-packages/__pycache__/drv_libxml2.cpython-311.opt-1.pyc
/usr/lib/python3.11/site-packages/__pycache__/drv_libxml2.cpython-311.pyc
/usr/lib/python3.11/site-packages/__pycache__/libxml2.cpython-311.opt-1.pyc
/usr/lib/python3.11/site-packages/__pycache__/libxml2.cpython-311.pyc
/usr/lib/python3.11/site-packages/drv_libxml2.py
/usr/lib/python3.11/site-packages/libxml2.py
/usr/lib64/cmake/libxml2/libxml2-config.cmake
/usr/lib64/libxml2.so
/usr/lib64/libxml2.so.2
/usr/lib64/libxml2.so.2.10.4
/usr/lib64/pkgconfig/libxml-2.0.pc
/usr/lib64/python3.11/site-packages/libxml2mod.so
/usr/share/aclocal/libxml.m4
/usr/share/doc/
/usr/share/gtk-doc/
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 2.10.4
- Version bump
