Name:       gettext
Version:    0.19.8.1
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
sed -i '/^TESTS =/d' gettext-runtime/tests/Makefile.in &&
sed -i 's/test-lock..EXEEXT.//' gettext-tools/gnulib-tests/Makefile.in
sed -e '/AppData/{N;N;p;s/\.appdata\./.metainfo./}' \
    -i gettext-tools/its/appdata.loc

%configure --disable-static \
           --docdir=/usr/share/doc/gettext-0.19.8.1
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
chmod -v 0755 %{buildroot}/usr/lib64/preloadable_libintl.so
rm -rf %{buildroot}/usr/share/doc/gettext-0.19.8.1/examples

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
/usr/lib64/gettext/cldr-plurals
/usr/lib64/gettext/hostname
/usr/lib64/gettext/project-id
/usr/lib64/gettext/urlget
/usr/lib64/gettext/user-email
/usr/lib64/libasprintf.so
/usr/lib64/libasprintf.so.0
/usr/lib64/libasprintf.so.0.0.0
/usr/lib64/libgettextlib-0.19.8.1.so
/usr/lib64/libgettextlib.so
/usr/lib64/libgettextpo.so
/usr/lib64/libgettextpo.so.0
/usr/lib64/libgettextpo.so.0.5.4
/usr/lib64/libgettextsrc-0.19.8.1.so
/usr/lib64/libgettextsrc.so
/usr/lib64/preloadable_libintl.so
/usr/share/

%changelog
# let's skip this for now
