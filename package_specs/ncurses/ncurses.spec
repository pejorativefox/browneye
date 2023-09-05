Name:       ncurses
Version:    6.4
Release:    1
Summary:    Text based user interface library
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 (SVr4), and more. 

%prep
%setup

%build
#sed -i '/LIBTOOL_INSTALL/d' c++/Makefile.in
%configure  --prefix=/usr           \
            --mandir=/usr/share/man \
            --with-shared           \
            --without-debug         \
            --without-normal        \
            --with-cxx-shared       \
            --enable-pc-files       \
            --enable-widec          \
            --with-pkg-config-libdir=/usr/lib/pkgconfig
%make_build

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib64/pkgconfig/
for lib in ncurses form panel menu ; do
    rm -vf                    %{buildroot}/usr/lib64/lib${lib}.so
    echo "INPUT(-l${lib}w)" > %{buildroot}/usr/lib64/lib${lib}.so
    ln -sfv ${lib}w.pc        %{buildroot}/usr/lib64/pkgconfig/${lib}.pc
done

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
/usr/lib64/libformw.so.6.4
/usr/lib64/libmenuw.so
/usr/lib64/libmenuw.so.6
/usr/lib64/libmenuw.so.6.4
/usr/lib64/libncursesw.so
/usr/lib64/libncursesw.so.6
/usr/lib64/libncursesw.so.6.4
/usr/lib64/libpanelw.so
/usr/lib64/libpanelw.so.6
/usr/lib64/libpanelw.so.6.4
/usr/lib64/libform.so
/usr/lib64/libmenu.so
/usr/lib64/libncurses.so
/usr/lib64/libpanel.so
/usr/lib64/libncurses++w.so
/usr/lib64/libncurses++w.so.6
/usr/lib64/libncurses++w.so.6.4
/usr/lib64/pkgconfig/form.pc
/usr/lib64/pkgconfig/menu.pc
/usr/lib64/pkgconfig/ncurses.pc
/usr/lib64/pkgconfig/panel.pc
/usr/lib/pkgconfig/formw.pc
/usr/lib/pkgconfig/menuw.pc
/usr/lib/pkgconfig/ncurses++w.pc
/usr/lib/pkgconfig/ncursesw.pc
/usr/lib/pkgconfig/panelw.pc
/usr/share/man/
/usr/share/tabset/
/usr/share/terminfo/

%changelog
* Mon Sep 4 2023 Chris Statzer <chris.statzer@gmail.com> 
- Version bump

* Sat Jun 17 2023 Chris Statzer <chris.statzer@gmail.com> 6.4
- Bumped version to 6.4
