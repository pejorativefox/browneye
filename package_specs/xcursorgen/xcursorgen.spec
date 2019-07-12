Name:       xcursorgen
Version:    1.0.7
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
/usr/bin/xcursorgen
/usr/share/man/man1/xcursorgen.1.gz

%changelog
# let's skip this for now

