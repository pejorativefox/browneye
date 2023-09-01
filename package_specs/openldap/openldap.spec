Name:       openldap
Version:    2.6.6
Release:    1
Summary:    Open source implementation of the LDAP Protocol
License:    OpenLDAP
Source0:    %{name}-%{version}.tgz
Prefix:     /usr

%description
The OpenLDAP package provides an open source implementation of the Lightweight Directory Access Protocol. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/etc/
/usr/sbin/
/usr/share/
/usr/lib64/
/usr/bin/
/usr/include/
/usr/libexec/slapd

%changelog
* Tue Jun 13 2023 Chris Statzer <chris.statzer@gmail.com> 3.30.1
- Initial RPM

