Name:       iana-etc
Version:    20230810
Release:    1
Summary:    Authoritative list of internet protocals
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Protocol parameter registries represent the authoritative record of many of the codes and numbers contained in a variety of Internet protocols.

%prep
%setup -q -a0

%build

%install    
rm -rf %{buildroot}
mkdir -pv %{buildroot}/etc
cp services protocols %{buildroot}/etc

%files
/etc/protocols
/etc/services

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 20230810
- Version bump
