Name:       rxvt-unicode
Version:    9.22
Release:    1
Summary:    rxvt-unicode is a fork of the well known terminal emulator rxvt.
License:    GPL
Source0:    %{name}-%{version}.tar.bz2
Prefix:     /usr

%description
rxvt-unicode is a fork of the well known terminal emulator rxvt.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/urxvt
/usr/bin/urxvtc
/usr/bin/urxvtd
/usr/lib64/urxvt/perl/
/usr/lib64/urxvt/urxvt.pm
/usr/share/man/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 9.22-1
- Initial RPM

