Name:       libstemmer
Version:    1.0
Release:    1
Summary:    Snowball Stemming Algorithms.
License:    GPL
Source0:    libstemmer_c.tgz
Prefix:     /usr

%description
Snowball Stemming Algorithms.

%prep
%setup -n libstemmer_c

%build
sed -i -r "s|(^libstemmer.o:)|libstemmer.so: \$\(snowball_sources:.c=.o\)\n\
\t\$\(CC\) \$\(CFLAGS\) -shared \$\(LDFLAGS\) -Wl,-soname,libstemmer.so.0 \
-o \$\@.0.0.0 \$\^\n\1|" Makefile
make libstemmer.so %{?_smp_mflags} CFLAGS="%{optflags} -fPIC -Iinclude" LDFLAGS="$RPM_LD_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -p -D -m 755	libstemmer.so.0.0.0	%{buildroot}%{_libdir}/
ln -s libstemmer.so.0.0.0	%{buildroot}%{_libdir}/libstemmer.so.0
ln -s libstemmer.so.0.0.0	%{buildroot}%{_libdir}/libstemmer.so
install -p -D -m 644	include/*	%{buildroot}%{_includedir}/

%files
/usr/include/libstemmer.h
/usr/lib64/libstemmer.so
/usr/lib64/libstemmer.so.0
/usr/lib64/libstemmer.so.0.0.0

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.0
- Initial RPM

