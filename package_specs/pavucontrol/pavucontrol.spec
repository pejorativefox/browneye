Name:       pavucontrol
Version:    3.0
Release:    1
Summary:    Pulse Audio volume mixer
License:    GPL
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK based volume control tool ("mixer") for the PulseAudio sound server.

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/pavucontrol
/usr/share/applications/pavucontrol.desktop
/usr/share/doc/pavucontrol/README.html
/usr/share/doc/pavucontrol/style.css
/usr/share/locale/
/usr/share/pavucontrol/pavucontrol.glade

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 3.0
- Initial RPM

