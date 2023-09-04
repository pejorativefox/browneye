Name:       flex
Version:    2.6.4
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
sed -i "/math.h/a #include <malloc.h>" src/flexdef.h
%configure --docdir=/usr/share/doc/flex-2.6.4
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/flex
/usr/bin/flex++
/usr/include/FlexLexer.h
/usr/lib64/libfl.a
/usr/lib64/libfl.so
/usr/lib64/libfl.so.2
/usr/lib64/libfl.so.2.0.0
/usr/share/doc/flex-2.6.4/AUTHORS
/usr/share/doc/flex-2.6.4/COPYING
/usr/share/doc/flex-2.6.4/NEWS
/usr/share/doc/flex-2.6.4/ONEWS
/usr/share/doc/flex-2.6.4/README.md
/usr/share/info/flex.info-1.gz
/usr/share/info/flex.info-2.gz
/usr/share/info/flex.info.gz
/usr/share/locale/ca/LC_MESSAGES/flex.mo
/usr/share/locale/da/LC_MESSAGES/flex.mo
/usr/share/locale/de/LC_MESSAGES/flex.mo
/usr/share/locale/en@boldquot/LC_MESSAGES/flex.mo
/usr/share/locale/en@quot/LC_MESSAGES/flex.mo
/usr/share/locale/eo/LC_MESSAGES/flex.mo
/usr/share/locale/es/LC_MESSAGES/flex.mo
/usr/share/locale/fi/LC_MESSAGES/flex.mo
/usr/share/locale/fr/LC_MESSAGES/flex.mo
/usr/share/locale/ga/LC_MESSAGES/flex.mo
/usr/share/locale/hr/LC_MESSAGES/flex.mo
/usr/share/locale/ko/LC_MESSAGES/flex.mo
/usr/share/locale/nl/LC_MESSAGES/flex.mo
/usr/share/locale/pl/LC_MESSAGES/flex.mo
/usr/share/locale/pt_BR/LC_MESSAGES/flex.mo
/usr/share/locale/ro/LC_MESSAGES/flex.mo
/usr/share/locale/ru/LC_MESSAGES/flex.mo
/usr/share/locale/sr/LC_MESSAGES/flex.mo
/usr/share/locale/sv/LC_MESSAGES/flex.mo
/usr/share/locale/tr/LC_MESSAGES/flex.mo
/usr/share/locale/vi/LC_MESSAGES/flex.mo
/usr/share/locale/zh_CN/LC_MESSAGES/flex.mo
/usr/share/locale/zh_TW/LC_MESSAGES/flex.mo
/usr/share/man/man1/flex.1.gz

%changelog
# let's skip this for now
