Name:       xorgproto
Version:    2023.2
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
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
/usr/include/GL/
/usr/include/X11/
/usr/share/doc/
/usr/share/pkgconfig/

%changelog
# let's skip this for now
