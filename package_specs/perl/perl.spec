Name:       perl
Version:    5.38.0
Release:    1
Summary:    Perl programming language
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

AutoReq: no

Provides: /bin/perl

Requires: libc.so.6()(64bit), libcrypt.so.2()(64bit), libdl.so.2()(64bit), libgdbm.so.6()(64bit), libgdbm_compat.so.4()(64bit), libm.so.6()(64bit), libpthread.so.0()(64bit), librt.so.1()(64bit), libutil.so.1()(64bit)

%description
Perl programming language

%prep
%setup -q

%build
export BUILD_ZLIB=False
export BUILD_BZIP2=0
sh Configure -des                                         \
             -Dprefix=/usr                                \
             -Dvendorprefix=/usr                          \
             -Dprivlib=%{_libdir}/perl5/%{version}/core_perl      \
             -Darchlib=%{_libdir}/perl5/%{version}/core_perl      \
             -Dsitelib=%{_libdir}/perl5/%{version}/site_perl      \
             -Dsitearch=%{_libdir}/perl5/%{version}/site_perl     \
             -Dvendorlib=%{_libdir}/perl5/%{version}/vendor_perl  \
             -Dvendorarch=%{_libdir}/perl5/%{version}/vendor_perl \
             -Dman1dir=/usr/share/man/man1                \
             -Dman3dir=/usr/share/man/man3                \
             -Dpager="/usr/bin/less -isR"                 \
             -Duseshrplib                                 \
             -Dusethreads 
unset BUILD_ZLIB BUILD_BZIP2
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
rm %{buildroot}/usr/share/man/man3/Thread.3

%files -f ../../SOURCES/perl.filelist

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 5.38.0-1
- Version bump
