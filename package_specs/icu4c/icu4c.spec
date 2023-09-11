Name:       icu4c
Version:    73.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    icu4c-73_2-src.tgz


%description
TODO

%prep
%setup -q -n icu

%build
pushd source
%configure
%make_build
popd

%install    
rm -rf %{buildroot}
pushd source
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/derb
/usr/bin/genbrk
/usr/bin/gencfu
/usr/bin/gencnval
/usr/bin/gendict
/usr/bin/genrb
/usr/bin/icu-config
/usr/bin/icuinfo
/usr/bin/makeconv
/usr/bin/pkgdata
/usr/bin/uconv
/usr/bin/icuexportdata
/usr/lib64/icu/73.2/Makefile.inc
/usr/lib64/icu/73.2/pkgdata.inc
/usr/lib64/icu/Makefile.inc
/usr/lib64/icu/current
/usr/lib64/icu/pkgdata.inc
/usr/lib64/libicudata.so
/usr/lib64/libicudata.so.73
/usr/lib64/libicudata.so.73.2
/usr/lib64/libicui18n.so
/usr/lib64/libicui18n.so.73
/usr/lib64/libicui18n.so.73.2
/usr/lib64/libicuio.so
/usr/lib64/libicuio.so.73
/usr/lib64/libicuio.so.73.2
/usr/lib64/libicutest.so
/usr/lib64/libicutest.so.73
/usr/lib64/libicutest.so.73.2
/usr/lib64/libicutu.so
/usr/lib64/libicutu.so.73
/usr/lib64/libicutu.so.73.2
/usr/lib64/libicuuc.so
/usr/lib64/libicuuc.so.73
/usr/lib64/libicuuc.so.73.2
/usr/lib64/pkgconfig/icu-i18n.pc
/usr/lib64/pkgconfig/icu-io.pc
/usr/lib64/pkgconfig/icu-uc.pc
/usr/sbin/escapesrc
/usr/sbin/genccode
/usr/sbin/gencmn
/usr/sbin/gennorm2
/usr/sbin/gensprep
/usr/sbin/icupkg
/usr/share/icu/73.2/LICENSE
/usr/share/icu/73.2/config/mh-linux
/usr/share/icu/73.2/install-sh
/usr/share/icu/73.2/mkinstalldirs
/usr/include/unicode/
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 73.2-1
- Version bump
