Name:       libtheora
Version:    1.1.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build

sed -i 's/png_\(sizeof\)/\1/g' examples/png2theora.c &&
%configure --prefix=/usr --disable-static

%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/theora/codec.h
/usr/include/theora/theora.h
/usr/include/theora/theoradec.h
/usr/include/theora/theoraenc.h
/usr/lib64/libtheora.so
/usr/lib64/libtheora.so.0
/usr/lib64/libtheora.so.0.3.10
/usr/lib64/libtheoradec.so
/usr/lib64/libtheoradec.so.1
/usr/lib64/libtheoradec.so.1.1.4
/usr/lib64/libtheoraenc.so
/usr/lib64/libtheoraenc.so.1
/usr/lib64/libtheoraenc.so.1.1.2
/usr/lib64/pkgconfig/theora.pc
/usr/lib64/pkgconfig/theoradec.pc
/usr/lib64/pkgconfig/theoraenc.pc
/usr/share/doc/libtheora-1.1.1/*

%changelog
# let's skip this for now
