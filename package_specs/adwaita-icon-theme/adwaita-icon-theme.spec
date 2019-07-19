Name:       adwaita-icon-theme
Version:    3.30.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


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
/usr/share/icons/*
/usr/share/pkgconfig/adwaita-icon-theme.pc

%changelog
# let's skip this for now

