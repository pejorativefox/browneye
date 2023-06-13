Name:       openvpn
Version:    2.4.9
Release:    1
Summary:    Open source VPN client
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Open source VPN client

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/include/openvpn-msg.h
/usr/include/openvpn-plugin.h
/usr/lib64/openvpn/plugins/openvpn-plugin-auth-pam.la
/usr/lib64/openvpn/plugins/openvpn-plugin-auth-pam.so
/usr/lib64/openvpn/plugins/openvpn-plugin-down-root.la
/usr/lib64/openvpn/plugins/openvpn-plugin-down-root.so
/usr/sbin/openvpn
/usr/share/doc/openvpn/COPYING
/usr/share/doc/openvpn/COPYRIGHT.GPL
/usr/share/doc/openvpn/Changes.rst
/usr/share/doc/openvpn/README
/usr/share/doc/openvpn/README.IPv6
/usr/share/doc/openvpn/README.auth-pam
/usr/share/doc/openvpn/README.down-root
/usr/share/doc/openvpn/README.mbedtls
/usr/share/doc/openvpn/management-notes.txt
/usr/share/man/man8/openvpn.8.gz

%changelog
* Wed Aug 19 2020 Chris Statzer <chris.statzer@qq.com> 2.4.9
- Initial RPM

