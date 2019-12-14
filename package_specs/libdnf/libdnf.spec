Name:       libdnf
Version:    0.39.1
Release:    1
Summary:    Software management library. 
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

Requires: nss >= 3.42.1-1

%description
Software management library. 

%prep
%setup

%build
mkdir build
pushd build
cmake 	-DWITH_GTKDOC=0 \
	-DWITH_HTML=0 \
	-DWITH_MAN=0 \
	-DPYTHON_DESIRED=3 \
	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
	..
%make_build
popd

%install
rm -rf %{buildroot}
pushd build
%make_install
popd

%files
/usr/lib64/libdnf.so
/usr/lib64/libdnf.so.2
/usr/lib64/libdnf/plugins/README
/usr/lib64/pkgconfig/libdnf.pc
/usr/share/locale/*
/usr/include/libdnf/*
/usr/lib/python3.7/site-packages/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.39.1
- Initial RPM

