Name:       util-macros
Version:    1.20.0
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
/usr/share/aclocal/xorg-macros.m4
/usr/share/pkgconfig/xorg-macros.pc
/usr/share/util-macros/INSTALL

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.20.0-1
- Version bump
