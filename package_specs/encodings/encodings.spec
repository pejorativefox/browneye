Name:       encodings
Version:    1.0.4
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: util-macros

%description
TODO

%prep
%setup -a 0

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/share/fonts/X11/encodings/adobe-dingbats.enc.gz
/usr/share/fonts/X11/encodings/adobe-standard.enc.gz
/usr/share/fonts/X11/encodings/adobe-symbol.enc.gz
/usr/share/fonts/X11/encodings/armscii-8.enc.gz
/usr/share/fonts/X11/encodings/ascii-0.enc.gz
/usr/share/fonts/X11/encodings/dec-special.enc.gz
/usr/share/fonts/X11/encodings/encodings.dir
/usr/share/fonts/X11/encodings/ibm-cp437.enc.gz
/usr/share/fonts/X11/encodings/ibm-cp850.enc.gz
/usr/share/fonts/X11/encodings/ibm-cp852.enc.gz
/usr/share/fonts/X11/encodings/ibm-cp866.enc.gz
/usr/share/fonts/X11/encodings/iso8859-11.enc.gz
/usr/share/fonts/X11/encodings/iso8859-13.enc.gz
/usr/share/fonts/X11/encodings/iso8859-16.enc.gz
/usr/share/fonts/X11/encodings/iso8859-6.16.enc.gz
/usr/share/fonts/X11/encodings/iso8859-6.8x.enc.gz
/usr/share/fonts/X11/encodings/large/big5.eten-0.enc.gz
/usr/share/fonts/X11/encodings/large/big5hkscs-0.enc.gz
/usr/share/fonts/X11/encodings/large/cns11643-1.enc.gz
/usr/share/fonts/X11/encodings/large/cns11643-2.enc.gz
/usr/share/fonts/X11/encodings/large/cns11643-3.enc.gz
/usr/share/fonts/X11/encodings/large/encodings.dir
/usr/share/fonts/X11/encodings/large/gb18030-0.enc.gz
/usr/share/fonts/X11/encodings/large/gb18030.2000-0.enc.gz
/usr/share/fonts/X11/encodings/large/gb18030.2000-1.enc.gz
/usr/share/fonts/X11/encodings/large/gb2312.1980-0.enc.gz
/usr/share/fonts/X11/encodings/large/gbk-0.enc.gz
/usr/share/fonts/X11/encodings/large/jisx0201.1976-0.enc.gz
/usr/share/fonts/X11/encodings/large/jisx0208.1990-0.enc.gz
/usr/share/fonts/X11/encodings/large/jisx0212.1990-0.enc.gz
/usr/share/fonts/X11/encodings/large/ksc5601.1987-0.enc.gz
/usr/share/fonts/X11/encodings/large/ksc5601.1992-3.enc.gz
/usr/share/fonts/X11/encodings/large/sun.unicode.india-0.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1250.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1251.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1252.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1253.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1254.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1255.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1256.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1257.enc.gz
/usr/share/fonts/X11/encodings/microsoft-cp1258.enc.gz
/usr/share/fonts/X11/encodings/microsoft-win3.1.enc.gz
/usr/share/fonts/X11/encodings/mulearabic-0.enc.gz
/usr/share/fonts/X11/encodings/mulearabic-1.enc.gz
/usr/share/fonts/X11/encodings/mulearabic-2.enc.gz
/usr/share/fonts/X11/encodings/mulelao-1.enc.gz
/usr/share/fonts/X11/encodings/suneu-greek.enc.gz
/usr/share/fonts/X11/encodings/tcvn-0.enc.gz
/usr/share/fonts/X11/encodings/tis620-2.enc.gz
/usr/share/fonts/X11/encodings/viscii1.1-1.enc.gz

%changelog
# let's skip this for now

