Name:       xz
Version:    5.2.4
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
%configure --disable-static \
           --docdir=/usr/share/doc/xz-5.2.4
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/lzcat
/usr/bin/lzcmp
/usr/bin/lzdiff
/usr/bin/lzegrep
/usr/bin/lzfgrep
/usr/bin/lzgrep
/usr/bin/lzless
/usr/bin/lzma
/usr/bin/lzmadec
/usr/bin/lzmainfo
/usr/bin/lzmore
/usr/bin/unlzma
/usr/bin/unxz
/usr/bin/xz
/usr/bin/xzcat
/usr/bin/xzcmp
/usr/bin/xzdec
/usr/bin/xzdiff
/usr/bin/xzegrep
/usr/bin/xzfgrep
/usr/bin/xzgrep
/usr/bin/xzless
/usr/bin/xzmore
/usr/include/lzma.h
/usr/include/lzma/base.h
/usr/include/lzma/bcj.h
/usr/include/lzma/block.h
/usr/include/lzma/check.h
/usr/include/lzma/container.h
/usr/include/lzma/delta.h
/usr/include/lzma/filter.h
/usr/include/lzma/hardware.h
/usr/include/lzma/index.h
/usr/include/lzma/index_hash.h
/usr/include/lzma/lzma12.h
/usr/include/lzma/stream_flags.h
/usr/include/lzma/version.h
/usr/include/lzma/vli.h
/usr/lib64/liblzma.la
/usr/lib64/liblzma.so
/usr/lib64/liblzma.so.5
/usr/lib64/liblzma.so.5.2.4
/usr/lib64/pkgconfig/liblzma.pc
/usr/share/doc/xz-5.2.4/AUTHORS
/usr/share/doc/xz-5.2.4/COPYING
/usr/share/doc/xz-5.2.4/COPYING.GPLv2
/usr/share/doc/xz-5.2.4/NEWS
/usr/share/doc/xz-5.2.4/README
/usr/share/doc/xz-5.2.4/THANKS
/usr/share/doc/xz-5.2.4/TODO
/usr/share/doc/xz-5.2.4/examples/00_README.txt
/usr/share/doc/xz-5.2.4/examples/01_compress_easy.c
/usr/share/doc/xz-5.2.4/examples/02_decompress.c
/usr/share/doc/xz-5.2.4/examples/03_compress_custom.c
/usr/share/doc/xz-5.2.4/examples/04_compress_easy_mt.c
/usr/share/doc/xz-5.2.4/examples/Makefile
/usr/share/doc/xz-5.2.4/examples_old/xz_pipe_comp.c
/usr/share/doc/xz-5.2.4/examples_old/xz_pipe_decomp.c
/usr/share/doc/xz-5.2.4/faq.txt
/usr/share/doc/xz-5.2.4/history.txt
/usr/share/doc/xz-5.2.4/lzma-file-format.txt
/usr/share/doc/xz-5.2.4/xz-file-format.txt
/usr/share/locale/cs/LC_MESSAGES/xz.mo
/usr/share/locale/de/LC_MESSAGES/xz.mo
/usr/share/locale/fr/LC_MESSAGES/xz.mo
/usr/share/locale/it/LC_MESSAGES/xz.mo
/usr/share/locale/pl/LC_MESSAGES/xz.mo
/usr/share/locale/vi/LC_MESSAGES/xz.mo
/usr/share/man/man1/lzcat.1.gz
/usr/share/man/man1/lzcmp.1.gz
/usr/share/man/man1/lzdiff.1.gz
/usr/share/man/man1/lzegrep.1.gz
/usr/share/man/man1/lzfgrep.1.gz
/usr/share/man/man1/lzgrep.1.gz
/usr/share/man/man1/lzless.1.gz
/usr/share/man/man1/lzma.1.gz
/usr/share/man/man1/lzmadec.1.gz
/usr/share/man/man1/lzmainfo.1.gz
/usr/share/man/man1/lzmore.1.gz
/usr/share/man/man1/unlzma.1.gz
/usr/share/man/man1/unxz.1.gz
/usr/share/man/man1/xz.1.gz
/usr/share/man/man1/xzcat.1.gz
/usr/share/man/man1/xzcmp.1.gz
/usr/share/man/man1/xzdec.1.gz
/usr/share/man/man1/xzdiff.1.gz
/usr/share/man/man1/xzegrep.1.gz
/usr/share/man/man1/xzfgrep.1.gz
/usr/share/man/man1/xzgrep.1.gz
/usr/share/man/man1/xzless.1.gz
/usr/share/man/man1/xzmore.1.gz


%changelog
# let's skip this for now
