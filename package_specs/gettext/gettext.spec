Name:       gettext
Version:    0.22
Release:    1
Summary:    GNU Internationalization utilities
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
GNU Internationalization utilities

%prep
%setup -q

%build
%configure --disable-static \
           --docdir=/usr/share/doc/gettext-%{version}
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
chmod -v 0755 %{buildroot}/usr/lib64/preloadable_libintl.so
rm -rf %{buildroot}/usr/share/doc/gettext-%{version}/examples

%files
/usr/bin/autopoint
/usr/bin/envsubst
/usr/bin/gettext
/usr/bin/gettext.sh
/usr/bin/gettextize
/usr/bin/msgattrib
/usr/bin/msgcat
/usr/bin/msgcmp
/usr/bin/msgcomm
/usr/bin/msgconv
/usr/bin/msgen
/usr/bin/msgexec
/usr/bin/msgfilter
/usr/bin/msgfmt
/usr/bin/msggrep
/usr/bin/msginit
/usr/bin/msgmerge
/usr/bin/msgunfmt
/usr/bin/msguniq
/usr/bin/ngettext
/usr/bin/recode-sr-latin
/usr/bin/xgettext
/usr/include/autosprintf.h
/usr/include/gettext-po.h
/usr/include/textstyle.h
/usr/include/textstyle/stdbool.h
/usr/include/textstyle/version.h
/usr/include/textstyle/woe32dll.h
/usr/lib64/gettext/cldr-plurals
/usr/lib64/gettext/hostname
/usr/lib64/gettext/project-id
/usr/lib64/gettext/urlget
/usr/lib64/gettext/user-email
/usr/lib64/libasprintf.so
/usr/lib64/libasprintf.so.0
/usr/lib64/libasprintf.so.0.0.0
/usr/lib64/libgettextlib-0.22.so
/usr/lib64/libgettextlib.so
/usr/lib64/libgettextpo.so
/usr/lib64/libgettextpo.so.0
/usr/lib64/libgettextpo.so.0.5.9
/usr/lib64/libgettextsrc-0.22.so
/usr/lib64/libgettextsrc.so
/usr/lib64/libtextstyle.so
/usr/lib64/libtextstyle.so.0
/usr/lib64/libtextstyle.so.0.2.0
/usr/lib64/preloadable_libintl.so
/usr/share/info/libtextstyle.info.gz
/usr/share/aclocal/
/usr/share/doc/
/usr/share/gettext-%{version}/
/usr/share/gettext/
/usr/share/info/autosprintf.info.gz
/usr/share/info/gettext.info.gz
/usr/share/locale/
/usr/share/man/

%changelog
# let's skip this for now
