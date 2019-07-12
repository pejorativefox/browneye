Name:       font-alias
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
/usr/share/fonts/X11/100dpi/fonts.alias
/usr/share/fonts/X11/75dpi/fonts.alias
/usr/share/fonts/X11/cyrillic/fonts.alias
/usr/share/fonts/X11/misc/fonts.alias

%changelog
# let's skip this for now

