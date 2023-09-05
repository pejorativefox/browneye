Name:       grep
Version:    3.11
Release:    1
Summary:    Text searching cli tool
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. 

%prep
%setup -q

%build
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/egrep
/usr/bin/fgrep
/usr/bin/grep
/usr/share/info/grep.info.gz
/usr/share/locale/af/LC_MESSAGES/grep.mo
/usr/share/locale/be/LC_MESSAGES/grep.mo
/usr/share/locale/bg/LC_MESSAGES/grep.mo
/usr/share/locale/ca/LC_MESSAGES/grep.mo
/usr/share/locale/cs/LC_MESSAGES/grep.mo
/usr/share/locale/da/LC_MESSAGES/grep.mo
/usr/share/locale/de/LC_MESSAGES/grep.mo
/usr/share/locale/el/LC_MESSAGES/grep.mo
/usr/share/locale/eo/LC_MESSAGES/grep.mo
/usr/share/locale/es/LC_MESSAGES/grep.mo
/usr/share/locale/et/LC_MESSAGES/grep.mo
/usr/share/locale/eu/LC_MESSAGES/grep.mo
/usr/share/locale/fi/LC_MESSAGES/grep.mo
/usr/share/locale/fr/LC_MESSAGES/grep.mo
/usr/share/locale/ga/LC_MESSAGES/grep.mo
/usr/share/locale/gl/LC_MESSAGES/grep.mo
/usr/share/locale/he/LC_MESSAGES/grep.mo
/usr/share/locale/hr/LC_MESSAGES/grep.mo
/usr/share/locale/hu/LC_MESSAGES/grep.mo
/usr/share/locale/id/LC_MESSAGES/grep.mo
/usr/share/locale/it/LC_MESSAGES/grep.mo
/usr/share/locale/ja/LC_MESSAGES/grep.mo
/usr/share/locale/ko/LC_MESSAGES/grep.mo
/usr/share/locale/ky/LC_MESSAGES/grep.mo
/usr/share/locale/lt/LC_MESSAGES/grep.mo
/usr/share/locale/nb/LC_MESSAGES/grep.mo
/usr/share/locale/nl/LC_MESSAGES/grep.mo
/usr/share/locale/pa/LC_MESSAGES/grep.mo
/usr/share/locale/pl/LC_MESSAGES/grep.mo
/usr/share/locale/pt/LC_MESSAGES/grep.mo
/usr/share/locale/pt_BR/LC_MESSAGES/grep.mo
/usr/share/locale/ro/LC_MESSAGES/grep.mo
/usr/share/locale/ru/LC_MESSAGES/grep.mo
/usr/share/locale/sk/LC_MESSAGES/grep.mo
/usr/share/locale/sl/LC_MESSAGES/grep.mo
/usr/share/locale/sr/LC_MESSAGES/grep.mo
/usr/share/locale/sv/LC_MESSAGES/grep.mo
/usr/share/locale/th/LC_MESSAGES/grep.mo
/usr/share/locale/tr/LC_MESSAGES/grep.mo
/usr/share/locale/uk/LC_MESSAGES/grep.mo
/usr/share/locale/vi/LC_MESSAGES/grep.mo
/usr/share/locale/ka/LC_MESSAGES/grep.mo
/usr/share/locale/ta/LC_MESSAGES/grep.mo
/usr/share/locale/zh_CN/LC_MESSAGES/grep.mo
/usr/share/locale/zh_TW/LC_MESSAGES/grep.mo
/usr/share/man/man1/grep.1.gz


%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump
