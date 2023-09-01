Name:       libopus
Version:    1.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    opus-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0 -n opus-1.3

%build
%configure  --disable-static \
            --docdir=/usr/share/doc/opus-1.3
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/opus/opus.h
/usr/include/opus/opus_defines.h
/usr/include/opus/opus_multistream.h
/usr/include/opus/opus_projection.h
/usr/include/opus/opus_types.h
/usr/lib64/libopus.so
/usr/lib64/libopus.so.0
/usr/lib64/libopus.so.0.7.0
/usr/lib64/pkgconfig/opus.pc
/usr/share/aclocal/opus.m4

%changelog
# let's skip this for now

