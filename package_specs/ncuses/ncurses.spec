Name:       ncurses
Version:    6.1
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
sed -i '/LIBTOOL_INSTALL/d' c++/Makefile.in
%configure --mandir=/usr/share/man \
           --with-shared \
           --without-debug \
           --without-normal \
           --enable-pc-files \
           --enable-widec
%make_build

%install
rm -rf %{buildroot}
%make_install
#mkdir -pv %{buildroot}/lib
#mv -v %{buildroot}/usr/lib64/libncursesw.so.6* %{buildroot}/lib
mv -v %{buildroot}/share/pkgconfig %{buildroot}/usr/share

%post
for lib in ncurses form panel menu ; do
    rm -vf                    /usr/lib/lib${lib}.so
    echo "INPUT(-l${lib}w)" > /usr/lib/lib${lib}.so
    ln -sfv ${lib}w.pc        /usr/lib/pkgconfig/${lib}.pc
done
rm -vf                     /usr/lib/libcursesw.so
echo "INPUT(-lncursesw)" > /usr/lib/libcursesw.so
ln -sfv libncurses.so      /usr/lib/libcurses.so


%files
/usr/bin/captoinfo
/usr/bin/clear
/usr/bin/infocmp
/usr/bin/infotocap
/usr/bin/ncursesw6-config
/usr/bin/reset
/usr/bin/tabs
/usr/bin/tic
/usr/bin/toe
/usr/bin/tput
/usr/bin/tset
/usr/include/curses.h
/usr/include/cursesapp.h
/usr/include/cursesf.h
/usr/include/cursesm.h
/usr/include/cursesp.h
/usr/include/cursesw.h
/usr/include/cursslk.h
/usr/include/eti.h
/usr/include/etip.h
/usr/include/form.h
/usr/include/menu.h
/usr/include/nc_tparm.h
/usr/include/ncurses.h
/usr/include/ncurses_dll.h
/usr/include/panel.h
/usr/include/term.h
/usr/include/term_entry.h
/usr/include/termcap.h
/usr/include/tic.h
/usr/include/unctrl.h
/usr/lib64/libformw.so
/usr/lib64/libformw.so.6
/usr/lib64/libformw.so.6.1
/usr/lib64/libmenuw.so
/usr/lib64/libmenuw.so.6
/usr/lib64/libmenuw.so.6.1
/usr/lib64/libncurses++w.a
/usr/lib64/libncursesw.so
/usr/lib64/libncursesw.so.6
/usr/lib64/libncursesw.so.6.1
/usr/lib64/libpanelw.so
/usr/lib64/libpanelw.so.6
/usr/lib64/libpanelw.so.6.1
/usr/share/man/*
/usr/share/pkgconfig/formw.pc
/usr/share/pkgconfig/menuw.pc
/usr/share/pkgconfig/ncurses++w.pc
/usr/share/pkgconfig/ncursesw.pc
/usr/share/pkgconfig/panelw.pc
/usr/share/tabset/std
/usr/share/tabset/stdcrt
/usr/share/tabset/vt100
/usr/share/tabset/vt300
/usr/share/terminfo/*

%changelog
# let's skip this for now
