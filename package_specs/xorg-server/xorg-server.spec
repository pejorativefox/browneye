Name:       xorg-server
Version:    21.1.8
Release:    1
Summary:    Xorg server
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

BuildRequires: libx11, mesa, pixman, libdrm, libxfont2, libxkbfile, xtrans
BuildRequires: libepoxy, libxcvt

%description
Xorg server

%prep
%setup -q

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
rm %{buildroot}/var/lib/xkb/README.compiled

%files
/etc/sysconfig/createfiles
/usr/bin/X
/usr/bin/Xnest
/usr/bin/Xorg
/usr/bin/Xvfb
/usr/bin/gtf
/usr/include/xorg/
/usr/lib64/pkgconfig/xorg-server.pc
/usr/lib64/xorg/modules/
/usr/lib64/xorg/protocol.txt
/usr/libexec/Xorg
/usr/libexec/Xorg.wrap
/usr/share/X11/xorg.conf.d/10-quirks.conf
/usr/share/aclocal/xorg-server.m4
/usr/share/man/

%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 21.1.8-1
- Version bump

