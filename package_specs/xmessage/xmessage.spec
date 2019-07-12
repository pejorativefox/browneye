Name:       xmessage
Version:    1.0.5
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
/etc/X11/app-defaults/Xmessage
/etc/X11/app-defaults/Xmessage-color
/usr/bin/xmessage
/usr/share/man/man1/xmessage.1.gz

%changelog
# let's skip this for now

