Name:       dbus-glib
Version:    0.110
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz


%description
TODO

%prep
%setup -a 0

%build
%configure --disable-static
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/dbus-binding-tool
/usr/etc/bash_completion.d/dbus-bash-completion.sh
/usr/include/dbus-1.0/dbus/dbus-glib-bindings.h
/usr/include/dbus-1.0/dbus/dbus-glib-lowlevel.h
/usr/include/dbus-1.0/dbus/dbus-glib.h
/usr/include/dbus-1.0/dbus/dbus-gtype-specialized.h
/usr/include/dbus-1.0/dbus/dbus-gvalue-parse-variant.h
/usr/lib64/libdbus-glib-1.so
/usr/lib64/libdbus-glib-1.so.2
/usr/lib64/libdbus-glib-1.so.2.3.4
/usr/lib64/pkgconfig/dbus-glib-1.pc
/usr/libexec/dbus-bash-completion-helper
/usr/share/gtk-doc/html/dbus-glib/
/usr/share/man/man1/dbus-binding-tool.1.gz

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 0.11.0-1
- Version bump

