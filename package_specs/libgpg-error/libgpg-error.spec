Name:       libgpg-error
Version:    1.47
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2


%description
TODO

%prep
%setup -a 0

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
/usr/lib64/libgpg-error.so
/usr/lib64/libgpg-error.so.0
/usr/lib64/libgpg-error.so.0.34.0
/usr/lib64/pkgconfig/gpg-error.pc
/usr/share/aclocal/gpg-error.m4
/usr/share/aclocal/gpgrt.m4
/usr/share/common-lisp/source/gpg-error/gpg-error-codes.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error-package.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error.asd
/usr/share/common-lisp/source/gpg-error/gpg-error.lisp
/usr/share/info/gpgrt.info.gz
/usr/share/libgpg-error/errorref.txt
/usr/share/locale/cs/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/da/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/de/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/eo/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/es/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/fr/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/hu/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/it/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/ja/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/nl/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/pl/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/pt/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/ro/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/ru/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/sr/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/sv/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/uk/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/vi/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/zh_CN/LC_MESSAGES/libgpg-error.mo
/usr/share/locale/zh_TW/LC_MESSAGES/libgpg-error.mo
/usr/share/man/man1/gpgrt-config.1.gz
/usr/share/locale/tr/LC_MESSAGES/libgpg-error.mo

%changelog
# let's skip this for now

