Name:       check
Version:    0.12.0
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
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
sed -i '1 s/tools/usr/' %{buildroot}/usr/bin/checkmk

%files
/usr/bin/checkmk
/usr/include/check.h
/usr/include/check_stdint.h
/usr/lib64/libcheck.a
/usr/lib64/libcheck.so
/usr/lib64/libcheck.so.0
/usr/lib64/libcheck.so.0.0.0
/usr/lib64/pkgconfig/check.pc
/usr/share/aclocal/check.m4
/usr/share/doc/check/COPYING.LESSER
/usr/share/doc/check/ChangeLog
/usr/share/doc/check/NEWS
/usr/share/doc/check/README
/usr/share/doc/check/example/Makefile.am
/usr/share/doc/check/example/README
/usr/share/doc/check/example/configure.ac
/usr/share/doc/check/example/src/Makefile.am
/usr/share/doc/check/example/src/main.c
/usr/share/doc/check/example/src/money.1.c
/usr/share/doc/check/example/src/money.1.h
/usr/share/doc/check/example/src/money.2.h
/usr/share/doc/check/example/src/money.3.c
/usr/share/doc/check/example/src/money.4.c
/usr/share/doc/check/example/src/money.5.c
/usr/share/doc/check/example/src/money.6.c
/usr/share/doc/check/example/src/money.c
/usr/share/doc/check/example/src/money.h
/usr/share/doc/check/example/tests/Makefile.am
/usr/share/doc/check/example/tests/check_money.1.c
/usr/share/doc/check/example/tests/check_money.2.c
/usr/share/doc/check/example/tests/check_money.3.c
/usr/share/doc/check/example/tests/check_money.6.c
/usr/share/doc/check/example/tests/check_money.7.c
/usr/share/doc/check/example/tests/check_money.c
/usr/share/info/check.info.gz
/usr/share/man/man1/checkmk.1.gz

%changelog
# let's skip this for now
