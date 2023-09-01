Name:       expat
Version:    2.2.6
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
sed -i 's|usr/bin/env |bin/|' run.sh.in
%configure --disable-static \
           --docdir=/usr/share/doc/expat-2.2.6
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
/usr/lib64/libexpat.so
/usr/lib64/libexpat.so.1
/usr/lib64/libexpat.so.1.6.8
/usr/lib64/pkgconfig/expat.pc
/usr/share/doc/expat-2.2.6/AUTHORS
/usr/share/doc/expat-2.2.6/changelog
/usr/share/man/man1/xmlwf.1.gz

%changelog
# let's skip this for now
