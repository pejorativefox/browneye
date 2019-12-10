Name:       stunnel 
Version:    5.56
Release:    1
Summary:    TLS proxy daemon.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Stunnel is a proxy designed to add TLS encryption functionality to existing clients and servers without any changes in the programs' code. 

%prep
%setup -n stunnel-stunnel-%{version}

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
   /usr/bin/stunnel
   /usr/bin/stunnel3
   /usr/etc/stunnel/stunnel.conf-sample
   /usr/lib64/stunnel/libstunnel.la
   /usr/lib64/stunnel/libstunnel.so
   /usr/share/doc/stunnel/*
   /usr/share/man/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 5.56
- Initial package.
