Name:       polkit
Version:    0.115
Release:    2
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz
Patch:      polkit-0.115-security_patch-3.patch

%description
TODO

Requires: shadow >= 4.6

%post
groupadd -fg 27 polkitd &&
useradd -c "PolicyKit Daemon Owner" -d /etc/polkit-1 -u 27 \
        -g polkitd -s /bin/false polkitd

%prep
%setup -a 0
%patch -p1

%build
%configure  --sysconfdir=/etc                \
            --localstatedir=/var             \
            --disable-static                 \
            --enable-libsystemd-login=no     \
            --enable-libelogind=no           \
            --with-authfw=shadow --disable-man-pages
%make_build


%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
/etc/polkit-1/rules.d/50-default.rules
/usr/bin/pk-example-frobnicate
/usr/bin/pkaction
/usr/bin/pkcheck
/usr/bin/pkexec
/usr/bin/pkttyagent
/usr/include/polkit-1/*
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/lib/polkit-1/polkitd
/usr/lib64/girepository-1.0/Polkit-1.0.typelib
/usr/lib64/girepository-1.0/PolkitAgent-1.0.typelib
/usr/lib64/libpolkit-agent-1.la
/usr/lib64/libpolkit-agent-1.so
/usr/lib64/libpolkit-agent-1.so.0
/usr/lib64/libpolkit-agent-1.so.0.0.0
/usr/lib64/libpolkit-gobject-1.la
/usr/lib64/libpolkit-gobject-1.so
/usr/lib64/libpolkit-gobject-1.so.0
/usr/lib64/libpolkit-gobject-1.so.0.0.0
/usr/lib64/pkgconfig/polkit-agent-1.pc
/usr/lib64/pkgconfig/polkit-gobject-1.pc
/usr/share/dbus-1/system-services/org.freedesktop.PolicyKit1.service
/usr/share/gettext/its/polkit.its
/usr/share/gettext/its/polkit.loc
/usr/share/gir-1.0/Polkit-1.0.gir
/usr/share/gir-1.0/PolkitAgent-1.0.gir
/usr/share/locale/*
/usr/share/polkit-1/actions/org.freedesktop.policykit.examples.pkexec.policy
/usr/share/polkit-1/actions/org.freedesktop.policykit.policy

%changelog
* Sun May 10 2020 Chris Statzer <chris.statzer@qq.com> 0.115
- Updated post install to create proper polkitd user

* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.115
- Initial RPM

