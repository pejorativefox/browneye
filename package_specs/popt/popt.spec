# popt-1.16.tar.gz
Name:       popt
Version:    1.16
Release:    1
Summary:    popt command line option parsing library.
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

Provides: pkgconfig(popt)

%description
popt command line option parsing library.

%prep
%setup -q -a0

%build
%configure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/popt.h
/usr/lib/pkgconfig/popt.pc
/usr/lib64/libpopt.so
/usr/lib64/libpopt.so.0
/usr/lib64/libpopt.so.0.0.0
/usr/share/locale/cs/LC_MESSAGES/popt.mo
/usr/share/locale/da/LC_MESSAGES/popt.mo
/usr/share/locale/de/LC_MESSAGES/popt.mo
/usr/share/locale/eo/LC_MESSAGES/popt.mo
/usr/share/locale/es/LC_MESSAGES/popt.mo
/usr/share/locale/fi/LC_MESSAGES/popt.mo
/usr/share/locale/fr/LC_MESSAGES/popt.mo
/usr/share/locale/ga/LC_MESSAGES/popt.mo
/usr/share/locale/gl/LC_MESSAGES/popt.mo
/usr/share/locale/hu/LC_MESSAGES/popt.mo
/usr/share/locale/id/LC_MESSAGES/popt.mo
/usr/share/locale/is/LC_MESSAGES/popt.mo
/usr/share/locale/it/LC_MESSAGES/popt.mo
/usr/share/locale/ja/LC_MESSAGES/popt.mo
/usr/share/locale/ko/LC_MESSAGES/popt.mo
/usr/share/locale/lv/LC_MESSAGES/popt.mo
/usr/share/locale/nb/LC_MESSAGES/popt.mo
/usr/share/locale/nl/LC_MESSAGES/popt.mo
/usr/share/locale/pl/LC_MESSAGES/popt.mo
/usr/share/locale/pt/LC_MESSAGES/popt.mo
/usr/share/locale/ro/LC_MESSAGES/popt.mo
/usr/share/locale/ru/LC_MESSAGES/popt.mo
/usr/share/locale/sk/LC_MESSAGES/popt.mo
/usr/share/locale/sl/LC_MESSAGES/popt.mo
/usr/share/locale/sv/LC_MESSAGES/popt.mo
/usr/share/locale/th/LC_MESSAGES/popt.mo
/usr/share/locale/tr/LC_MESSAGES/popt.mo
/usr/share/locale/uk/LC_MESSAGES/popt.mo
/usr/share/locale/vi/LC_MESSAGES/popt.mo
/usr/share/locale/wa/LC_MESSAGES/popt.mo
/usr/share/locale/zh_CN/LC_MESSAGES/popt.mo
/usr/share/locale/zh_TW/LC_MESSAGES/popt.mo
/usr/share/man/man3/popt.3.gz


%changelog
# let's skip this for now
