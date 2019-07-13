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
/usr/share/terminfo/a/ansi+enq
/usr/share/terminfo/a/ansi+rep
/usr/share/terminfo/e/ecma+strikeout
/usr/share/terminfo/v/vs100
/usr/share/terminfo/x/xterm
/usr/share/terminfo/x/xterm+256color
/usr/share/terminfo/x/xterm+alt+title
/usr/share/terminfo/x/xterm+alt1049
/usr/share/terminfo/x/xterm+app
/usr/share/terminfo/x/xterm+app+pc
/usr/share/terminfo/x/xterm+decedit
/usr/share/terminfo/x/xterm+direct
/usr/share/terminfo/x/xterm+edit
/usr/share/terminfo/x/xterm+kbs
/usr/share/terminfo/x/xterm+noalt
/usr/share/terminfo/x/xterm+noapp
/usr/share/terminfo/x/xterm+noapp+pc
/usr/share/terminfo/x/xterm+pc+edit
/usr/share/terminfo/x/xterm+pcc0
/usr/share/terminfo/x/xterm+pcc1
/usr/share/terminfo/x/xterm+pcc2
/usr/share/terminfo/x/xterm+pcc3
/usr/share/terminfo/x/xterm+pce0
/usr/share/terminfo/x/xterm+pce1
/usr/share/terminfo/x/xterm+pce2
/usr/share/terminfo/x/xterm+pce3
/usr/share/terminfo/x/xterm+pcf0
/usr/share/terminfo/x/xterm+pcf1
/usr/share/terminfo/x/xterm+pcf2
/usr/share/terminfo/x/xterm+pcf3
/usr/share/terminfo/x/xterm+pcfN
/usr/share/terminfo/x/xterm+pcfkeys
/usr/share/terminfo/x/xterm+pcfn
/usr/share/terminfo/x/xterm+sm+1006
/usr/share/terminfo/x/xterm+titlestack
/usr/share/terminfo/x/xterm+tmux
/usr/share/terminfo/x/xterm+vt+edit
/usr/share/terminfo/x/xterm+x11mouse
/usr/share/terminfo/x/xterm-16color
/usr/share/terminfo/x/xterm-24
/usr/share/terminfo/x/xterm-256color
/usr/share/terminfo/x/xterm-65
/usr/share/terminfo/x/xterm-88color
/usr/share/terminfo/x/xterm-8bit
/usr/share/terminfo/x/xterm-basic
/usr/share/terminfo/x/xterm-bold
/usr/share/terminfo/x/xterm-boldso
/usr/share/terminfo/x/xterm-color
/usr/share/terminfo/x/xterm-direct
/usr/share/terminfo/x/xterm-hp
/usr/share/terminfo/x/xterm-ic
/usr/share/terminfo/x/xterm-mono
/usr/share/terminfo/x/xterm-new
/usr/share/terminfo/x/xterm-noapp
/usr/share/terminfo/x/xterm-nrc
/usr/share/terminfo/x/xterm-old
/usr/share/terminfo/x/xterm-r5
/usr/share/terminfo/x/xterm-r6
/usr/share/terminfo/x/xterm-rep
/usr/share/terminfo/x/xterm-sco
/usr/share/terminfo/x/xterm-sun
/usr/share/terminfo/x/xterm-vi
/usr/share/terminfo/x/xterm-vt220
/usr/share/terminfo/x/xterm-vt52
/usr/share/terminfo/x/xterm-xf86-v44
/usr/share/terminfo/x/xterm-xfree86
/usr/share/terminfo/x/xterm-xmc
/usr/share/terminfo/x/xterms


%changelog
# let's skip this for now

