Name:       bspwm
Version:    0.9.9
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

%make_build

%install
export PREFIX=/usr
rm -rf %{buildroot}
%make_install

%files
/usr/bin/bspc
/usr/bin/bspwm
/usr/share/bash-completion/completions/bspc
/usr/share/doc/bspwm/CHANGELOG.md
/usr/share/doc/bspwm/CONTRIBUTING.md
/usr/share/doc/bspwm/INSTALL.md
/usr/share/doc/bspwm/MISC.md
/usr/share/doc/bspwm/README.md
/usr/share/doc/bspwm/TODO.md
/usr/share/doc/bspwm/examples/bspwmrc
/usr/share/doc/bspwm/examples/external_rules/bspwmrc
/usr/share/doc/bspwm/examples/external_rules/external_rules
/usr/share/doc/bspwm/examples/overlapping_borders/bspwmrc
/usr/share/doc/bspwm/examples/panel/bspwmrc
/usr/share/doc/bspwm/examples/panel/panel
/usr/share/doc/bspwm/examples/panel/panel_bar
/usr/share/doc/bspwm/examples/panel/panel_colors
/usr/share/doc/bspwm/examples/panel/profile
/usr/share/doc/bspwm/examples/panel/sxhkdrc
/usr/share/doc/bspwm/examples/receptacles/README.md
/usr/share/doc/bspwm/examples/receptacles/extract_canvas
/usr/share/doc/bspwm/examples/receptacles/induce_rules
/usr/share/doc/bspwm/examples/sxhkdrc
/usr/share/fish/vendor_completions.d/bspc.fish
/usr/share/man/man1/bspc.1.gz
/usr/share/man/man1/bspwm.1.gz
/usr/share/xsessions/bspwm.desktop
/usr/share/zsh/site-functions/_bspc

%changelog
# let's skip this for now
