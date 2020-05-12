Name:       stunnel 
Version:    5.56
Release:    2
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

# Kludge for simple finit configs
mkdir -pv %{buildroot}/etc/finit.d/available
cat > %{buildroot}/etc/finit.d/available/stunnel.conf << "EOF"
# Stunnel4
# For proper logging it needs to be specified in your /etc/stunnel/stunnel.conf!
task [2345] /bin/stunnel
EOF

%files
/usr/bin/stunnel
/usr/bin/stunnel3
/usr/etc/stunnel/stunnel.conf-sample
/usr/lib64/stunnel/libstunnel.la
/usr/lib64/stunnel/libstunnel.so
/usr/share/doc/stunnel/*
/usr/share/man/*
/etc/finit.d/available/stunnel.conf

%changelog
* Thu May 14 2020 Chris Statzer <chris.statzer@qq.com> 5.56-2
- Added finit control script

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 5.56
- Initial package.
