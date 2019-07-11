Name:       attr
Version:    2.4.48
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
%configure --disable-static  \
            --sysconfdir=/etc \
            --docdir=/usr/share/doc/attr-2.4.48
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/xattr.conf
/usr/bin/attr
/usr/bin/getfattr
/usr/bin/setfattr
/usr/include/attr/attributes.h
/usr/include/attr/error_context.h
/usr/include/attr/libattr.h
/usr/lib64/libattr.la
/usr/lib64/libattr.so
/usr/lib64/libattr.so.1
/usr/lib64/libattr.so.1.1.2448
/usr/lib64/pkgconfig/libattr.pc
/usr/share/doc/attr-2.4.48/CHANGES
/usr/share/doc/attr-2.4.48/COPYING
/usr/share/doc/attr-2.4.48/COPYING.LGPL
/usr/share/doc/attr-2.4.48/PORTING
/usr/share/locale/cs/LC_MESSAGES/attr.mo
/usr/share/locale/de/LC_MESSAGES/attr.mo
/usr/share/locale/en@boldquot/LC_MESSAGES/attr.mo
/usr/share/locale/en@quot/LC_MESSAGES/attr.mo
/usr/share/locale/es/LC_MESSAGES/attr.mo
/usr/share/locale/fr/LC_MESSAGES/attr.mo
/usr/share/locale/gl/LC_MESSAGES/attr.mo
/usr/share/locale/nl/LC_MESSAGES/attr.mo
/usr/share/locale/pl/LC_MESSAGES/attr.mo
/usr/share/locale/sv/LC_MESSAGES/attr.mo
/usr/share/man/man1/attr.1.gz
/usr/share/man/man1/getfattr.1.gz
/usr/share/man/man1/setfattr.1.gz
/usr/share/man/man3/attr_get.3.gz
/usr/share/man/man3/attr_getf.3.gz
/usr/share/man/man3/attr_list.3.gz
/usr/share/man/man3/attr_listf.3.gz
/usr/share/man/man3/attr_multi.3.gz
/usr/share/man/man3/attr_multif.3.gz
/usr/share/man/man3/attr_remove.3.gz
/usr/share/man/man3/attr_removef.3.gz
/usr/share/man/man3/attr_set.3.gz
/usr/share/man/man3/attr_setf.3.gz


%changelog
# let's skip this for now
