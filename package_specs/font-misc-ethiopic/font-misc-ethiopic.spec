Name:       font-misc-ethiopic
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
/usr/share/fonts/X11/OTF/GohaTibebZemen.otf
/usr/share/fonts/X11/OTF/fonts.dir
/usr/share/fonts/X11/OTF/fonts.scale
/usr/share/fonts/X11/TTF/GohaTibebZemen.ttf
/usr/share/fonts/X11/TTF/fonts.dir
/usr/share/fonts/X11/TTF/fonts.scale

%changelog
# let's skip this for now

