Name:       libx265
Version:    3.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    x265_%{version}.tar.gz


%description
TODO

%prep
%setup -a 0 -n x265_3.0

%build
mkdir build-x265
pushd build-x265
cmake -DCMAKE_INSTALL_PREFIX=/usr ../source
%make_build
popd

%install    
rm -rf %{buildroot}
pushd build-x265
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/x265
/usr/include/x265.h
/usr/include/x265_config.h
/usr/lib/libx265.a
/usr/lib/libx265.so
/usr/lib/libx265.so.169
/usr/lib/pkgconfig/x265.pc


%changelog
# let's skip this for now

