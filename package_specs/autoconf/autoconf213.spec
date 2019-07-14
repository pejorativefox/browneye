Name:       autoconf213
Version:    2.13
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    autoconf-%{version}.tar.gz
Patch:     autoconf-2.13-consolidated_fixes-1.patch

%description
TODO

%prep
%setup -a 0 -n autoconf-2.13
%patch -p1

%build
mv -v autoconf.texi autoconf213.texi
rm -v autoconf.info
%configure  --prefix=/usr --program-suffix=2.13
%make_build


%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/autoconf2.13
/usr/bin/autoheader2.13
/usr/bin/autoreconf2.13
/usr/bin/autoscan2.13
/usr/bin/autoupdate2.13
/usr/bin/ifnames2.13
/usr/share/autoconf-2.13/acconfig.h
/usr/share/autoconf-2.13/acfunctions
/usr/share/autoconf-2.13/acgeneral.m4
/usr/share/autoconf-2.13/acheaders
/usr/share/autoconf-2.13/acidentifiers
/usr/share/autoconf-2.13/acmakevars
/usr/share/autoconf-2.13/acoldnames.m4
/usr/share/autoconf-2.13/acprograms
/usr/share/autoconf-2.13/acspecific.m4
/usr/share/autoconf-2.13/autoconf.m4
/usr/share/autoconf-2.13/autoconf.m4f
/usr/share/autoconf-2.13/autoheader.m4
/usr/share/autoconf-2.13/autoheader.m4f


%changelog
# let's skip this for now

