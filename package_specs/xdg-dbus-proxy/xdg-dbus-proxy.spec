Name:       xdg-dbus-proxy
Version:    0.1.2
Release:    1
Summary:    filtering proxy for D-Bus connections
License:    LGPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
filtering proxy for D-Bus connections

%prep
%setup
sed -i 's/XSLTPROC = xsltproc/XSLTPROC = true/g' Makefile.in
touch xdg-dbus-proxy.1

%build
%configure  --disable-doxygen-docs    \
            --disable-xml-docs        \
            --disable-man-pages
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/xdg-dbus-proxy
/usr/share/man/man1/xdg-dbus-proxy.1.gz

%changelog
* Thu Sep 10 2020 Chris Statzer <chris.statzer@qq.com> 0.1.2
- Initial RPM

