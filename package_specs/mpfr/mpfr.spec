Name:       mpfr
Version:    4.0.2
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
%configure --disable-static --enable-thread-safe --docdir=/usr/share/doc/mpfr-4.0.2
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/mpf2mpfr.h
/usr/include/mpfr.h
/usr/lib64/libmpfr.la
/usr/lib64/libmpfr.so
/usr/lib64/libmpfr.so.6
/usr/lib64/libmpfr.so.6.0.2
/usr/lib64/pkgconfig/mpfr.pc
/usr/share/doc/mpfr-4.0.2/AUTHORS
/usr/share/doc/mpfr-4.0.2/BUGS
/usr/share/doc/mpfr-4.0.2/COPYING
/usr/share/doc/mpfr-4.0.2/COPYING.LESSER
/usr/share/doc/mpfr-4.0.2/FAQ.html
/usr/share/doc/mpfr-4.0.2/NEWS
/usr/share/doc/mpfr-4.0.2/TODO
/usr/share/doc/mpfr-4.0.2/examples/ReadMe
/usr/share/doc/mpfr-4.0.2/examples/can_round.c
/usr/share/doc/mpfr-4.0.2/examples/divworst.c
/usr/share/doc/mpfr-4.0.2/examples/rndo-add.c
/usr/share/doc/mpfr-4.0.2/examples/sample.c
/usr/share/doc/mpfr-4.0.2/examples/version.c
/usr/share/info/mpfr.info.gz




%changelog
# let's skip this for now
