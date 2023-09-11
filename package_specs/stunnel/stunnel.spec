Name:       stunnel 
Version:    5.69
Release:    1
Summary:    TLS proxy daemon.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Source1:    stunnel-service.conf
Source2:    stunnel.service
Prefix:     /usr

%description
Stunnel is a proxy designed to add TLS encryption functionality to existing clients and servers without any changes in the programs' code. 

%prep
%setup -n stunnel-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

mkdir -pv %{buildroot}/etc/finit.d/available
mkdir -pv %{buildroot}/etc/service.d

cp %{SOURCE1} %{buildroot}/etc/finit.d/available/stunnel.conf
cp %{SOURCE2} %{buildroot}/etc/service.d/


%files
/usr/bin/stunnel
/usr/bin/stunnel3
/usr/etc/stunnel/stunnel.conf-sample
/usr/lib64/stunnel/libstunnel.so
/usr/share/doc/stunnel/
/usr/share/man/
/etc/finit.d/available/stunnel.conf
/etc/service.d/stunnel.service

%changelog
* Mon Jun 12 2023 Chris Statzer <chris.statzer@gmail.com> 5.69
- Version bump

* Thu May 14 2020 Chris Statzer <chris.statzer@qq.com> 5.56-2
- Added finit control script

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 5.56
- Initial package.
