Name:       tar
Version:    1.31
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
sed -i 's/abort.*/FALLTHROUGH;/' src/extract.c
export FORCE_UNSAFE_CONFIGURE=1
%configure 
%make_build
unset FORCE_UNSAFE_CONFIGURE
%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/tar
/usr/libexec/rmt
/usr/share/info/tar.info-1.gz
/usr/share/info/tar.info-2.gz
/usr/share/info/tar.info.gz
/usr/share/locale/bg/LC_MESSAGES/tar.mo
/usr/share/locale/ca/LC_MESSAGES/tar.mo
/usr/share/locale/cs/LC_MESSAGES/tar.mo
/usr/share/locale/da/LC_MESSAGES/tar.mo
/usr/share/locale/de/LC_MESSAGES/tar.mo
/usr/share/locale/el/LC_MESSAGES/tar.mo
/usr/share/locale/eo/LC_MESSAGES/tar.mo
/usr/share/locale/es/LC_MESSAGES/tar.mo
/usr/share/locale/et/LC_MESSAGES/tar.mo
/usr/share/locale/eu/LC_MESSAGES/tar.mo
/usr/share/locale/fi/LC_MESSAGES/tar.mo
/usr/share/locale/fr/LC_MESSAGES/tar.mo
/usr/share/locale/ga/LC_MESSAGES/tar.mo
/usr/share/locale/gl/LC_MESSAGES/tar.mo
/usr/share/locale/hr/LC_MESSAGES/tar.mo
/usr/share/locale/hu/LC_MESSAGES/tar.mo
/usr/share/locale/id/LC_MESSAGES/tar.mo
/usr/share/locale/it/LC_MESSAGES/tar.mo
/usr/share/locale/ja/LC_MESSAGES/tar.mo
/usr/share/locale/ko/LC_MESSAGES/tar.mo
/usr/share/locale/ky/LC_MESSAGES/tar.mo
/usr/share/locale/ms/LC_MESSAGES/tar.mo
/usr/share/locale/nb/LC_MESSAGES/tar.mo
/usr/share/locale/nl/LC_MESSAGES/tar.mo
/usr/share/locale/pl/LC_MESSAGES/tar.mo
/usr/share/locale/pt/LC_MESSAGES/tar.mo
/usr/share/locale/pt_BR/LC_MESSAGES/tar.mo
/usr/share/locale/ro/LC_MESSAGES/tar.mo
/usr/share/locale/ru/LC_MESSAGES/tar.mo
/usr/share/locale/sk/LC_MESSAGES/tar.mo
/usr/share/locale/sl/LC_MESSAGES/tar.mo
/usr/share/locale/sr/LC_MESSAGES/tar.mo
/usr/share/locale/sv/LC_MESSAGES/tar.mo
/usr/share/locale/tr/LC_MESSAGES/tar.mo
/usr/share/locale/uk/LC_MESSAGES/tar.mo
/usr/share/locale/vi/LC_MESSAGES/tar.mo
/usr/share/locale/zh_CN/LC_MESSAGES/tar.mo
/usr/share/locale/zh_TW/LC_MESSAGES/tar.mo
/usr/share/man/man1/tar.1.gz
/usr/share/man/man8/rmt.8.gz

%changelog
# let's skip this for now
