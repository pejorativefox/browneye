Name:       xterm
Version:    344
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tgz



%description
TODO

%prep
%setup -a 0

%build
sed -i '/v0/{n;s/new:/new:kb=^?:/}' termcap &&
printf '\tkbs=\\177,\n' >> terminfo &&
export TERMINFO=/usr/share/terminfo
%configure --with-xinitdir=/etc/X11/app-defaults
%make_build
unset TERMINFO

%install    
rm -rf %{buildroot}
%make_install
make install-ti DESTDIR=%{buildroot}
rm -vf %{buildroot}%{_infodir}/dir*
rm -vrf %{buildroot}/usr/share/terminfo

%files
/usr/bin/koi8rxterm
/usr/bin/resize
/usr/bin/uxterm
/usr/bin/xterm
/usr/lib/X11/app-defaults/KOI8RXTerm
/usr/lib/X11/app-defaults/KOI8RXTerm-color
/usr/lib/X11/app-defaults/UXTerm
/usr/lib/X11/app-defaults/UXTerm-color
/usr/lib/X11/app-defaults/XTerm
/usr/lib/X11/app-defaults/XTerm-color
/usr/share/man/man1/koi8rxterm.1.gz
/usr/share/man/man1/resize.1.gz
/usr/share/man/man1/uxterm.1.gz
/usr/share/man/man1/xterm.1.gz
/usr/share/pixmaps/filled-xterm_32x32.xpm
/usr/share/pixmaps/filled-xterm_48x48.xpm
/usr/share/pixmaps/mini.xterm_32x32.xpm
/usr/share/pixmaps/mini.xterm_48x48.xpm
/usr/share/pixmaps/xterm-color_32x32.xpm
/usr/share/pixmaps/xterm-color_48x48.xpm
/usr/share/pixmaps/xterm_32x32.xpm
/usr/share/pixmaps/xterm_48x48.xpm

%changelog
# let's skip this for now

