Name:       util-macros
Version:    1.19.2
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build 
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/share/aclocal/xorg-macros.m4
/usr/share/pkgconfig/xorg-macros.pc
/usr/share/util-macros/INSTALL

%changelog
# let's skip this for now
