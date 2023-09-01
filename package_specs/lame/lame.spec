Name:       lame
Version:    3.100
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
%configure --enable-mp3rtp --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/mp3rtp
/usr/bin/lame
/usr/include/lame/lame.h
/usr/lib64/libmp3lame.so
/usr/lib64/libmp3lame.so.0
/usr/lib64/libmp3lame.so.0.0.0
/usr/share/doc/lame/html/about.html
/usr/share/doc/lame/html/abr.html
/usr/share/doc/lame/html/cbr.html
/usr/share/doc/lame/html/contact.html
/usr/share/doc/lame/html/contributors.html
/usr/share/doc/lame/html/detailed.html
/usr/share/doc/lame/html/history.html
/usr/share/doc/lame/html/index.html
/usr/share/doc/lame/html/introduction.html
/usr/share/doc/lame/html/links.html
/usr/share/doc/lame/html/list.html
/usr/share/doc/lame/html/ms_stereo.html
/usr/share/doc/lame/html/usage.html
/usr/share/doc/lame/html/vbr.html
/usr/share/man/man1/lame.1.gz


%changelog
# let's skip this for now

