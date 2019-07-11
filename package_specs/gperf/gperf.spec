Name:       gperf
Version:    3.1
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
%configure --docdir=/usr/share/doc/gperf-3.1
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/gperf
/usr/share/doc/gperf-3.1/gperf.html
/usr/share/info/gperf.info.gz
/usr/share/man/man1/gperf.1.gz

%changelog
# let's skip this for now
