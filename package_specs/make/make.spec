Name:       make
Version:    4.2.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
sed -i '211,217 d; 219,229 d; 232 d' glob/glob.c
%configure 
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/make
/usr/include/gnumake.h
/usr/share/info/make.info-1.gz
/usr/share/info/make.info-2.gz
/usr/share/info/make.info.gz
/usr/share/locale/be/LC_MESSAGES/make.mo
/usr/share/locale/cs/LC_MESSAGES/make.mo
/usr/share/locale/da/LC_MESSAGES/make.mo
/usr/share/locale/de/LC_MESSAGES/make.mo
/usr/share/locale/es/LC_MESSAGES/make.mo
/usr/share/locale/fi/LC_MESSAGES/make.mo
/usr/share/locale/fr/LC_MESSAGES/make.mo
/usr/share/locale/ga/LC_MESSAGES/make.mo
/usr/share/locale/gl/LC_MESSAGES/make.mo
/usr/share/locale/he/LC_MESSAGES/make.mo
/usr/share/locale/hr/LC_MESSAGES/make.mo
/usr/share/locale/id/LC_MESSAGES/make.mo
/usr/share/locale/it/LC_MESSAGES/make.mo
/usr/share/locale/ja/LC_MESSAGES/make.mo
/usr/share/locale/ko/LC_MESSAGES/make.mo
/usr/share/locale/lt/LC_MESSAGES/make.mo
/usr/share/locale/nl/LC_MESSAGES/make.mo
/usr/share/locale/pl/LC_MESSAGES/make.mo
/usr/share/locale/pt_BR/LC_MESSAGES/make.mo
/usr/share/locale/ru/LC_MESSAGES/make.mo
/usr/share/locale/sv/LC_MESSAGES/make.mo
/usr/share/locale/tr/LC_MESSAGES/make.mo
/usr/share/locale/uk/LC_MESSAGES/make.mo
/usr/share/locale/vi/LC_MESSAGES/make.mo
/usr/share/locale/zh_CN/LC_MESSAGES/make.mo
/usr/share/man/man1/make.1.gz

%changelog
# let's skip this for now
