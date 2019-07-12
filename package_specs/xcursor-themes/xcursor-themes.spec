Name:       xcursor-themes
Version:    1.0.6
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
/usr/share/icons/handhelds/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/handhelds/cursors/X_cursor
/usr/share/icons/handhelds/cursors/arrow
/usr/share/icons/handhelds/cursors/based_arrow_down
/usr/share/icons/handhelds/cursors/based_arrow_up
/usr/share/icons/handhelds/cursors/bottom_left_corner
/usr/share/icons/handhelds/cursors/bottom_right_corner
/usr/share/icons/handhelds/cursors/bottom_side
/usr/share/icons/handhelds/cursors/bottom_tee
/usr/share/icons/handhelds/cursors/center_ptr
/usr/share/icons/handhelds/cursors/circle
/usr/share/icons/handhelds/cursors/cross
/usr/share/icons/handhelds/cursors/cross_reverse
/usr/share/icons/handhelds/cursors/crosshair
/usr/share/icons/handhelds/cursors/dot
/usr/share/icons/handhelds/cursors/dotbox
/usr/share/icons/handhelds/cursors/double_arrow
/usr/share/icons/handhelds/cursors/draft_large
/usr/share/icons/handhelds/cursors/draft_small
/usr/share/icons/handhelds/cursors/draped_box
/usr/share/icons/handhelds/cursors/fleur
/usr/share/icons/handhelds/cursors/gumby
/usr/share/icons/handhelds/cursors/hand2
/usr/share/icons/handhelds/cursors/left_ptr
/usr/share/icons/handhelds/cursors/left_ptr_watch
/usr/share/icons/handhelds/cursors/left_side
/usr/share/icons/handhelds/cursors/left_tee
/usr/share/icons/handhelds/cursors/ll_angle
/usr/share/icons/handhelds/cursors/pencil
/usr/share/icons/handhelds/cursors/plus
/usr/share/icons/handhelds/cursors/right_ptr
/usr/share/icons/handhelds/cursors/right_side
/usr/share/icons/handhelds/cursors/right_tee
/usr/share/icons/handhelds/cursors/sb_h_double_arrow
/usr/share/icons/handhelds/cursors/sb_right_arrow
/usr/share/icons/handhelds/cursors/sb_up_arrow
/usr/share/icons/handhelds/cursors/sb_v_double_arrow
/usr/share/icons/handhelds/cursors/shuttle
/usr/share/icons/handhelds/cursors/tcross
/usr/share/icons/handhelds/cursors/top_left_arrow
/usr/share/icons/handhelds/cursors/top_left_corner
/usr/share/icons/handhelds/cursors/top_right_corner
/usr/share/icons/handhelds/cursors/top_side
/usr/share/icons/handhelds/cursors/top_tee
/usr/share/icons/handhelds/cursors/watch
/usr/share/icons/handhelds/cursors/xterm
/usr/share/icons/redglass/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/redglass/cursors/X_cursor
/usr/share/icons/redglass/cursors/arrow
/usr/share/icons/redglass/cursors/based_arrow_down
/usr/share/icons/redglass/cursors/based_arrow_up
/usr/share/icons/redglass/cursors/bottom_left_corner
/usr/share/icons/redglass/cursors/bottom_right_corner
/usr/share/icons/redglass/cursors/bottom_side
/usr/share/icons/redglass/cursors/bottom_tee
/usr/share/icons/redglass/cursors/center_ptr
/usr/share/icons/redglass/cursors/circle
/usr/share/icons/redglass/cursors/cross
/usr/share/icons/redglass/cursors/cross_reverse
/usr/share/icons/redglass/cursors/crosshair
/usr/share/icons/redglass/cursors/dot
/usr/share/icons/redglass/cursors/dotbox
/usr/share/icons/redglass/cursors/double_arrow
/usr/share/icons/redglass/cursors/draft_large
/usr/share/icons/redglass/cursors/draft_small
/usr/share/icons/redglass/cursors/draped_box
/usr/share/icons/redglass/cursors/fleur
/usr/share/icons/redglass/cursors/gumby
/usr/share/icons/redglass/cursors/hand2
/usr/share/icons/redglass/cursors/left_ptr
/usr/share/icons/redglass/cursors/left_ptr_watch
/usr/share/icons/redglass/cursors/left_side
/usr/share/icons/redglass/cursors/left_tee
/usr/share/icons/redglass/cursors/ll_angle
/usr/share/icons/redglass/cursors/pencil
/usr/share/icons/redglass/cursors/plus
/usr/share/icons/redglass/cursors/right_ptr
/usr/share/icons/redglass/cursors/right_side
/usr/share/icons/redglass/cursors/right_tee
/usr/share/icons/redglass/cursors/sb_h_double_arrow
/usr/share/icons/redglass/cursors/sb_right_arrow
/usr/share/icons/redglass/cursors/sb_up_arrow
/usr/share/icons/redglass/cursors/sb_v_double_arrow
/usr/share/icons/redglass/cursors/shuttle
/usr/share/icons/redglass/cursors/tcross
/usr/share/icons/redglass/cursors/top_left_arrow
/usr/share/icons/redglass/cursors/top_left_corner
/usr/share/icons/redglass/cursors/top_right_corner
/usr/share/icons/redglass/cursors/top_side
/usr/share/icons/redglass/cursors/top_tee
/usr/share/icons/redglass/cursors/watch
/usr/share/icons/redglass/cursors/xterm
/usr/share/icons/whiteglass/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/whiteglass/cursors/X_cursor
/usr/share/icons/whiteglass/cursors/arrow
/usr/share/icons/whiteglass/cursors/base_arrow_down
/usr/share/icons/whiteglass/cursors/base_arrow_up
/usr/share/icons/whiteglass/cursors/boat
/usr/share/icons/whiteglass/cursors/bottom_left_corner
/usr/share/icons/whiteglass/cursors/bottom_right_corner
/usr/share/icons/whiteglass/cursors/bottom_side
/usr/share/icons/whiteglass/cursors/bottom_tee
/usr/share/icons/whiteglass/cursors/center_ptr
/usr/share/icons/whiteglass/cursors/circle
/usr/share/icons/whiteglass/cursors/cross
/usr/share/icons/whiteglass/cursors/cross_reverse
/usr/share/icons/whiteglass/cursors/crosshair
/usr/share/icons/whiteglass/cursors/dnd-none
/usr/share/icons/whiteglass/cursors/dot
/usr/share/icons/whiteglass/cursors/dot_box_mask
/usr/share/icons/whiteglass/cursors/double_arrow
/usr/share/icons/whiteglass/cursors/draft_large
/usr/share/icons/whiteglass/cursors/draft_small
/usr/share/icons/whiteglass/cursors/draped_box
/usr/share/icons/whiteglass/cursors/exchange
/usr/share/icons/whiteglass/cursors/fleur
/usr/share/icons/whiteglass/cursors/grab
/usr/share/icons/whiteglass/cursors/gumby
/usr/share/icons/whiteglass/cursors/hand
/usr/share/icons/whiteglass/cursors/hand1
/usr/share/icons/whiteglass/cursors/hand2
/usr/share/icons/whiteglass/cursors/left_ptr
/usr/share/icons/whiteglass/cursors/left_ptr_watch
/usr/share/icons/whiteglass/cursors/left_side
/usr/share/icons/whiteglass/cursors/left_tee
/usr/share/icons/whiteglass/cursors/ll_angle
/usr/share/icons/whiteglass/cursors/lr_angle
/usr/share/icons/whiteglass/cursors/pencil
/usr/share/icons/whiteglass/cursors/pirate
/usr/share/icons/whiteglass/cursors/plus
/usr/share/icons/whiteglass/cursors/pointer
/usr/share/icons/whiteglass/cursors/question_arrow
/usr/share/icons/whiteglass/cursors/right_ptr
/usr/share/icons/whiteglass/cursors/right_side
/usr/share/icons/whiteglass/cursors/right_tee
/usr/share/icons/whiteglass/cursors/sailboat
/usr/share/icons/whiteglass/cursors/sb_down_arrow
/usr/share/icons/whiteglass/cursors/sb_h_double_arrow
/usr/share/icons/whiteglass/cursors/sb_left_arrow
/usr/share/icons/whiteglass/cursors/sb_right_arrow
/usr/share/icons/whiteglass/cursors/sb_up_arrow
/usr/share/icons/whiteglass/cursors/sb_v_double_arrow
/usr/share/icons/whiteglass/cursors/shuttle
/usr/share/icons/whiteglass/cursors/sizing
/usr/share/icons/whiteglass/cursors/target
/usr/share/icons/whiteglass/cursors/tcross
/usr/share/icons/whiteglass/cursors/top_left_arrow
/usr/share/icons/whiteglass/cursors/top_left_corner
/usr/share/icons/whiteglass/cursors/top_right_corner
/usr/share/icons/whiteglass/cursors/top_side
/usr/share/icons/whiteglass/cursors/top_tee
/usr/share/icons/whiteglass/cursors/trek
/usr/share/icons/whiteglass/cursors/ul_angle
/usr/share/icons/whiteglass/cursors/ur_angle
/usr/share/icons/whiteglass/cursors/watch
/usr/share/icons/whiteglass/cursors/xterm


%changelog
# let's skip this for now

