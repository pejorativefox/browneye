Name:       startup-notification
Version:    0.12
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.gz

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
/usr/include/startup-notification-1.0/libsn/sn-common.h
/usr/include/startup-notification-1.0/libsn/sn-launchee.h
/usr/include/startup-notification-1.0/libsn/sn-launcher.h
/usr/include/startup-notification-1.0/libsn/sn-monitor.h
/usr/include/startup-notification-1.0/libsn/sn-util.h
/usr/include/startup-notification-1.0/libsn/sn.h
/usr/lib64/libstartup-notification-1.a
/usr/lib64/libstartup-notification-1.so
/usr/lib64/libstartup-notification-1.so.0
/usr/lib64/libstartup-notification-1.so.0.0.0
/usr/lib64/pkgconfig/libstartup-notification-1.0.pc


%changelog
# let's skip this for now

