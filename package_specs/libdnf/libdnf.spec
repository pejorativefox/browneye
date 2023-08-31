Name:       libdnf
Version:    0.70.2
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
cmake 	-DWITH_GTKDOC=OFF \
	-DWITH_HTML=OFF \
	-DWITH_MAN=OFF \
	-DPYTHON_DESIRED:FILEPATH=/usr/bin/python3 \
	-DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DWITH_GTKDOC=OFF \
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
* Thu Aug 31 2023 Chris Statzer <chris.statzer@gmail.com> 0.70.2
- Version bump

* Wed May 13 2020 Chris Statzer <chris.statzer@qq.com> 0.47.0
- Upgrade to fix dnf incompat

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.39.1
- Initial RPM

