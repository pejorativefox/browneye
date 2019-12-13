Name:       gawk
Version:    4.2.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

Provides: /bin/gawk

%description
TODO

%prep
%setup -q -a0

%build
sed -i 's/extras//' Makefile.in
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-4.2.1
/usr/include/gawkapi.h
/usr/lib64/gawk/filefuncs.so
/usr/lib64/gawk/fnmatch.so
/usr/lib64/gawk/fork.so
/usr/lib64/gawk/inplace.so
/usr/lib64/gawk/intdiv.so
/usr/lib64/gawk/ordchr.so
/usr/lib64/gawk/readdir.so
/usr/lib64/gawk/readfile.so
/usr/lib64/gawk/revoutput.so
/usr/lib64/gawk/revtwoway.so
/usr/lib64/gawk/rwarray.so
/usr/lib64/gawk/time.so
/usr/libexec/awk/grcat
/usr/libexec/awk/pwcat
/usr/share/awk/assert.awk
/usr/share/awk/bits2str.awk
/usr/share/awk/cliff_rand.awk
/usr/share/awk/ctime.awk
/usr/share/awk/ftrans.awk
/usr/share/awk/getopt.awk
/usr/share/awk/gettime.awk
/usr/share/awk/group.awk
/usr/share/awk/have_mpfr.awk
/usr/share/awk/inplace.awk
/usr/share/awk/intdiv0.awk
/usr/share/awk/join.awk
/usr/share/awk/libintl.awk
/usr/share/awk/noassign.awk
/usr/share/awk/ord.awk
/usr/share/awk/passwd.awk
/usr/share/awk/processarray.awk
/usr/share/awk/quicksort.awk
/usr/share/awk/readable.awk
/usr/share/awk/readfile.awk
/usr/share/awk/rewind.awk
/usr/share/awk/round.awk
/usr/share/awk/shellquote.awk
/usr/share/awk/strtonum.awk
/usr/share/awk/walkarray.awk
/usr/share/awk/zerofile.awk
/usr/share/info/gawk.info.gz
/usr/share/info/gawkinet.info.gz
/usr/share/info/gawkworkflow.info.gz
/usr/share/locale/ca/LC_MESSAGES/gawk.mo
/usr/share/locale/da/LC_MESSAGES/gawk.mo
/usr/share/locale/de/LC_MESSAGES/gawk.mo
/usr/share/locale/es/LC_MESSAGES/gawk.mo
/usr/share/locale/fi/LC_MESSAGES/gawk.mo
/usr/share/locale/fr/LC_MESSAGES/gawk.mo
/usr/share/locale/id/LC_MESSAGES/gawk.mo
/usr/share/locale/it/LC_MESSAGES/gawk.mo
/usr/share/locale/ja/LC_MESSAGES/gawk.mo
/usr/share/locale/ms/LC_MESSAGES/gawk.mo
/usr/share/locale/nl/LC_MESSAGES/gawk.mo
/usr/share/locale/pl/LC_MESSAGES/gawk.mo
/usr/share/locale/pt_BR/LC_MESSAGES/gawk.mo
/usr/share/locale/sv/LC_MESSAGES/gawk.mo
/usr/share/locale/vi/LC_MESSAGES/gawk.mo
/usr/share/locale/zh_CN/LC_MESSAGES/gawk.mo
/usr/share/man/man1/gawk.1.gz
/usr/share/man/man3/filefuncs.3am.gz
/usr/share/man/man3/fnmatch.3am.gz
/usr/share/man/man3/fork.3am.gz
/usr/share/man/man3/inplace.3am.gz
/usr/share/man/man3/ordchr.3am.gz
/usr/share/man/man3/readdir.3am.gz
/usr/share/man/man3/readfile.3am.gz
/usr/share/man/man3/revoutput.3am.gz
/usr/share/man/man3/revtwoway.3am.gz
/usr/share/man/man3/rwarray.3am.gz
/usr/share/man/man3/time.3am.gz

%changelog
# let's skip this for now
