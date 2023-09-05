Name:       gawk
Version:    5.2.2
Release:    1
Summary:    GNU pattern scanner
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

Provides: /bin/gawk

%description
Gawk is a powerful text-processing and data-manipulating tool

%prep
%setup -q

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
/usr/bin/gawk-%{version}
/usr/bin/gawkbug
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
/usr/share/awk/isnumeric.awk
/usr/share/awk/ns_passwd.awk
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
/usr/share/locale/
/usr/share/man/
/usr/share/info/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 5.2.2-1
- Version bump
