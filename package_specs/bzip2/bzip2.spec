Name:       bzip2
Version:    1.0.6
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
make -f Makefile-libbz2_so \
    CC="%{__cc}" AR="%{__ar}" RANLIB="%{__ranlib}" \
    CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -fpic -fPIC $O3" \
    %{?_smp_mflags} all

rm -f *.o
	
make CC="%{__cc}" AR="%{__ar}" RANLIB="%{__ranlib}" \
     CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 $O3" \
     %{?_smp_mflags} all

%install
rm -rf %{buildroot}
chmod 644 bzlib.h
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/pkgconfig,%{_includedir}}
cp -p bzlib.h $RPM_BUILD_ROOT%{_includedir}
install -m 755 libbz2.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install -m 644 libbz2.a $RPM_BUILD_ROOT%{_libdir}
# install -m 644 bzip2.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/bzip2.pc
install -m 755 bzip2-shared  $RPM_BUILD_ROOT%{_bindir}/bzip2
install -m 755 bzip2recover bzgrep bzdiff bzmore  $RPM_BUILD_ROOT%{_bindir}/

cp -p bzip2.1 bzdiff.1 bzgrep.1 bzmore.1  $RPM_BUILD_ROOT%{_mandir}/man1/
ln -s bzip2 $RPM_BUILD_ROOT%{_bindir}/bunzip2
ln -s bzip2 $RPM_BUILD_ROOT%{_bindir}/bzcat
ln -s bzdiff $RPM_BUILD_ROOT%{_bindir}/bzcmp
ln -s bzmore $RPM_BUILD_ROOT%{_bindir}/bzless
ln -s bzgrep $RPM_BUILD_ROOT%{_bindir}/bzegrep
ln -s bzgrep $RPM_BUILD_ROOT%{_bindir}/bzfgrep
ln -s libbz2.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libbz2.so.1
ln -s libbz2.so.1 $RPM_BUILD_ROOT%{_libdir}/libbz2.so
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzip2recover.1
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bunzip2.1
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzcat.1
ln -s bzdiff.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzcmp.1
ln -s bzmore.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzless.1
ln -s bzgrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzegrep.1
ln -s bzgrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzfgrep.1

%files
/usr/bin/bunzip2
/usr/bin/bzcat
/usr/bin/bzcmp
/usr/bin/bzdiff
/usr/bin/bzegrep
/usr/bin/bzfgrep
/usr/bin/bzgrep
/usr/bin/bzip2
/usr/bin/bzip2recover
/usr/bin/bzless
/usr/bin/bzmore
/usr/include/bzlib.h
/usr/lib64/libbz2.a
/usr/lib64/libbz2.so
/usr/lib64/libbz2.so.1
/usr/lib64/libbz2.so.1.0.6
/usr/share/man/man1/bunzip2.1.gz
/usr/share/man/man1/bzcat.1.gz
/usr/share/man/man1/bzcmp.1.gz
/usr/share/man/man1/bzdiff.1.gz
/usr/share/man/man1/bzegrep.1.gz
/usr/share/man/man1/bzfgrep.1.gz
/usr/share/man/man1/bzgrep.1.gz
/usr/share/man/man1/bzip2.1.gz
/usr/share/man/man1/bzip2recover.1.gz
/usr/share/man/man1/bzless.1.gz
/usr/share/man/man1/bzmore.1.gz


%changelog
# let's skip this for now
