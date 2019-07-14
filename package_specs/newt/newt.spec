Name:       newt
Version:    0.52.20
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz

%description
TODO

%prep
%setup -a 0

%build
sed -e 's/^LIBNEWT =/#&/' \
    -e '/install -m 644 $(LIBNEWT)/ s/^/#/' \
    -e 's/$(LIBNEWT)/$(LIBNEWTSONAME)/g' \
    -i Makefile.in
%configure --with-gpm-support
%make_build


%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/whiptail
/usr/include/newt.h
/usr/lib64/libnewt.so
/usr/lib64/libnewt.so.0.52
/usr/lib64/libnewt.so.0.52.20
/usr/lib64/pkgconfig/libnewt.pc
/usr/lib64/python2.7/site-packages/_snack.so
/usr/lib64/python2.7/site-packages/snack.py
/usr/lib64/python3.7/site-packages/_snack.so
/usr/lib64/python3.7/site-packages/snack.py
/usr/share/locale/ar/LC_MESSAGES/newt.mo
/usr/share/locale/as/LC_MESSAGES/newt.mo
/usr/share/locale/ast/LC_MESSAGES/newt.mo
/usr/share/locale/bal/LC_MESSAGES/newt.mo
/usr/share/locale/bg/LC_MESSAGES/newt.mo
/usr/share/locale/bn/LC_MESSAGES/newt.mo
/usr/share/locale/bn_IN/LC_MESSAGES/newt.mo
/usr/share/locale/bs/LC_MESSAGES/newt.mo
/usr/share/locale/ca/LC_MESSAGES/newt.mo
/usr/share/locale/cs/LC_MESSAGES/newt.mo
/usr/share/locale/cy/LC_MESSAGES/newt.mo
/usr/share/locale/da/LC_MESSAGES/newt.mo
/usr/share/locale/de/LC_MESSAGES/newt.mo
/usr/share/locale/dz/LC_MESSAGES/newt.mo
/usr/share/locale/el/LC_MESSAGES/newt.mo
/usr/share/locale/eo/LC_MESSAGES/newt.mo
/usr/share/locale/es/LC_MESSAGES/newt.mo
/usr/share/locale/et/LC_MESSAGES/newt.mo
/usr/share/locale/eu/LC_MESSAGES/newt.mo
/usr/share/locale/fa/LC_MESSAGES/newt.mo
/usr/share/locale/fi/LC_MESSAGES/newt.mo
/usr/share/locale/fr/LC_MESSAGES/newt.mo
/usr/share/locale/ga/LC_MESSAGES/newt.mo
/usr/share/locale/gl/LC_MESSAGES/newt.mo
/usr/share/locale/gu/LC_MESSAGES/newt.mo
/usr/share/locale/he/LC_MESSAGES/newt.mo
/usr/share/locale/hi/LC_MESSAGES/newt.mo
/usr/share/locale/hr/LC_MESSAGES/newt.mo
/usr/share/locale/hu/LC_MESSAGES/newt.mo
/usr/share/locale/ia/LC_MESSAGES/newt.mo
/usr/share/locale/id/LC_MESSAGES/newt.mo
/usr/share/locale/it/LC_MESSAGES/newt.mo
/usr/share/locale/ja/LC_MESSAGES/newt.mo
/usr/share/locale/ka/LC_MESSAGES/newt.mo
/usr/share/locale/km/LC_MESSAGES/newt.mo
/usr/share/locale/kn/LC_MESSAGES/newt.mo
/usr/share/locale/ko/LC_MESSAGES/newt.mo
/usr/share/locale/ku/LC_MESSAGES/newt.mo
/usr/share/locale/lt/LC_MESSAGES/newt.mo
/usr/share/locale/lv/LC_MESSAGES/newt.mo
/usr/share/locale/mg/LC_MESSAGES/newt.mo
/usr/share/locale/mk/LC_MESSAGES/newt.mo
/usr/share/locale/ml/LC_MESSAGES/newt.mo
/usr/share/locale/mr/LC_MESSAGES/newt.mo
/usr/share/locale/ms/LC_MESSAGES/newt.mo
/usr/share/locale/nb/LC_MESSAGES/newt.mo
/usr/share/locale/nds/LC_MESSAGES/newt.mo
/usr/share/locale/ne/LC_MESSAGES/newt.mo
/usr/share/locale/nl/LC_MESSAGES/newt.mo
/usr/share/locale/nn/LC_MESSAGES/newt.mo
/usr/share/locale/pa/LC_MESSAGES/newt.mo
/usr/share/locale/pl/LC_MESSAGES/newt.mo
/usr/share/locale/pt/LC_MESSAGES/newt.mo
/usr/share/locale/pt_BR/LC_MESSAGES/newt.mo
/usr/share/locale/ro/LC_MESSAGES/newt.mo
/usr/share/locale/ru/LC_MESSAGES/newt.mo
/usr/share/locale/sk/LC_MESSAGES/newt.mo
/usr/share/locale/sl/LC_MESSAGES/newt.mo
/usr/share/locale/sq/LC_MESSAGES/newt.mo
/usr/share/locale/sr/LC_MESSAGES/newt.mo
/usr/share/locale/sr@latin/LC_MESSAGES/newt.mo
/usr/share/locale/sv/LC_MESSAGES/newt.mo
/usr/share/locale/ta/LC_MESSAGES/newt.mo
/usr/share/locale/te/LC_MESSAGES/newt.mo
/usr/share/locale/tg/LC_MESSAGES/newt.mo
/usr/share/locale/th/LC_MESSAGES/newt.mo
/usr/share/locale/tl/LC_MESSAGES/newt.mo
/usr/share/locale/tr/LC_MESSAGES/newt.mo
/usr/share/locale/uk/LC_MESSAGES/newt.mo
/usr/share/locale/vi/LC_MESSAGES/newt.mo
/usr/share/locale/wo/LC_MESSAGES/newt.mo
/usr/share/locale/xh/LC_MESSAGES/newt.mo
/usr/share/locale/zh_CN/LC_MESSAGES/newt.mo
/usr/share/locale/zh_TW/LC_MESSAGES/newt.mo
/usr/share/man/man1/whiptail.1.gz


%changelog
# let's skip this for now

