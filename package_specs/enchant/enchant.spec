Name:       enchant
Version:    2.2.11
Release:    1
Summary:    Spell check library
License:    LGPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Spell check library

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/enchant-2
/usr/bin/enchant-lsmod-2
/usr/include/enchant-2/enchant++.h
/usr/include/enchant-2/enchant-provider.h
/usr/include/enchant-2/enchant.h
/usr/lib64/libenchant-2.a
/usr/lib64/libenchant-2.la
/usr/lib64/libenchant-2.so
/usr/lib64/libenchant-2.so.2
/usr/lib64/libenchant-2.so.2.2.11
/usr/lib64/pkgconfig/enchant-2.pc
/usr/share/enchant/enchant.ordering
/usr/share/man/man1/enchant-2.1.gz
/usr/share/man/man1/enchant-lsmod-2.1.gz

%changelog
* Wed Sep 09 2020 Chris Statzer <chris.statzer@qq.com> 2.2.11
- Initial RPM

