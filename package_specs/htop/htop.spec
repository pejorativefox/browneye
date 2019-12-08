Name:       htop
Version:    2.2.0
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%configure --prefix=/usr --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/htop
/usr/share/applications/htop.desktop
/usr/share/man/man1/htop.1.gz
/usr/share/pixmaps/htop.png


%changelog
# let's skip this for now
