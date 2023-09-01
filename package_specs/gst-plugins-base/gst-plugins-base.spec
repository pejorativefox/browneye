Name:       gst-plugins-base
Version:    1.16.2
Release:    1
Summary:    Base gstreamer plugins
License:    Various
Source0:    %{name}-%{version}.tar.xz
Prefix:     /usr

%description
Base gstreamer plugins

%prep
%setup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/gst-device-monitor-1.0
/usr/bin/gst-discoverer-1.0
/usr/bin/gst-play-1.0
/usr/include/gstreamer-1.0/
/usr/lib64/
/usr/share/

%changelog
* Thu Sep 10 2020 Chris Statzer <chris.statzer@qq.com> 1.16.2
- Initial RPM

