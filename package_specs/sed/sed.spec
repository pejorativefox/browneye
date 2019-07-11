Name:       sed
Version:    4.7
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
sed -i 's/usr/tools/'                 build-aux/help2man
sed -i 's/testsuite.panic-tests.sh//' Makefile.in
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*


%files
/usr/bin/sed
/usr/share/info/sed.info.gz
/usr/share/locale/af/LC_MESSAGES/sed.mo
/usr/share/locale/ast/LC_MESSAGES/sed.mo
/usr/share/locale/bg/LC_MESSAGES/sed.mo
/usr/share/locale/ca/LC_MESSAGES/sed.mo
/usr/share/locale/cs/LC_MESSAGES/sed.mo
/usr/share/locale/da/LC_MESSAGES/sed.mo
/usr/share/locale/de/LC_MESSAGES/sed.mo
/usr/share/locale/el/LC_MESSAGES/sed.mo
/usr/share/locale/eo/LC_MESSAGES/sed.mo
/usr/share/locale/es/LC_MESSAGES/sed.mo
/usr/share/locale/et/LC_MESSAGES/sed.mo
/usr/share/locale/eu/LC_MESSAGES/sed.mo
/usr/share/locale/fi/LC_MESSAGES/sed.mo
/usr/share/locale/fr/LC_MESSAGES/sed.mo
/usr/share/locale/ga/LC_MESSAGES/sed.mo
/usr/share/locale/gl/LC_MESSAGES/sed.mo
/usr/share/locale/he/LC_MESSAGES/sed.mo
/usr/share/locale/hr/LC_MESSAGES/sed.mo
/usr/share/locale/hu/LC_MESSAGES/sed.mo
/usr/share/locale/id/LC_MESSAGES/sed.mo
/usr/share/locale/it/LC_MESSAGES/sed.mo
/usr/share/locale/ja/LC_MESSAGES/sed.mo
/usr/share/locale/ko/LC_MESSAGES/sed.mo
/usr/share/locale/nb/LC_MESSAGES/sed.mo
/usr/share/locale/nl/LC_MESSAGES/sed.mo
/usr/share/locale/pl/LC_MESSAGES/sed.mo
/usr/share/locale/pt/LC_MESSAGES/sed.mo
/usr/share/locale/pt_BR/LC_MESSAGES/sed.mo
/usr/share/locale/ro/LC_MESSAGES/sed.mo
/usr/share/locale/ru/LC_MESSAGES/sed.mo
/usr/share/locale/sk/LC_MESSAGES/sed.mo
/usr/share/locale/sl/LC_MESSAGES/sed.mo
/usr/share/locale/sr/LC_MESSAGES/sed.mo
/usr/share/locale/sv/LC_MESSAGES/sed.mo
/usr/share/locale/tr/LC_MESSAGES/sed.mo
/usr/share/locale/uk/LC_MESSAGES/sed.mo
/usr/share/locale/vi/LC_MESSAGES/sed.mo
/usr/share/locale/zh_CN/LC_MESSAGES/sed.mo
/usr/share/locale/zh_TW/LC_MESSAGES/sed.mo
/usr/share/man/man1/sed.1.gz

%changelog
# let's skip this for now
