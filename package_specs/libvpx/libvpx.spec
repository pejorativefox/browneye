Name:       libvpx
Version:    1.8.0
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
sed -i 's/cp -p/cp/' build/make/Makefile &&

mkdir -pv libvpx-build
pushd libvpx-build

../configure --prefix=/usr    \
             --enable-shared  \
             --disable-static
%make_build
popd

%install    
rm -rf %{buildroot}
pushd libvpx-build
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/vpxdec
/usr/bin/vpxenc
/usr/include/vpx/vp8.h
/usr/include/vpx/vp8cx.h
/usr/include/vpx/vp8dx.h
/usr/include/vpx/vpx_codec.h
/usr/include/vpx/vpx_decoder.h
/usr/include/vpx/vpx_encoder.h
/usr/include/vpx/vpx_frame_buffer.h
/usr/include/vpx/vpx_image.h
/usr/include/vpx/vpx_integer.h
/usr/lib/libvpx.so
/usr/lib/libvpx.so.6
/usr/lib/libvpx.so.6.0
/usr/lib/libvpx.so.6.0.0
/usr/lib/pkgconfig/vpx.pc

%changelog
# let's skip this for now

