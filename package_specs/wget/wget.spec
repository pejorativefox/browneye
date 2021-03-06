Name:       wget
Version:    1.20.1
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
%configure --sysconfdir=/etc  \
           --with-ssl=openssl
%make_build 

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/wgetrc
/usr/bin/wget
/usr/share/info/wget.info.gz
/usr/share/locale/be/LC_MESSAGES/wget.mo
/usr/share/locale/bg/LC_MESSAGES/wget.mo
/usr/share/locale/ca/LC_MESSAGES/wget.mo
/usr/share/locale/cs/LC_MESSAGES/wget.mo
/usr/share/locale/da/LC_MESSAGES/wget.mo
/usr/share/locale/de/LC_MESSAGES/wget.mo
/usr/share/locale/el/LC_MESSAGES/wget.mo
/usr/share/locale/en_GB/LC_MESSAGES/wget.mo
/usr/share/locale/eo/LC_MESSAGES/wget.mo
/usr/share/locale/es/LC_MESSAGES/wget.mo
/usr/share/locale/et/LC_MESSAGES/wget.mo
/usr/share/locale/eu/LC_MESSAGES/wget.mo
/usr/share/locale/fi/LC_MESSAGES/wget.mo
/usr/share/locale/fr/LC_MESSAGES/wget.mo
/usr/share/locale/ga/LC_MESSAGES/wget.mo
/usr/share/locale/gl/LC_MESSAGES/wget.mo
/usr/share/locale/he/LC_MESSAGES/wget.mo
/usr/share/locale/hr/LC_MESSAGES/wget.mo
/usr/share/locale/hu/LC_MESSAGES/wget.mo
/usr/share/locale/id/LC_MESSAGES/wget.mo
/usr/share/locale/it/LC_MESSAGES/wget.mo
/usr/share/locale/ja/LC_MESSAGES/wget.mo
/usr/share/locale/lt/LC_MESSAGES/wget.mo
/usr/share/locale/nb/LC_MESSAGES/wget.mo
/usr/share/locale/nl/LC_MESSAGES/wget.mo
/usr/share/locale/pl/LC_MESSAGES/wget.mo
/usr/share/locale/pt/LC_MESSAGES/wget.mo
/usr/share/locale/pt_BR/LC_MESSAGES/wget.mo
/usr/share/locale/ro/LC_MESSAGES/wget.mo
/usr/share/locale/ru/LC_MESSAGES/wget.mo
/usr/share/locale/sk/LC_MESSAGES/wget.mo
/usr/share/locale/sl/LC_MESSAGES/wget.mo
/usr/share/locale/sr/LC_MESSAGES/wget.mo
/usr/share/locale/sv/LC_MESSAGES/wget.mo
/usr/share/locale/tr/LC_MESSAGES/wget.mo
/usr/share/locale/uk/LC_MESSAGES/wget.mo
/usr/share/locale/vi/LC_MESSAGES/wget.mo
/usr/share/locale/zh_CN/LC_MESSAGES/wget.mo
/usr/share/locale/zh_TW/LC_MESSAGES/wget.mo
/usr/share/man/man1/wget.1.gz

%changelog
# let's skip this for now
