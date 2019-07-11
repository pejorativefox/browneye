Name:       less
Version:    530
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

%configure --sysconfdir=/etc
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey
/usr/share/man/man1/less.1.gz
/usr/share/man/man1/lessecho.1.gz
/usr/share/man/man1/lesskey.1.gz

%changelog
# let's skip this for now
