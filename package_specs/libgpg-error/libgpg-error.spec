Name:       libgpg-error
Version:    1.47
Release:    1
Summary:    GnuPG error library
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2


%description
The libgpg-error package contains a library that defines common error values for all GnuPG components

%prep
%setup -q

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/gpg-error
/usr/bin/gpgrt-config
/usr/bin/yat2m
/usr/include/gpg-error.h
/usr/include/gpgrt.h
/usr/share/aclocal/gpg-error.m4
/usr/share/aclocal/gpgrt.m4
/usr/share/common-lisp/source/gpg-error/gpg-error-codes.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error-package.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error.asd
/usr/share/common-lisp/source/gpg-error/gpg-error.lisp
/usr/share/info/gpgrt.info.gz
/usr/share/libgpg-error/errorref.txt
/usr/lib64/libgpg-error.so
/usr/lib64/libgpg-error.so.0
/usr/lib64/libgpg-error.so.0.34.0
/usr/lib64/pkgconfig/gpg-error.pc
/usr/share/locale/
/usr/share/man/man1/gpgrt-config.1.gz

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.47-1
- Version bump
