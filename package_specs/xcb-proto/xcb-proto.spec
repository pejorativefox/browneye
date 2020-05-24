Name:       xcb-proto
Version:    1.13
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
/usr/lib64/pkgconfig/xcb-proto.pc
/usr/share/xcb/
/usr/lib/python3.7/site-packages/

%changelog
# let's skip this for now
