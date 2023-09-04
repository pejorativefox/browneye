Name:       acl
Version:    2.3.1
Release:    1
Summary:    Linux access control lists.
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
The Acl package contains utilities to administer Access Control Lists, which are used to
define more fine-grained discretionary access rights for files and directories. 

%prep
%setup

%build
%configure --disable-static       \
           --libexecdir=/usr/lib  \
           --docdir=/usr/share/doc/acl-%{version}
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/chacl
/usr/bin/getfacl
/usr/bin/setfacl
/usr/include/acl/libacl.h
/usr/include/sys/acl.h
/usr/lib64/libacl.so
/usr/lib64/libacl.so.1
/usr/lib64/libacl.so.1.1.2301
/usr/lib64/pkgconfig/libacl.pc
/usr/share/doc/acl-%{version}/
/usr/share/locale/
/usr/share/man/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.2.53
- Initial RPM release
