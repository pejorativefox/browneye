Name:       diffutils
Version:    3.7
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
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff
/usr/share/info/diffutils.info.gz
/usr/share/locale/bg/LC_MESSAGES/diffutils.mo
/usr/share/locale/ca/LC_MESSAGES/diffutils.mo
/usr/share/locale/cs/LC_MESSAGES/diffutils.mo
/usr/share/locale/da/LC_MESSAGES/diffutils.mo
/usr/share/locale/de/LC_MESSAGES/diffutils.mo
/usr/share/locale/el/LC_MESSAGES/diffutils.mo
/usr/share/locale/eo/LC_MESSAGES/diffutils.mo
/usr/share/locale/es/LC_MESSAGES/diffutils.mo
/usr/share/locale/fi/LC_MESSAGES/diffutils.mo
/usr/share/locale/fr/LC_MESSAGES/diffutils.mo
/usr/share/locale/ga/LC_MESSAGES/diffutils.mo
/usr/share/locale/gl/LC_MESSAGES/diffutils.mo
/usr/share/locale/he/LC_MESSAGES/diffutils.mo
/usr/share/locale/hr/LC_MESSAGES/diffutils.mo
/usr/share/locale/hu/LC_MESSAGES/diffutils.mo
/usr/share/locale/id/LC_MESSAGES/diffutils.mo
/usr/share/locale/it/LC_MESSAGES/diffutils.mo
/usr/share/locale/ja/LC_MESSAGES/diffutils.mo
/usr/share/locale/lv/LC_MESSAGES/diffutils.mo
/usr/share/locale/ms/LC_MESSAGES/diffutils.mo
/usr/share/locale/nb/LC_MESSAGES/diffutils.mo
/usr/share/locale/nl/LC_MESSAGES/diffutils.mo
/usr/share/locale/pl/LC_MESSAGES/diffutils.mo
/usr/share/locale/pt/LC_MESSAGES/diffutils.mo
/usr/share/locale/pt_BR/LC_MESSAGES/diffutils.mo
/usr/share/locale/ro/LC_MESSAGES/diffutils.mo
/usr/share/locale/ru/LC_MESSAGES/diffutils.mo
/usr/share/locale/sr/LC_MESSAGES/diffutils.mo
/usr/share/locale/sv/LC_MESSAGES/diffutils.mo
/usr/share/locale/tr/LC_MESSAGES/diffutils.mo
/usr/share/locale/uk/LC_MESSAGES/diffutils.mo
/usr/share/locale/vi/LC_MESSAGES/diffutils.mo
/usr/share/locale/zh_CN/LC_MESSAGES/diffutils.mo
/usr/share/locale/zh_TW/LC_MESSAGES/diffutils.mo
/usr/share/man/man1/cmp.1.gz
/usr/share/man/man1/diff.1.gz
/usr/share/man/man1/diff3.1.gz
/usr/share/man/man1/sdiff.1.gz

%changelog
# let's skip this for now
