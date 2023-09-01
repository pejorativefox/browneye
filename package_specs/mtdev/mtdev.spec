Name:       mtdev
Version:    1.1.5
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2


%description
TODO

%prep
%setup -a 0

%build
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/mtdev-test
/usr/include/mtdev-mapping.h
/usr/include/mtdev-plumbing.h
/usr/include/mtdev.h
/usr/lib64/libmtdev.a
/usr/lib64/libmtdev.so
/usr/lib64/libmtdev.so.1
/usr/lib64/libmtdev.so.1.0.0
/usr/lib64/pkgconfig/mtdev.pc

%changelog
# let's skip this for now

