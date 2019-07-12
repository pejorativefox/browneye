Name:       xkbutils
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
/usr/bin/xkbbell
/usr/bin/xkbvleds
/usr/bin/xkbwatch
/usr/share/man/man1/xkbbell.1.gz
/usr/share/man/man1/xkbvleds.1.gz
/usr/share/man/man1/xkbwatch.1.gz

%changelog
# let's skip this for now

