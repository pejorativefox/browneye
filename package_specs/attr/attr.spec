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
%setup

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
/usr/lib64/libattr.so
/usr/lib64/libattr.so.1
/usr/lib64/libattr.so.1.1.2448
/usr/lib64/pkgconfig/libattr.pc
/usr/share/doc/attr-2.4.48/CHANGES
/usr/share/doc/attr-2.4.48/COPYING
/usr/share/doc/attr-2.4.48/COPYING.LGPL
/usr/share/doc/attr-2.4.48/PORTING
/usr/share/locale/*
/usr/share/man/*


%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.4.48
- Initial RPM

