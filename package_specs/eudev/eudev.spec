Name:       eudev
Version:    3.2.12
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
%configure  --prefix=/usr           \
            --bindir=/sbin          \
            --sbindir=/sbin         \
            --libdir=/usr/lib       \
            --sysconfdir=/etc       \
            --libexecdir=/lib       \
            --with-rootprefix=      \
            --with-rootlibdir=/lib  \
            --enable-manpages       \
            --disable-static        \
            --config-cache
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv %{buildroot}/lib64/udev/rules.d
mkdir -pv %{buildroot}/etc/udev/rules.d


%files
/etc/udev/rules.d/
/lib64/udev/rules.d/
/etc/udev/hwdb.d/
/etc/udev/udev.conf
/lib/libudev.so.1
/lib/libudev.so.1.6.3
/lib/udev/
/sbin/udevadm
/sbin/udevd
/usr/include/libudev.h
/usr/include/udev.h
/usr/lib/libudev.so
/usr/lib/pkgconfig/libudev.pc
/usr/share/man/man5/udev.conf.5.gz
/usr/share/man/man7/udev.7.gz
/usr/share/man/man8/udevadm.8.gz
/usr/share/man/man8/udevd.8.gz
/usr/share/pkgconfig/udev.pc
/usr/share/man/man7/hwdb.7.gz

%changelog
# let's skip this for now
