Name:       vte
Version:    0.72.2
Release:    1
Summary:    Virtual Terminal Emulator library.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

BuildRequires: icu4c

%description
Virtual Terminal Emulator library.

%prep
%setup

%build
mkdir build
pushd build
meson   --prefix=/usr     \
	--sysconfdir=/etc \
        -Dfribidi=false   \
        -Dvapi=false      \
        -D_systemd=false
ninja
popd

%install
rm -rf %{buildroot}
pushd build
DESTDIR=%{buildroot} ninja install
popd

%files
/etc/profile.d/vte.csh
/etc/profile.d/vte.sh
/usr/bin/vte-2.91
/usr/include/vte-2.91/vte/vte.h
/usr/include/vte-2.91/vte/vtedeprecated.h
/usr/include/vte-2.91/vte/vteenums.h
/usr/include/vte-2.91/vte/vteglobals.h
/usr/include/vte-2.91/vte/vtemacros.h
/usr/include/vte-2.91/vte/vtepty.h
/usr/include/vte-2.91/vte/vteregex.h
/usr/include/vte-2.91/vte/vteterminal.h
/usr/include/vte-2.91/vte/vtetypebuiltins-gtk3.h
/usr/include/vte-2.91/vte/vtetypebuiltins.h
/usr/include/vte-2.91/vte/vteversion.h
/usr/lib64/girepository-1.0/Vte-2.91.typelib
/usr/lib64/libvte-2.91.so
/usr/lib64/libvte-2.91.so.0
/usr/lib64/libvte-2.91.so.0.7200.2
/usr/lib64/pkgconfig/vte-2.91.pc
/usr/libexec/vte-urlencode-cwd
/usr/share/gir-1.0/Vte-2.91.gir
/usr/share/glade/catalogs/vte-2.91.xml
/usr/share/glade/pixmaps/hicolor/16x16/actions/widget-vte-terminal.png
/usr/share/glade/pixmaps/hicolor/22x22/actions/widget-vte-terminal.png
/usr/share/locale/

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 0.59.0
- Added this sample to help with adding new packages.

