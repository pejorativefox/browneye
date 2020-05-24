Name:       xrandr
Version:    1.5.0
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz



%description
TODO

%prep
%setup -n xorg-xrandr-xrandr-%{version}

%build
./autogen.sh
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/xkeystone
/usr/bin/xrandr
/usr/share/man/man1/xrandr.1.gz

%changelog
# let's skip this for now

