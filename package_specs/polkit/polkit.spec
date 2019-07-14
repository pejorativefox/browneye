Name:       polkit
Version:    0.115
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz
Patch:      polkit-0.115-security_patch-3.patch

%description
TODO

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
/usr/include/polkit-1/polkit/polkit.h
/usr/include/polkit-1/polkit/polkitactiondescription.h
/usr/include/polkit-1/polkit/polkitauthority.h
/usr/include/polkit-1/polkit/polkitauthorityfeatures.h
/usr/include/polkit-1/polkit/polkitauthorizationresult.h
/usr/include/polkit-1/polkit/polkitcheckauthorizationflags.h
/usr/include/polkit-1/polkit/polkitdetails.h
/usr/include/polkit-1/polkit/polkitenumtypes.h
/usr/include/polkit-1/polkit/polkiterror.h
/usr/include/polkit-1/polkit/polkitidentity.h
/usr/include/polkit-1/polkit/polkitimplicitauthorization.h
/usr/include/polkit-1/polkit/polkitpermission.h
/usr/include/polkit-1/polkit/polkitprivate.h
/usr/include/polkit-1/polkit/polkitsubject.h
/usr/include/polkit-1/polkit/polkitsystembusname.h
/usr/include/polkit-1/polkit/polkittemporaryauthorization.h
/usr/include/polkit-1/polkit/polkittypes.h
/usr/include/polkit-1/polkit/polkitunixgroup.h
/usr/include/polkit-1/polkit/polkitunixnetgroup.h
/usr/include/polkit-1/polkit/polkitunixprocess.h
/usr/include/polkit-1/polkit/polkitunixsession.h
/usr/include/polkit-1/polkit/polkitunixuser.h
/usr/include/polkit-1/polkitagent/polkitagent.h
/usr/include/polkit-1/polkitagent/polkitagentenumtypes.h
/usr/include/polkit-1/polkitagent/polkitagentlistener.h
/usr/include/polkit-1/polkitagent/polkitagentsession.h
/usr/include/polkit-1/polkitagent/polkitagenttextlistener.h
/usr/include/polkit-1/polkitagent/polkitagenttypes.h
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
/usr/share/locale/cs/LC_MESSAGES/polkit-1.mo
/usr/share/locale/da/LC_MESSAGES/polkit-1.mo
/usr/share/locale/de/LC_MESSAGES/polkit-1.mo
/usr/share/locale/hr/LC_MESSAGES/polkit-1.mo
/usr/share/locale/hu/LC_MESSAGES/polkit-1.mo
/usr/share/locale/id/LC_MESSAGES/polkit-1.mo
/usr/share/locale/pl/LC_MESSAGES/polkit-1.mo
/usr/share/locale/pt_BR/LC_MESSAGES/polkit-1.mo
/usr/share/locale/sk/LC_MESSAGES/polkit-1.mo
/usr/share/locale/sv/LC_MESSAGES/polkit-1.mo
/usr/share/locale/tr/LC_MESSAGES/polkit-1.mo
/usr/share/locale/uk/LC_MESSAGES/polkit-1.mo
/usr/share/locale/zh_CN/LC_MESSAGES/polkit-1.mo
/usr/share/locale/zh_TW/LC_MESSAGES/polkit-1.mo
/usr/share/polkit-1/actions/org.freedesktop.policykit.examples.pkexec.policy
/usr/share/polkit-1/actions/org.freedesktop.policykit.policy


%changelog
# let's skip this for now

