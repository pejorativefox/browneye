Name:       mpc
Version:    1.3.1
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
%configure --disable-static --docdir=/usr/share/doc/mpc-%{version}
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/mpc.h
/usr/lib64/
/usr/share/info/mpc.info.gz

%changelog
* Wed Aug 30 2023 Chris Statzer <chris.statzer@gmail.com> 1.3.1
- Version bump
