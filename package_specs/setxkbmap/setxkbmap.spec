Name:       setxkbmap
Version:    1.3.1
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
/usr/bin/setxkbmap
/usr/share/man/man1/setxkbmap.1.gz

%changelog
# let's skip this for now

