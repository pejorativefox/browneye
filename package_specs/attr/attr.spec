Name:       attr
Version:    2.5.1
Release:    1
Summary:    Commands for Manipulating Filesystem Extended Attributes
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Commands for Manipulating Filesystem Extended Attributes

%prep
%setup

%build
%configure  --disable-static  \
            --sysconfdir=/etc \
            --docdir=/usr/share/doc/attr-%{version}
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
/usr/lib64/libattr.so.1.1.2501
/usr/lib64/pkgconfig/libattr.pc
/usr/share/doc/
/usr/share/locale/
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.4.48
- Initial RPM

