Name:       gtk+
Version:    3.24.5
Release:    2
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz


%description
TODO

%prep
%setup

%build
%configure  --sysconfdir=/etc         \
            --enable-broadway-backend \
            --enable-x11-backend
%make_build

%install    
rm -rf %{buildroot}
%make_install
glib-compile-schemas %{buildroot}/usr/share/glib-2.0/schemas
rm -vf %{buildroot}%{_infodir}/dir*

%post
gtk-query-immodules-3.0 --update-cache

%files
/etc/gtk-3.0/im-multipress.conf
/usr/bin/broadwayd
/usr/bin/gtk-builder-tool
/usr/bin/gtk-encode-symbolic-svg
/usr/bin/gtk-launch
/usr/bin/gtk-query-immodules-3.0
/usr/bin/gtk-query-settings
/usr/bin/gtk-update-icon-cache
/usr/bin/gtk3-demo
/usr/bin/gtk3-demo-application
/usr/bin/gtk3-icon-browser
/usr/bin/gtk3-widget-factory
/usr/include/
/usr/lib64/
/usr/share/

%changelog
# let's skip this for now

