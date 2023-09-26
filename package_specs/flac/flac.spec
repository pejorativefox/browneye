Name:       flac
Version:    1.3.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup -a 0 

%build
%configure  --disable-thorough-tests
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/flac
/usr/bin/metaflac
/usr/include/FLAC++/all.h
/usr/include/FLAC++/decoder.h
/usr/include/FLAC++/encoder.h
/usr/include/FLAC++/export.h
/usr/include/FLAC++/metadata.h
/usr/include/FLAC/all.h
/usr/include/FLAC/assert.h
/usr/include/FLAC/callback.h
/usr/include/FLAC/export.h
/usr/include/FLAC/format.h
/usr/include/FLAC/metadata.h
/usr/include/FLAC/ordinals.h
/usr/include/FLAC/stream_decoder.h
/usr/include/FLAC/stream_encoder.h
/usr/lib64/libFLAC++.so
/usr/lib64/libFLAC++.so.6
/usr/lib64/libFLAC++.so.6.3.0
/usr/lib64/libFLAC.so
/usr/lib64/libFLAC.so.8
/usr/lib64/libFLAC.so.8.3.0
/usr/lib64/pkgconfig/flac++.pc
/usr/lib64/pkgconfig/flac.pc
/usr/share/aclocal/libFLAC++.m4
/usr/share/aclocal/libFLAC.m4
/usr/share/doc/flac-1.3.2/FLAC.tag
/usr/share/doc/flac-1.3.2/html/changelog.html
/usr/share/doc/flac-1.3.2/html/developers.html
/usr/share/doc/flac-1.3.2/html/documentation.html
/usr/share/doc/flac-1.3.2/html/documentation_bugs.html
/usr/share/doc/flac-1.3.2/html/documentation_example_code.html
/usr/share/doc/flac-1.3.2/html/documentation_format_overview.html
/usr/share/doc/flac-1.3.2/html/documentation_tools.html
/usr/share/doc/flac-1.3.2/html/documentation_tools_flac.html
/usr/share/doc/flac-1.3.2/html/documentation_tools_metaflac.html
/usr/share/doc/flac-1.3.2/html/faq.html
/usr/share/doc/flac-1.3.2/html/favicon.ico
/usr/share/doc/flac-1.3.2/html/features.html
/usr/share/doc/flac-1.3.2/html/flac.css
/usr/share/doc/flac-1.3.2/html/format.html
/usr/share/doc/flac-1.3.2/html/id.html
/usr/share/doc/flac-1.3.2/html/images/logo.svg
/usr/share/doc/flac-1.3.2/html/images/logo130.gif
/usr/share/doc/flac-1.3.2/html/index.html
/usr/share/doc/flac-1.3.2/html/license.html
/usr/share/doc/flac-1.3.2/html/ogg_mapping.html
/usr/share/man/man1/flac.1.gz
/usr/share/man/man1/metaflac.1.gz

%changelog
# let's skip this for now

