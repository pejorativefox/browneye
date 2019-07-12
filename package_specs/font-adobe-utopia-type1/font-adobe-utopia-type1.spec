Name:       font-adobe-utopia-type1
Version:    1.0.4
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
/usr/share/fonts/X11/Type1/UTBI____.afm
/usr/share/fonts/X11/Type1/UTBI____.pfa
/usr/share/fonts/X11/Type1/UTB_____.afm
/usr/share/fonts/X11/Type1/UTB_____.pfa
/usr/share/fonts/X11/Type1/UTI_____.afm
/usr/share/fonts/X11/Type1/UTI_____.pfa
/usr/share/fonts/X11/Type1/UTRG____.afm
/usr/share/fonts/X11/Type1/UTRG____.pfa
/usr/share/fonts/X11/Type1/fonts.dir
/usr/share/fonts/X11/Type1/fonts.scale

%changelog
# let's skip this for now

