Name:       gtk-xfce-engine
Version:    3.2.0
Release:    1
Summary:    Xfce Gtk engine
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
Xfce Gtk engine

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/lib64/gtk-2.0/2.10.0/engines/libxfce.la
/usr/lib64/gtk-2.0/2.10.0/engines/libxfce.so
/usr/share/themes/Xfce-4.0/gtk-2.0/gtkrc
/usr/share/themes/Xfce-4.2/gtk-2.0/gtkrc
/usr/share/themes/Xfce-4.4/gtk-2.0/gtkrc
/usr/share/themes/Xfce-4.6/gtk-2.0/gtkrc
/usr/share/themes/Xfce-b5/gtk-2.0/gtkrc
/usr/share/themes/Xfce-basic/gtk-2.0/gtkrc
/usr/share/themes/Xfce-cadmium/gtk-2.0/gtkrc
/usr/share/themes/Xfce-curve/gtk-2.0/gtkrc
/usr/share/themes/Xfce-dawn/gtk-2.0/gtkrc
/usr/share/themes/Xfce-dusk/gtk-2.0/gtkrc
/usr/share/themes/Xfce-flat/gtk-2.0/gtkrc
/usr/share/themes/Xfce-kde2/gtk-2.0/gtkrc
/usr/share/themes/Xfce-kolors/gtk-2.0/gtkrc
/usr/share/themes/Xfce-light/gtk-2.0/gtkrc
/usr/share/themes/Xfce-orange/gtk-2.0/gtkrc
/usr/share/themes/Xfce-redmondxp/gtk-2.0/gtkrc
/usr/share/themes/Xfce-saltlake/gtk-2.0/gtkrc
/usr/share/themes/Xfce-smooth/gtk-2.0/gtkrc
/usr/share/themes/Xfce-stellar/gtk-2.0/gtkrc
/usr/share/themes/Xfce-winter/gtk-2.0/gtkrc
/usr/share/themes/Xfce/gtk-2.0/gtkrc

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 3.2.0
- Initial RPM

