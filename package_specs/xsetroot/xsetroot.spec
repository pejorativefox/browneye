Name:       xsetroot
Version:    1.1.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: xbitmaps

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
/usr/bin/xsetroot
/usr/share/man/man1/xsetroot.1.gz

%changelog
# let's skip this for now

