Name:       iana-etc
Version:    2.30
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*


%files
/etc/protocols
/etc/services

%changelog
# let's skip this for now
