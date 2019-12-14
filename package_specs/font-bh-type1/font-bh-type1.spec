Name:       font-bh-type1
Version:    1.0.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



%description
TODO

%prep
%setup

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
rm -rf %{buildroot}/usr/share/fonts/X11/Type1/fonts.dir
rm -rf %{buildroot}/usr/share/fonts/X11/Type1/fonts.scale

%files
/usr/share/fonts/X11/Type1/l047013t.afm
/usr/share/fonts/X11/Type1/l047013t.pfa
/usr/share/fonts/X11/Type1/l047016t.afm
/usr/share/fonts/X11/Type1/l047016t.pfa
/usr/share/fonts/X11/Type1/l047033t.afm
/usr/share/fonts/X11/Type1/l047033t.pfa
/usr/share/fonts/X11/Type1/l047036t.afm
/usr/share/fonts/X11/Type1/l047036t.pfa
/usr/share/fonts/X11/Type1/l048013t.afm
/usr/share/fonts/X11/Type1/l048013t.pfa
/usr/share/fonts/X11/Type1/l048016t.afm
/usr/share/fonts/X11/Type1/l048016t.pfa
/usr/share/fonts/X11/Type1/l048033t.afm
/usr/share/fonts/X11/Type1/l048033t.pfa
/usr/share/fonts/X11/Type1/l048036t.afm
/usr/share/fonts/X11/Type1/l048036t.pfa
/usr/share/fonts/X11/Type1/l049013t.afm
/usr/share/fonts/X11/Type1/l049013t.pfa
/usr/share/fonts/X11/Type1/l049016t.afm
/usr/share/fonts/X11/Type1/l049016t.pfa
/usr/share/fonts/X11/Type1/l049033t.afm
/usr/share/fonts/X11/Type1/l049033t.pfa
/usr/share/fonts/X11/Type1/l049036t.afm
/usr/share/fonts/X11/Type1/l049036t.pfa


%changelog
# let's skip this for now

