Name:       libvorbis
Version:    1.3.6
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -q

%build
%configure  --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/vorbis/codec.h
/usr/include/vorbis/vorbisenc.h
/usr/include/vorbis/vorbisfile.h
/usr/lib64/libvorbis.so
/usr/lib64/libvorbis.so.0
/usr/lib64/libvorbis.so.0.4.8
/usr/lib64/libvorbisenc.so
/usr/lib64/libvorbisenc.so.2
/usr/lib64/libvorbisenc.so.2.0.11
/usr/lib64/libvorbisfile.so
/usr/lib64/libvorbisfile.so.3
/usr/lib64/libvorbisfile.so.3.3.7
/usr/lib64/pkgconfig/vorbis.pc
/usr/lib64/pkgconfig/vorbisenc.pc
/usr/lib64/pkgconfig/vorbisfile.pc
/usr/share/aclocal/vorbis.m4
/usr/share/doc/libvorbis-1.3.6/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.3.6-1
- Version bump

