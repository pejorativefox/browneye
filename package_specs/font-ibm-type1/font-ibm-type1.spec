Name:       font-ibm-type1
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
/usr/share/fonts/X11/Type1/cour.afm
/usr/share/fonts/X11/Type1/cour.pfa
/usr/share/fonts/X11/Type1/courb.afm
/usr/share/fonts/X11/Type1/courb.pfa
/usr/share/fonts/X11/Type1/courbi.afm
/usr/share/fonts/X11/Type1/courbi.pfa
/usr/share/fonts/X11/Type1/couri.afm
/usr/share/fonts/X11/Type1/couri.pfa
/usr/share/fonts/X11/Type1/fonts.dir
/usr/share/fonts/X11/Type1/fonts.scale

%changelog
# let's skip this for now

