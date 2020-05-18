Name:       tzdb
Version:    2020a
Release:    2
Summary:    The Time Zone Database
License:    NO_IDEA
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
The Time Zone Database

%prep
%setup

%build
%make_build

%install
rm -rf %{buildroot}
%make_install

rm %{buildroot}/usr/bin/tzselect
rm %{buildroot}/usr/sbin/zic

%files
/etc/localtime
/usr/bin/zdump
/usr/lib/libtz.a
/usr/share/man/man3/newctime.3.gz
/usr/share/man/man3/newtzset.3.gz
/usr/share/man/man5/tzfile.5.gz
/usr/share/man/man8/tzselect.8.gz
/usr/share/man/man8/zdump.8.gz
/usr/share/man/man8/zic.8.gz
/usr/share/zoneinfo-posix
/usr/share/zoneinfo-leaps/
/usr/share/zoneinfo/

%changelog
* Sun May 17 2020 Chris Statzer <chris.statzer@qq.com> 2020a
- Initial RPM

