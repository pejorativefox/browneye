Name:       xinit
Version:    1.4.0
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
sed -e '/$serverargs $vtarg/ s/serverargs/: #&/' \
    -i startx.cpp
%configure --with-xinitdir=/etc/X11/app-defaults
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*


%files
/etc/X11/app-defaults/xinitrc
/usr/bin/startx
/usr/bin/xinit
/usr/share/man/man1/startx.1.gz
/usr/share/man/man1/xinit.1.gz

%changelog
# let's skip this for now

