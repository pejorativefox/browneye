Name:       htop
Version:    3.2.2
Release:    1
Summary:    interactive process viewer 
License:    GPL3
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
interactive process viewer 

%prep
%setup -q

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/htop
/usr/share/applications/htop.desktop
/usr/share/man/man1/htop.1.gz
/usr/share/pixmaps/htop.png
/usr/share/icons/hicolor/scalable/apps/htop.svg

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 3.2.2-1
- Version bump
