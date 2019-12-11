Name:       proxychains-ng
Version:    4.14
Release:    1
Summary:    CLI utility to pipe tcp traffic througha proxy.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
proxychains ng (new generation) - a preloader which hooks calls to sockets in 
dynamically linked programs and redirects it through one or more socks/http 
proxies. 

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
mkdir %{buildroot}/etc
cp src/proxychains.conf %{buildroot}/etc/

%files
/etc/proxychains.conf
/usr/bin/proxychains4
/usr/lib64/libproxychains4.so

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14
- Initial rpm package
