Name:       rofi
Version:    1.5.4
Release:    1
Summary:    Rofi application launcher.
License:    GPL
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
Rofi application launcher

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/rofi
/usr/bin/rofi-sensible-terminal
/usr/bin/rofi-theme-selector
/usr/include/rofi/helper.h
/usr/include/rofi/mode-private.h
/usr/include/rofi/mode.h
/usr/include/rofi/rofi-icon-fetcher.h
/usr/include/rofi/rofi-types.h
/usr/lib64/pkgconfig/rofi.pc
/usr/share/man/man1/rofi-sensible-terminal.1.gz
/usr/share/man/man1/rofi-theme-selector.1.gz
/usr/share/man/man1/rofi.1.gz
/usr/share/man/man5/rofi-theme.5.gz
/usr/share/rofi/*

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 1.5.4
- Initial RPM

