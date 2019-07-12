Name:       xbitmaps
Version:    1.1.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2



%description
TODO

%prep
%setup -a 0

%build
%configure 
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/include/X11/bitmaps/1x1
/usr/include/X11/bitmaps/2x2
/usr/include/X11/bitmaps/black
/usr/include/X11/bitmaps/black6
/usr/include/X11/bitmaps/box6
/usr/include/X11/bitmaps/boxes
/usr/include/X11/bitmaps/calculator
/usr/include/X11/bitmaps/cntr_ptr
/usr/include/X11/bitmaps/cntr_ptrmsk
/usr/include/X11/bitmaps/cross_weave
/usr/include/X11/bitmaps/dimple1
/usr/include/X11/bitmaps/dimple3
/usr/include/X11/bitmaps/dot
/usr/include/X11/bitmaps/dropbar7
/usr/include/X11/bitmaps/dropbar8
/usr/include/X11/bitmaps/escherknot
/usr/include/X11/bitmaps/flagdown
/usr/include/X11/bitmaps/flagup
/usr/include/X11/bitmaps/flipped_gray
/usr/include/X11/bitmaps/gray
/usr/include/X11/bitmaps/gray1
/usr/include/X11/bitmaps/gray3
/usr/include/X11/bitmaps/grid16
/usr/include/X11/bitmaps/grid2
/usr/include/X11/bitmaps/grid4
/usr/include/X11/bitmaps/grid8
/usr/include/X11/bitmaps/hlines2
/usr/include/X11/bitmaps/hlines3
/usr/include/X11/bitmaps/icon
/usr/include/X11/bitmaps/keyboard16
/usr/include/X11/bitmaps/left_ptr
/usr/include/X11/bitmaps/left_ptrmsk
/usr/include/X11/bitmaps/letters
/usr/include/X11/bitmaps/light_gray
/usr/include/X11/bitmaps/mailempty
/usr/include/X11/bitmaps/mailemptymsk
/usr/include/X11/bitmaps/mailfull
/usr/include/X11/bitmaps/mailfullmsk
/usr/include/X11/bitmaps/mensetmanus
/usr/include/X11/bitmaps/menu10
/usr/include/X11/bitmaps/menu12
/usr/include/X11/bitmaps/menu16
/usr/include/X11/bitmaps/menu6
/usr/include/X11/bitmaps/menu8
/usr/include/X11/bitmaps/noletters
/usr/include/X11/bitmaps/opendot
/usr/include/X11/bitmaps/opendotMask
/usr/include/X11/bitmaps/plaid
/usr/include/X11/bitmaps/right_ptr
/usr/include/X11/bitmaps/right_ptrmsk
/usr/include/X11/bitmaps/root_weave
/usr/include/X11/bitmaps/scales
/usr/include/X11/bitmaps/sipb
/usr/include/X11/bitmaps/star
/usr/include/X11/bitmaps/starMask
/usr/include/X11/bitmaps/stipple
/usr/include/X11/bitmaps/target
/usr/include/X11/bitmaps/terminal
/usr/include/X11/bitmaps/tie_fighter
/usr/include/X11/bitmaps/vlines2
/usr/include/X11/bitmaps/vlines3
/usr/include/X11/bitmaps/weird_size
/usr/include/X11/bitmaps/wide_weave
/usr/include/X11/bitmaps/wingdogs
/usr/include/X11/bitmaps/woman
/usr/include/X11/bitmaps/xfd_icon
/usr/include/X11/bitmaps/xlogo11
/usr/include/X11/bitmaps/xlogo16
/usr/include/X11/bitmaps/xlogo32
/usr/include/X11/bitmaps/xlogo64
/usr/include/X11/bitmaps/xsnow
/usr/share/pkgconfig/xbitmaps.pc

%changelog
# let's skip this for now
