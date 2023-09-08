Name:       fribidi
Version:    1.0.13
Release:    1
Summary:    GNU FriBidi 
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.xz

Provides: pkgconfig(fribidi)

%description
The Free Implementation of the Unicode Bidirectional Algorithm.

%prep
%setup -q

%build
mkdir build-glib
pushd build-glib

meson --prefix=/usr ..
ninja
popd

%install    
rm -rf %{buildroot}
pushd build-glib
DESTDIR=%{buildroot} ninja install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/fribidi
/usr/include/fribidi/fribidi-arabic.h
/usr/include/fribidi/fribidi-begindecls.h
/usr/include/fribidi/fribidi-bidi-types-list.h
/usr/include/fribidi/fribidi-bidi-types.h
/usr/include/fribidi/fribidi-bidi.h
/usr/include/fribidi/fribidi-brackets.h
/usr/include/fribidi/fribidi-char-sets-list.h
/usr/include/fribidi/fribidi-char-sets.h
/usr/include/fribidi/fribidi-common.h
/usr/include/fribidi/fribidi-config.h
/usr/include/fribidi/fribidi-deprecated.h
/usr/include/fribidi/fribidi-enddecls.h
/usr/include/fribidi/fribidi-flags.h
/usr/include/fribidi/fribidi-joining-types-list.h
/usr/include/fribidi/fribidi-joining-types.h
/usr/include/fribidi/fribidi-joining.h
/usr/include/fribidi/fribidi-mirroring.h
/usr/include/fribidi/fribidi-shape.h
/usr/include/fribidi/fribidi-types.h
/usr/include/fribidi/fribidi-unicode-version.h
/usr/include/fribidi/fribidi-unicode.h
/usr/include/fribidi/fribidi.h
/usr/lib64/libfribidi.so
/usr/lib64/libfribidi.so.0
/usr/lib64/libfribidi.so.0.4.0
/usr/lib64/pkgconfig/fribidi.pc
/usr/share/man/man3/fribidi_charset_to_unicode.3.gz
/usr/share/man/man3/fribidi_debug_status.3.gz
/usr/share/man/man3/fribidi_get_bidi_type.3.gz
/usr/share/man/man3/fribidi_get_bidi_type_name.3.gz
/usr/share/man/man3/fribidi_get_bidi_types.3.gz
/usr/share/man/man3/fribidi_get_bracket.3.gz
/usr/share/man/man3/fribidi_get_bracket_types.3.gz
/usr/share/man/man3/fribidi_get_joining_type.3.gz
/usr/share/man/man3/fribidi_get_joining_type_name.3.gz
/usr/share/man/man3/fribidi_get_joining_types.3.gz
/usr/share/man/man3/fribidi_get_mirror_char.3.gz
/usr/share/man/man3/fribidi_get_par_direction.3.gz
/usr/share/man/man3/fribidi_get_par_embedding_levels.3.gz
/usr/share/man/man3/fribidi_get_par_embedding_levels_ex.3.gz
/usr/share/man/man3/fribidi_get_type.3.gz
/usr/share/man/man3/fribidi_get_type_internal.3.gz
/usr/share/man/man3/fribidi_join_arabic.3.gz
/usr/share/man/man3/fribidi_log2vis.3.gz
/usr/share/man/man3/fribidi_log2vis_get_embedding_levels.3.gz
/usr/share/man/man3/fribidi_mirroring_status.3.gz
/usr/share/man/man3/fribidi_parse_charset.3.gz
/usr/share/man/man3/fribidi_remove_bidi_marks.3.gz
/usr/share/man/man3/fribidi_reorder_line.3.gz
/usr/share/man/man3/fribidi_reorder_nsm_status.3.gz
/usr/share/man/man3/fribidi_set_debug.3.gz
/usr/share/man/man3/fribidi_set_mirroring.3.gz
/usr/share/man/man3/fribidi_set_reorder_nsm.3.gz
/usr/share/man/man3/fribidi_shape.3.gz
/usr/share/man/man3/fribidi_shape_arabic.3.gz
/usr/share/man/man3/fribidi_shape_mirroring.3.gz
/usr/share/man/man3/fribidi_unicode_to_charset.3.gz


%changelog
* Wed Sep 6 2023 Chris Statzer <chris.statzer@gmail.com> 1.0.13-1
- Version bump
