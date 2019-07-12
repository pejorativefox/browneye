Name:       font-bh-ttf
Version:    1.0.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



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
/etc/fonts/conf.avail/42-luxi-mono.conf
/etc/fonts/conf.d/42-luxi-mono.conf
/usr/share/fonts/X11/TTF/fonts.dir
/usr/share/fonts/X11/TTF/fonts.scale
/usr/share/fonts/X11/TTF/luximb.ttf
/usr/share/fonts/X11/TTF/luximbi.ttf
/usr/share/fonts/X11/TTF/luximr.ttf
/usr/share/fonts/X11/TTF/luximri.ttf
/usr/share/fonts/X11/TTF/luxirb.ttf
/usr/share/fonts/X11/TTF/luxirbi.ttf
/usr/share/fonts/X11/TTF/luxirr.ttf
/usr/share/fonts/X11/TTF/luxirri.ttf
/usr/share/fonts/X11/TTF/luxisb.ttf
/usr/share/fonts/X11/TTF/luxisbi.ttf
/usr/share/fonts/X11/TTF/luxisr.ttf
/usr/share/fonts/X11/TTF/luxisri.ttf


%changelog
# let's skip this for now

