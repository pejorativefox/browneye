Name:       gtk2+
Version:    2.24.32
Release:    2
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    gtk+-%{version}.tar.xz

Provides: pkgconfig(gtk+-2.0)

%description
TODO

%prep
%setup -q -n gtk+-%{version}

%build
sed -e 's#l \(gtk-.*\).sgml#& -o \1#' \
    -i docs/{faq,tutorial}/Makefile.in
%configure
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mv %{buildroot}/usr/bin/gtk-update-icon-cache %{buildroot}/usr/bin/gtk2-update-icon-cache
mkdir -pv %{buildroot}/etc/gtk-2.0/

cat > %{buildroot}/etc/gtk-2.0/gtkrc << "EOF"
include "/usr/share/themes/Clearlooks/gtk-2.0/gtkrc"
gtk-icon-theme-name = "elementary"
EOF

%post
gtk-query-immodules-2.0 --update-cache

%files -f ../../SOURCES/gtk2.filelist

%changelog
# let's skip this for now

