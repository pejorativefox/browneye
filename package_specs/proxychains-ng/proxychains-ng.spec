Name:       proxychains-ng
Version:    4.16
Release:    1
Summary:    CLI utility to pipe tcp traffic througha proxy.
License:    GPL
Source0:    %{name}-%{version}.tar.xz
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
/usr/bin/proxychains4-daemon
/usr/lib64/libproxychains4.so

%changelog
* Mon Jun 10 2023 Chris Statzer <chris.statzer@gmail.com> 4.16
- Version Bump

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 4.14
- Initial rpm package
