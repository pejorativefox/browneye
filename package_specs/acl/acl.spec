Name:       acl
Version:    2.2.53
Release:    1
Summary:    Linux access control lists.
License:    LGPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The Acl package contains utilities to administer Access Control Lists, which are used to
define more fine-grained discretionary access rights for files and directories. 

%prep
%setup

%build
%configure --disable-static       \
           --libexecdir=/usr/lib  \
           --docdir=/usr/share/doc/acl-2.2.53
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
/usr/lib64/libacl.la
/usr/lib64/libacl.so
/usr/lib64/libacl.so.1
/usr/lib64/libacl.so.1.1.2253
/usr/lib64/pkgconfig/libacl.pc
/usr/share/doc/acl-2.2.53/*
/usr/share/locale/de/LC_MESSAGES/acl.mo
/usr/share/locale/en@boldquot/LC_MESSAGES/acl.mo
/usr/share/locale/en@quot/LC_MESSAGES/acl.mo
/usr/share/locale/es/LC_MESSAGES/acl.mo
/usr/share/locale/fr/LC_MESSAGES/acl.mo
/usr/share/locale/gl/LC_MESSAGES/acl.mo
/usr/share/locale/pl/LC_MESSAGES/acl.mo
/usr/share/locale/sv/LC_MESSAGES/acl.mo
/usr/share/man/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 2.2.53
- Initial RPM release
