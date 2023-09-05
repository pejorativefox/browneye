Name:       expat
Version:    2.5.0
Release:    1
Summary:    stream-oriented XML parser
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
stream-oriented XML parser

%prep
%setup -q

%build
%configure --disable-static \
           --docdir=/usr/share/doc/expat-%{version}
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/xmlwf
/usr/include/expat.h
/usr/include/expat_config.h
/usr/include/expat_external.h
/usr/lib64/cmake/expat-%{version}/
/usr/lib64/libexpat.so.1.8.10
/usr/lib64/libexpat.so
/usr/lib64/libexpat.so.1
/usr/lib64/pkgconfig/expat.pc
/usr/share/doc/expat-%{version}/

%changelog
# let's skip this for now
