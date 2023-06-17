Name:       xorg-server
Version:    1.20.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: libX11, mesa, pixman, libdrm, libXfont2, libxkbfile, xtrans
BuildRequires: libepoxy
%description
TODO

%prep
%setup -a 0

%build
%configure --enable-glamor          \
           --enable-install-setuid  \
           --enable-suid-wrapper    \
           --disable-systemd-logind \
           --with-xkb-output=/var/lib/xkb
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/etc/X11/xorg.conf.d &&
mkdir -pv %{buildroot}/etc/sysconfig
cat >> %{buildroot}/etc/sysconfig/createfiles << "EOF"
/tmp/.ICE-unix dir 1777 root root
/tmp/.X11-unix dir 1777 root root
EOF

%files
/etc/sysconfig/createfiles
/usr/bin/X
/usr/bin/Xnest
/usr/bin/Xorg
/usr/bin/Xvfb
/usr/bin/cvt
/usr/bin/gtf
/usr/include/xorg/
/usr/lib64/pkgconfig/xorg-server.pc
/usr/lib64/xorg/modules/
/usr/lib64/xorg/protocol.txt
/usr/share/X11/xorg.conf.d/10-quirks.conf
/usr/share/aclocal/xorg-server.m4
/usr/share/man/man1/Xnest.1.gz
/usr/share/man/man1/Xorg.1.gz
/usr/share/man/man1/Xserver.1.gz
/usr/share/man/man1/Xvfb.1.gz
/usr/share/man/man1/cvt.1.gz
/usr/share/man/man1/gtf.1.gz
/usr/share/man/man4/exa.4.gz
/usr/share/man/man4/fbdevhw.4.gz
/usr/share/man/man4/modesetting.4.gz
/usr/share/man/man5/xorg.conf.5.gz
/usr/share/man/man5/xorg.conf.d.5.gz
/var/lib/xkb/README.compiled
/usr/libexec/Xorg
/usr/libexec/Xorg.wrap
/usr/share/man/man1/Xorg.wrap.1.gz
/usr/share/man/man5/Xwrapper.config.5.gz

%changelog
# let's skip this for now

