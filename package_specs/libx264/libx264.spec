Name:       libx264
Version:    20190815
Release:    1
Summary:    TODO
License:    GPL3
Source0:    x264-snapshot-20190815-2245-stable.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -n x264-snapshot-20190815-2245-stable

%build
%configure --enable-shared --diasble-cli
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/x264
/usr/include/x264.h
/usr/include/x264_config.h
/usr/lib64/libx264.so
/usr/lib64/libx264.so.157
/usr/lib64/pkgconfig/x264.pc

%changelog
# let's skip this for now
