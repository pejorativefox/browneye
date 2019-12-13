Name:       libsndfile
Version:    1.0.28
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
%configure  --disable-static \
            --docdir=/usr/share/doc/libsndfile-1.0.28
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/sndfile-cmp
/usr/bin/sndfile-concat
/usr/bin/sndfile-convert
/usr/bin/sndfile-deinterleave
/usr/bin/sndfile-info
/usr/bin/sndfile-interleave
/usr/bin/sndfile-metadata-get
/usr/bin/sndfile-metadata-set
/usr/bin/sndfile-play
/usr/bin/sndfile-salvage
/usr/include/sndfile.h
/usr/include/sndfile.hh
/usr/lib64/libsndfile.la
/usr/lib64/libsndfile.so
/usr/lib64/libsndfile.so.1
/usr/lib64/libsndfile.so.1.0.28
/usr/lib64/pkgconfig/sndfile.pc
/usr/share/doc/libsndfile-1.0.28/FAQ.html
/usr/share/doc/libsndfile-1.0.28/api.html
/usr/share/doc/libsndfile-1.0.28/bugs.html
/usr/share/doc/libsndfile-1.0.28/command.html
/usr/share/doc/libsndfile-1.0.28/embedded_files.html
/usr/share/doc/libsndfile-1.0.28/index.html
/usr/share/doc/libsndfile-1.0.28/libsndfile.css
/usr/share/doc/libsndfile-1.0.28/libsndfile.jpg
/usr/share/doc/libsndfile-1.0.28/lists.html
/usr/share/doc/libsndfile-1.0.28/new_file_type.HOWTO
/usr/share/doc/libsndfile-1.0.28/octave.html
/usr/share/doc/libsndfile-1.0.28/sndfile_info.html
/usr/share/doc/libsndfile-1.0.28/tutorial.html
/usr/share/doc/libsndfile-1.0.28/win32.html
/usr/share/man/man1/sndfile-cmp.1.gz
/usr/share/man/man1/sndfile-concat.1.gz
/usr/share/man/man1/sndfile-convert.1.gz
/usr/share/man/man1/sndfile-deinterleave.1.gz
/usr/share/man/man1/sndfile-info.1.gz
/usr/share/man/man1/sndfile-interleave.1.gz
/usr/share/man/man1/sndfile-metadata-get.1.gz
/usr/share/man/man1/sndfile-metadata-set.1.gz
/usr/share/man/man1/sndfile-play.1.gz
/usr/share/man/man1/sndfile-salvage.1.gz
/usr/bin/sndfile-regtest

%changelog
# let's skip this for now

