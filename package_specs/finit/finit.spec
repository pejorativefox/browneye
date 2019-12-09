
Name:       finit
Version:    3.2
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}-rc1.tar.xz



%description
TODO

%prep
%setup -a 0 -n finit-3.2-rc1

%build
%configure --enable-dbus-plugin --enable-rw-rootfs --enable-progress 
%make_build

%install
#rm -rf %{buildroot}
%make_install

%files
/usr/bin/logit
/usr/include/finit/*
/usr/lib64/finit/*
/usr/sbin/finit
/usr/sbin/halt
/usr/sbin/init
/usr/sbin/initctl
/usr/sbin/poweroff
/usr/sbin/reboot
/usr/sbin/shutdown
/usr/sbin/suspend
/usr/sbin/telinit
/usr/share/doc/finit/*


%changelog
# let's skip this for now
